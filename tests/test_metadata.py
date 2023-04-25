import httpx
import pytest

from bobifi.samtrafiken import metadata_url


def test_metadata_test():
    with httpx.Client() as client:
        _ = client.get(metadata_url(env="test", version=1))
        _ = client.get(metadata_url(env="test", version=2))


def test_metadata_prod():
    with httpx.Client() as client:
        _ = client.get(metadata_url(env="prod", version=1))
        _ = client.get(metadata_url(env="prod", version=2))


def test_metadata_version():
    url = metadata_url(env="prod")
    assert "/v2/" in url
    url = metadata_url(env="prod", version=1)
    assert "/v1/" in url
    url = metadata_url(env="prod", version=2)
    assert "/v2/" in url


def test_metadata_unknown():
    with pytest.raises(KeyError):
        _ = httpx.get(metadata_url(env="xyzzy"))
