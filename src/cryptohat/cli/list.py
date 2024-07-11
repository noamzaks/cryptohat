from bs4 import BeautifulSoup
import requests
import click

from cryptohat.cli.utilities import transform_name


@click.command()
@click.option("--category", default="")
def list(category: str):
    if category == "":
        challenges = BeautifulSoup(
            requests.get("https://cryptohack.org/challenges").text, "html.parser"
        )
        for a in challenges.find_all("a"):
            if (
                "href" in a.attrs
                and a["href"] != "/challenges/"
                and a["href"].startswith("/challenges")
            ):
                print(a["href"].split("/")[2])
    else:
        c = BeautifulSoup(
            requests.get(f"https://cryptohack.org/challenges/{category}").text,
            "html.parser",
        )
        challenges = c.find_all("li", {"class": "challenge"})
        for challenge in challenges:
            name = challenge.find("div", {"class": "challenge-text"}).text
            print(f"{category}/{challenge['data-stage']}/{transform_name(name)}")
