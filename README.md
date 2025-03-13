# Quadratic Equation Solver

This is a command-line tool for solving quadratic equations of the form:

```
ax^2 + bx + c = 0
```

## Requirements
- Python 3.5+
- pip dependencies

## Installation
Ensure you have Python installed, then install dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### Interactive Mode
Run the script without specifying a file, and enter the coefficients manually:

```sh
python solver.py
```

The program will prompt you to enter values for `a`, `b`, and `c`.

### File Input Mode
Provide a file containing three space-separated numbers (coefficients `a b c`):

Example file (`test_valid.txt`):
```
2 1 -3
```

Run the script with:
```sh
python solver.py test_valid.txt
```

## Example Outputs

```
$ python solver.py
Enter a = 2
Enter b = 1
Enter c = -3
Equation is: (2.0) x^2 + (1.0) x + (-3.0) = 0
There are 2 roots
x1 = -1.5
x2 = 1.0
```

```
$ python solver.py input.txt
Equation is: (2.0) x^2 + (1) x + (-3) = 0
There are 2 roots
x1 = -1.5
x2 = 1.0
```

## Revert commit
[c9a77](https://github.com/elaiviaien/mtrpz_01/commit/c9a7775f4973e7f08ea08f1398ba911e43bf0172)