import requests

from bobifi.samtrafiken import metadata_url


def test_metadata_test():
    _ = requests.get(metadata_url(env="test"))

def test_metadata_prod():
    _ = requests.get(metadata_url(env="prod"))
