import click

from cryptohat.cli.seed import seed
from cryptohat.cli.download import download
from cryptohat.cli.list import list


@click.group()
def cli():
    pass


def main():
    cli.add_command(seed)
    cli.add_command(download)
    cli.add_command(list)
    cli()
