# pyomo-MINLP-benchmarking

# What is this?
This repository mostly contains the `run_benchmarks.py` script as well as
a collection of MINLP problems/models, which have been taken from the
[MINLPlib](http://www.minlplib.org/) and converted to [Pyomo](https://github.com/Pyomo/pyomo) models with the
`translate.py` file.

# Example usage

When running

```sh
python run_benchmarks.py -h  # show some help
python run_benchmarks.py --solver mindtpy --model-dir models
# or, when re-running
python run_benchmarks.py --solver mindtpy --model-dir models --redo-existing --no-skip-failed
```
After running, the `results/<solver>` dir will contain a `.txt` file for
each model output, aswell as a `trace_file.trc` which can be loaded into 
??? to generate automatic benchmarking plots (not yet tested).
