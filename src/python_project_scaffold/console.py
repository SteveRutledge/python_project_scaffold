# src/python_project_scaffold/console.py
import click

from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """The Python Project Scaffold"""
    click.echo("Hulo wurld!")

