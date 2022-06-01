# python-exercises

This repository is a collection of exercises from the OpenEDG courses on python, starting with [Python Essentials - Part 1 (Basics)](https://edube.org/study/pe1).

To assist with my learning, I decided to build a project that would allow me to implement each exercise as a class, and use unit tests to verify each implementation.

The `Makefile` included with this project includes a number of targets to both run the tests (with coverage), but also to check the code for formatting, linting and type correctness. The make targets can be found by running:

```
% make help

Usage:
  make <target>

Targets:
  venv                 Create/activate python virtualenv
  fmt                  Format python code using black
  check-fmt            Perform code format using black
  check-lint           Perform pylint check
  check-type           Perform mypy check
  check                Perform fmt, lint and type checks
  test                 Perform unit tests
  coverage             Create coverage report
Help
  help                 Show help
```

I expect the structure of this project to change and evolve.