# My working through the book `High Performance Python (2nd Edition)`

`https://www.oreilly.com/library/view/high-performance-python/9781492055013/`

1. Chapter 1

Testing: - create test/ folder, use pytest library, use coverage tool to progress
Docstrings to every class and function
Keep PEP8 coding standards

2. Chapter 2 - 
Throughout the chapter we work with Julia set - it's a dynamic form of Mandelbrot set, as I understood after a short investigation.
With this algorithm we can test a high computing performance.

- Instead of using lots of print statements to see how the code works, we shoul use decorators - `@` - it's a cleaner approach and could be made to more advanced level

Other ways to measure performance:
- using `timeit` module, can be used from terminal the following way - `python -m timeit -n 5 -r 1 -s "import {python_script}" \ "{python_script}.{function}({function_parameters})"` where `-m` is module, `-n` number of loops, `-r` is a number of repetitions. Also `-v` verbose could be added
- timing with standard UNIX sysmems command - used the following way: `/usr/bin/time -p python {python_script.py}`
- using `cProfile` module - `python -m cProfile -s cumulative {python_script.py}`. We can store the ouput in a separate file for a further use - `python3 -m cProfile -o profile.stats ch2_wt_decorators.py`
- later we can load it with a package `pstats` like `pstats.Stats('profile.stats')`. Some of good methods for this object are: `print_stats` (just like it was printed in the console), `print_callers` (which functions were called the most), `print_callees` (to trace where these functions were called the most)