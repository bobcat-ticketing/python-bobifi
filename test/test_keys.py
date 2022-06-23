import os

from cryptojwt.jwx import key_from_jwk_dict

from bobifi.samtrafiken import prod, test


def test_jwks_test():
    _ = [key_from_jwk_dict(k) for k in test.trusted_jwks()["keys"]]
    os.stat(test.where())


def test_jwks_prod():
    _ = [key_from_jwk_dict(k) for k in test.trusted_jwks()["keys"]]
    os.stat(prod.where())
