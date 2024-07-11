import os
import random as python_random
from importlib.machinery import SourceFileLoader

import click


@click.command()
@click.argument("filename")
@click.option("--seed", default=0)
def seed(filename: str, seed: int):
    """
    Sets the random seed and overrides `os.urandom` to use the regular random module, to make a random challenge deterministic.
    Since `Crypto.Random` uses `os.urandom` under the hood, this also overrides the pycryptodome random results.
    """

    python_random.seed(seed)

    def urandom_override(size: int):
        return python_random.randbytes(size)

    setattr(os, "urandom", urandom_override)
    SourceFileLoader("__main__", filename).load_module()
