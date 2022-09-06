import pytest
import requests

from bobifi.samtrafiken import metadata_url


def test_metadata_test():
    _ = requests.get(metadata_url(env="test", version=1))
    _ = requests.get(metadata_url(env="test", version=2))


def test_metadata_prod():
    _ = requests.get(metadata_url(env="prod", version=1))
    _ = requests.get(metadata_url(env="prod", version=2))


def test_metadata_version():
    url = metadata_url(env="prod")
    assert "/v2/" in url
    url = metadata_url(env="prod", version=1)
    assert "/v1/" in url
    url = metadata_url(env="prod", version=2)
    assert "/v2/" in url


def test_metadata_unknown():
    with pytest.raises(KeyError):
        _ = requests.get(metadata_url(env="xyzzy"))
