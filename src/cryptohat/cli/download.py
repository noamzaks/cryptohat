import click
import requests
import os
from bs4 import BeautifulSoup
from halo import Halo

from cryptohat.cli.utilities import transform_name


@click.command()
@click.argument("challenge")
def download(challenge: str):
    split = challenge.split("/")

    if len(split) != 3:
        raise click.ClickException(
            "The `challenge` argument must be <category>/<stage>/<challenge>"
        )

    [category, stage, challenge_name] = split

    root = os.path.join("challenges", category, stage, challenge_name)
    os.makedirs(root, exist_ok=True)

    spinner = Halo("Fetching the category page...")
    spinner.start()

    category = BeautifulSoup(
        requests.get(f"https://cryptohack.org/challenges/{category}").text,
        "html.parser",
    )
    challenges = category.find_all("li", {"class": "challenge"})
    for challenge in challenges:
        name = challenge.find("div", {"class": "challenge-text"}).text

        if challenge["data-stage"] == stage and transform_name(name) == challenge_name:
            for a in challenge.find_all("a"):
                if a["href"].startswith("/static"):
                    filename = os.path.join(root, a.text)
                    spinner.text = f"Downloading {filename}..."

                    content = requests.get("https://cryptohack.org" + a["href"]).content

                    # Make server interactive scripts work locally
                    content = content.replace(
                        b"from utils import listener", b"from cryptohat import listener"
                    )

                    with open(filename, "wb") as f:
                        f.write(content)
            break
    else:
        spinner.stop()
        raise click.ClickException(
            "The given challenge was not found! Use the `list` command to see all challenges of a given category."
        )

    spinner.succeed("Challenge files downloaded into the `challenges` folder.")
