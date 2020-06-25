import os
import sys
import logging
from datetime import datetime
from util.julian_datetime import get_julian_datetime
from csv import writer as csv_writer
from argparse import ArgumentParser
from contextlib import contextmanager
from importlib import import_module
from pyomo.environ import SolverFactory
from pyomo.opt import SolverStatus
from pyomo.opt import TerminationCondition as tc
from util.parse_to_gams import (termination_condition_to_gams_format,
                                solver_status_to_gams)
from datetime import datetime


def parse_command_line_arguments():
    parser = ArgumentParser(
        description='Benchmark specified solver on problem files')
    parser.add_argument('--redo-existing', dest='skip_existing', default=True,
                        action='store_const', const=False,
                        help='Redo benchmark if result file is already existing')
    parser.add_argument('--no-skip-failed', dest='skip_failed', default=True,
                        action='store_const', const=False,
                        help="Skip file if file in 'failed_models.txt'")
    parser.add_argument('--solver', dest='solver_name', type=str, required=True,
                        metavar='solver_name',
                        choices=['baron', 'mindtpy', 'feas-pump'])
    parser.add_argument('--strategy', dest='solver_strategy', type=str,
                        required=False, metavar='solver_strategy', default="OA",
                        help='Solver strategy (if applicable)')
    parser.add_argument('--timelimit', dest='timelimit', type=int,
                        required=False, metavar='timelimit', default=60,
                        help='Time limit (sec) for each model')
    parser.add_argument('--model-dir', dest='model_dir', default='models',
                        required=False, metavar='model_dir',
                        help='Directory where models are stored as .py files')
    parser.add_argument('--single-tree', dest='single_tree', default=False,
                        action='store_const', const=True,
                        help='Call single-tree implementation of MindtPy')
    parser.add_argument('--feasibility-norm', dest='feasibility_norm', type=str, default='L1',
                        required=False, metavar='feasibility_norm', choices=['L1', 'L2', 'L_infinity'])
    parser.add_argument('--differentiate-mode', dest='differentiate_mode', type=str, default="reverse_symbolic",
                        required=False, metavar='differentiate_mode', choices=["reverse_symbolic", "sympy"])
    parser.add_argument('--mip-solver', dest='mip_solver', type=str, default='gurobi',
                        required=False, metavar='mip_solver')
    parser.add_argument('--linearize-inactive', dest='linearize_inactive', default=False,
                        action='store_const', const=True,
                        help='Add OA cuts for all constriants no matter active or inactive')
    parser.add_argument('--nlp-solver', dest='nlp_solver', type=str, default='ipopt',
                        required=False, metavar='nlp_solver')
    parser.add_argument('--method-name', dest='method_name', type=str, default='',
                        required=False, metavar='method_name')
    return parser.parse_args()


@contextmanager
def redirect_stdout(ofile_obj):
    original_stdout = sys.stdout
    sys.stdout = ofile_obj
    yield
    sys.stdout = original_stdout


@contextmanager
def load_model(model_name):
    global model_scope
    model_scope = import_module(model_name)
    yield
    del model_scope


def construct_trace_data(opt, results):
    problem = results['Problem'][0]
    solver = results['Solver'][0]
    if args.solver_name in ['mindtpy', 'gdpopt']:
        trace_data = [
            model_name,  # GAMS model filename
            'MINLP',     # LP, MIP, NLP, etc.
            solver['Name'] + ("LPNLP" if args.single_tree ==
                              True else "")+args.method_name,
            args.nlp_solver,  # default NLP solver
            args.mip_solver,  # default MIP solver
            get_julian_datetime(datetime.now()),  # start day/time of job
            # direction 0=min, 1=max
            0 if (problem['Sense'] ==
                  1 or problem['Sense'] == 'minimize') else 1,
            # total number of equations
            results['Problem'][0]['Number of constraints'],
            # total number of variables
            results['Problem'][0]['Number of variables'],
            results['Problem'][0]['Number of binary variables'] + \
            results['Problem'][0]['Number of integer variables'],  # total number of discrete variables
            '',  # 'nznum?',  # number of nonzeros
            '',  # 'nlz?',  # number of nonlinear nonzeros
            0,  # 1= optfile included
            # GAMS model return status - see the GAMS return codes section.
            termination_condition_to_gams_format(solver.Termination_condition),
            # GAMS solver return status - see the GAMS return codes section.
            solver_status_to_gams(solver.Status) if solver.Status is SolverStatus.ok else termination_condition_to_gams_format(
                solver.Termination_condition),
            problem['Upper bound'],  # value of objecive function
            problem['Lower bound'],  # objective function estimate
            solver['Wallclock time'],  # resource time used (sec)
            # number of solver iterations
            solver['Iterations'] if args.single_tree == False else solver['Num nodes'],
            0,  # dom used
            0,  # nodes used
            '# automatically generated by benchmarker'
        ]
        return trace_data


def benchmark_model(timelimit):
    try:
        opt = SolverFactory(args.solver_name)
        opt.CONFIG.logger.propagate = False
        opt.CONFIG.logger.addHandler(logging.FileHandler(
            sys.stdout.name, mode=sys.stdout.mode))
        model = model_scope.m
        results = opt.solve(model, tee=True, time_limit=timelimit,
                            mip_solver=args.mip_solver,
                            nlp_solver=args.nlp_solver,
                            strategy=args.solver_strategy,
                            feasibility_norm=args.feasibility_norm,
                            differentiate_mode=args.differentiate_mode,
                            linearize_inactive=args.linearize_inactive,
                            single_tree=args.single_tree)
        # if args.solver_strategy is None:
        #     results = opt.solve(model, tee=True, time_limit=timelimit,
        #                         single_tree=args.single_tree)
        # else:
        #     results = opt.solve(model, tee=True, time_limit=timelimit,
        #                         strategy=args.solver_strategy, single_tree=args.single_tree)
        del opt.CONFIG.logger.handlers[0]
        solving_time = results.Solver[0].Wallclock_time
        print(f'Solving time: {solving_time}\n')
        if results.Solver[0].Termination_condition == tc.optimal:
            solving_times.append([model_name, solving_time])
        elif results.Solver[0].Termination_condition == tc.maxTimeLimit:
            solving_times.append([model_name, 'maxTimeLimit'])
        elif results.Solver[0].Termination_condition == tc.maxIterations:
            solving_times.append([model_name, 'maxIterations'])
        trace_data = construct_trace_data(opt, results)
        trace_file_obj.write(', '.join(str(el) for el in trace_data) + '\n')

    except Exception as e:
        # os.remove(result_file)
        print(e)
        if model_file not in prev_failed_models:
            error_file_obj.write(model_file+'\n')
        print(f"Failed to solve '{model_file}'", file=sys.stderr)
        print(e, file=sys.stderr)
        print(f"File written to '{error_file}'", file=sys.stderr)


if __name__ == '__main__':
    args = parse_command_line_arguments()
    current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    ####### SETUP (directories and files) #######
    sys.path.insert(0, './'+args.model_dir)  # necessary to import models

    if not os.path.exists('results'):
        print("Creating new directory: './results'")
        os.makedirs('results')

    # Set various filenames
    model_files = [model_file for model_file in sorted(
        os.listdir(args.model_dir)) if model_file.endswith('.py')]
    solver_dir = args.solver_name + \
        (f"-{args.solver_strategy}" if args.solver_strategy else "") + \
        ("-LPNLP" if args.single_tree else "" + current_time)
    error_file = f"./results/{solver_dir}/failed_models.txt"
    trace_file = f"./results/{solver_dir}/trace_file.trc"
    solving_times_file = f"./results/{solver_dir}/solving_times.csv"
    if not os.path.exists('./results/'+solver_dir):
        print(f"Creating new directory: './results/{solver_dir}'")
        os.makedirs('./results/'+solver_dir)

    # Load previously failed model (or create empty file)
    prev_failed_models = set()
    try:
        with open(error_file, 'r') as error_file_obj:
            for line in error_file_obj:
                prev_failed_models.add(line.strip())
    except FileNotFoundError:
        with open(error_file, 'a'):
            pass

    solving_times = [['Instance name', 'Average solving time']]

    print('################################')
    print(f"Benchmarking solver '{args.solver_name}' " +
          ("with strategy '{args.solver_strategy}'" if args.solver_strategy else ""))
    print(f"Writing to './results/{solver_dir}'")
    print(f"Failed model files will be written to '{error_file}'")
    print(f"Trace files will be written to '{trace_file}'")
    print(f"Solving times will be written to '{solving_times_file}'")
    print('################################')

    with open(trace_file, 'w') as trace_file_obj:
        for model_file in model_files:
            model_name, _ = os.path.splitext(model_file)  # removes ending
            result_file = './results/'+solver_dir+'/'+model_name+'.txt'

            if args.skip_existing and os.path.exists(result_file):
                print(f"Skipping '{result_file}'")
                print(
                    "File exists already, please use the '--redo-existing' flag to override")
                continue

            elif args.skip_failed and model_file in prev_failed_models:
                print(f"Skipping '{result_file}'")
                print(
                    "File listed in 'failed_models.txt', please use the '--no-skip-failed' flag to override")
                continue

            else:
                print(f"Benchmarking '{model_file}'")
                # This causes all stdout to be written to the results file
                # and the model to be loaded as model_scope.m
                with open(result_file, 'w') as result_file_obj, \
                        open(error_file, 'a') as error_file_obj, \
                        redirect_stdout(result_file_obj), \
                        load_model(model_name):
                    benchmark_model(args.timelimit)

    with open(solving_times_file, 'w') as time_file:
        time_writer = csv_writer(time_file)
        time_writer.writerows(solving_times)
