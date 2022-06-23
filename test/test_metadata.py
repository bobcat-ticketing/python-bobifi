import requests

from bobifi.samtrafiken import prod, test


def test_metadata():
    _ = requests.get(test.metadata_url())
    _ = requests.get(prod.metadata_url())
