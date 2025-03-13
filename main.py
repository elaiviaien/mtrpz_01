import click
import os
import sys
import re

def solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        click.echo("Error. a cannot be 0")
        sys.exit(1)
    
    discriminant = b**2 - 4*a*c
    click.echo(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        click.echo("There are 2 roots")
        click.echo(f"x1 = {x1}")
        click.echo(f"x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        click.echo("There are 1 roots")
        click.echo(f"x1 = {x}")
    else:
        click.echo("There are 0 roots")


def get_float_input(prompt: str):
    while True:
        value = input(f"{prompt} = ")
        try:
            return float(value)
        except ValueError:
            click.echo(f"Error. Expected a valid real number, got {value} instead")


@click.command()
@click.argument('file', required=False, type=click.Path(exists=True))
def main(file):
    if file:
        try:
            with open(file, 'r') as f:
                content = f.read().strip()
                match = re.fullmatch(r'([-+]?[0-9]*\.?[0-9]+)\s([-+]?[0-9]*\.?[0-9]+)\s([-+]?[0-9]*\.?[0-9]+)', content)
                if not match:
                    raise ValueError("invalid file format")
                a, b, c = map(float, match.groups())
                solve_quadratic(a, b, c)
        except FileNotFoundError:
            click.echo(f"file {file} does not exist")
            sys.exit(1)
        except ValueError as e:
            click.echo(str(e))
            sys.exit(1)
    else:
        a = get_float_input("a")
        b = get_float_input("b")
        c = get_float_input("c")
    solve_quadratic(a, b, c)

if __name__ == "__main__":
    main()