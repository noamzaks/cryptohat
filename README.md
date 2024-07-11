# 🎩 CryptoHat

Utilities for working on [CryptoHack](https://cryptohack.org) challenges.

## Features

### Running interactive challenges locally

You can run any interactive challenge locally by simply changing the import `from utils import listener` to be `from cryptohat import listener`.

### Seeding the randomness

You can run any Python script, and in particular an interactive challenge running locally with a fixed random seed.
This works whenever the script uses `os.urandom`, the Python `random` module, or pycryptodome's `random` module.

Example usage:

```sh
cryptohat seed challenges/web/cloud/megalomaniac-1/13408.py
cryptohat seed challenges/web/cloud/megalomaniac-1/13408.py --seed 1574
```

### Connecting to interactive challenges

A useful client for connecting to interactive challenges is available by using `from cryptohat.client import Client`. You can also use the shorthands `LocalClient` and `RemoteClient` classes for challenges running locally or on the CryptoHack server accordingly.

## Getting Started

-   Clone this repository (`git clone https://github.com/noamzaks/cryptohat.git`).
-   (Optional) Set up Sage Math support by running the following command (you will probably need to change the Sage Math python3 path):

    ```sh
    rye toolchain register --name sage /Applications/SageMath-10-3.app/Contents/Frameworks/Sage.framework/Versions/10.3/local/var/lib/sage/venv-python3.11.8/bin/python3
    rye pin sage@3.11
    ```

    If you do this, whenever you want to have Sage Math when running a script, you'll need to set the `PYTHONPATH` accordingly, in my case: `PYTHONPATH=/Applications/SageMath-10-3.app/Contents/Frameworks/Sage.framework/Versions/10.3/local/var/lib/sage/venv-python3.11.8/lib/python3.11/site-packages`.

-   Create a virtual environment and install the dependencies by running `rye sync` inside the repository.
-   Activate this virtual environment, and then you should have the `cryptohat` binary.

_Note: VSCode should use the virtual environment set up by rye by default._
