import json

import httpx
import pytest
from jwcrypto.jws import JWS

from bobifi.samtrafiken import metadata_url, trusted_jwkset


def verify_metadata(env: str, content: str):
    jws = JWS()
    jws.deserialize(content)

    signatures = jws.objects["signatures"]
    print(f"{len(signatures)} signatures found")
    for signature in signatures:
        protected_header = json.loads(signature["protected"])
        kid = protected_header["kid"]
        serial = protected_header["serial"]
        not_valid_before = protected_header["notvalidbefore"]
        not_valid_after = protected_header["notvalidafter"]
        print(
            f"- {kid} serial {serial} valid from {not_valid_before} to {not_valid_after}"
        )
    jws.verify(trusted_jwkset(env=env))


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
