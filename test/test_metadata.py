import requests

from bobifi.samtrafiken import prod, test


def test_metadata():
    _ = requests.get(test.METADATA_URL)
    _ = requests.get(prod.METADATA_URL)
