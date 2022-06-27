import os

import pytest
from cryptojwt.jwx import key_from_jwk_dict

from bobifi.samtrafiken import trusted_jwks, where


def test_jwks_test():
    _ = [key_from_jwk_dict(k) for k in trusted_jwks(env="test")["keys"]]
    os.stat(where(env="test"))


def test_jwks_prod():
    _ = [key_from_jwk_dict(k) for k in trusted_jwks(env="prod")["keys"]]
    os.stat(where(env="prod"))


def test_jwks_unknown():
    with pytest.raises(KeyError):
        _ = trusted_jwks(env="xyzzy")
