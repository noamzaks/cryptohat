def transform_name(challenge_name: str):
    challenge_name = challenge_name.lower().replace(" ", "-")
    challenge_name = "".join(filter(lambda x: x.isalnum() or x == "-", challenge_name))
    return challenge_name
