from pyomo.opt import TerminationCondition
from pyomo.opt import SolverStatus


def termination_condition_to_gams_format(tc):
    """Converts termination condition to Gams 'MODEL STATUS CODE'
        http://www.gamsworld.org/performance/status_codes.htm
    """

    if tc is TerminationCondition.unknown:
        return 12
    if tc is TerminationCondition.maxTimeLimit:
        return 13
    if tc is TerminationCondition.maxIterations:
        return 2
    if tc is TerminationCondition.minFunctionValue:
        return 1
    if tc is TerminationCondition.minStepLength:
        return 16
    if tc is TerminationCondition.globallyOptimal:
        return 1
    if tc is TerminationCondition.locallyOptimal:
        return 2
    if tc is TerminationCondition.feasible:
        return 1  # 'optimal' -> not perfect
    if tc is TerminationCondition.optimal:
        return 1
    if tc is TerminationCondition.maxEvaluations:
        return 13
    if tc is TerminationCondition.other:
        return 14
    if tc is TerminationCondition.unbounded:
        return 3
    if tc is TerminationCondition.infeasible:
        return 4
    if tc is TerminationCondition.infeasibleOrUnbounded:
        return 4
    if tc is TerminationCondition.invalidProblem:
        return 13
    if tc is TerminationCondition.intermediateNonInteger:
        return 6
    if tc is TerminationCondition.noSolution:
        return 13
    if tc is TerminationCondition.solverFailure:
        return 12
    if tc is TerminationCondition.internalSolverError:
        return 12
    if tc is TerminationCondition.error:
        return 12
    if tc is TerminationCondition.userInterrupt:
        return 8
    if tc is TerminationCondition.resourceInterrupt:
        return 3
    if tc is TerminationCondition.licensingProblems:
        return 11


def solver_status_to_gams(ss):
    """Converts solution status to Gams 'SOLVER STATUS CODE'
        http://www.gamsworld.org/performance/status_codes.htm
    """
    if ss == SolverStatus.ok:       # Normal termination
        return 1
    if ss == SolverStatus.warning:  # Termination with unusual condition
        return 6
    if ss == SolverStatus.error:    # Terminated internally with error
        return 10
    if ss == SolverStatus.aborted:  # Terminated due to external conditions
        return 4
    if ss == SolverStatus.unknown:  # An unitialized value
        return 13
