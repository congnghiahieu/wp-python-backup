""" More at: https://click.palletsprojects.com/en"""

import click


@click.group()
def cli():
    pass


@click.command()
@click.option("--name", "-n", prompt="Enter your name")
@click.option(
    "--language",
    "-l",
    type=click.Choice(["vi", "jp", "ascii"], case_sensitive=False),
    prompt="Choose your language",
)
def run(language, name) -> None:
    click.echo(name)
    click.echo(language)


cli.add_command(run)

if __name__ == "__main__":
    cli()
