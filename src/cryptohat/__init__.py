import click

from cryptohat.seed import seed


@click.group()
def cli():
    pass


def main():
    cli.add_command(seed)
    cli()
