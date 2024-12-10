import os

import pytest
from jwcrypto.jwk import JWK

from bobifi.samtrafiken import trusted_jwks, where


def _test_jwks(env: str) -> None:
    keys = [JWK(**key) for key in trusted_jwks(env=env)["keys"]]
    for key in keys:
        print(f"env={env}, key={key.export()}")
    os.stat(where(env=env))


def test_jwks_test():
    _test_jwks(env="test")


def test_jwks_prod():
    _test_jwks(env="prod")


def test_jwks_unknown():
    with pytest.raises(KeyError):
        _ = trusted_jwks(env="xyzzy")
