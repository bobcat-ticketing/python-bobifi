import httpx
import pytest
from cryptojwt import JWS
from cryptojwt.jwx import key_from_jwk_dict

from bobifi.samtrafiken import metadata_url, trusted_jwks


def verify_metadata(env: str, content: str):
    jws = JWS()
    trusted_keys = [key_from_jwk_dict(k) for k in trusted_jwks(env=env)["keys"]]
    metadata = jws.verify_json(content, keys=trusted_keys, at_least_one=True)


def test_metadata_test():
    env = "test"
    with httpx.Client() as client:
        for version in [1, 2]:
            response = client.get(metadata_url(env=env, version=version))
            response.raise_for_status()
            verify_metadata(env, response.content)


def test_metadata_prod():
    env = "prod"
    with httpx.Client() as client:
        for version in [1, 2]:
            response = client.get(metadata_url(env=env, version=version))
            response.raise_for_status()
            verify_metadata(env, response.content)


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
