from cryptojwt.jwx import key_from_jwk_dict

from bobifi.samtrafiken import prod, test


def test_jwks():
    _ = [key_from_jwk_dict(k) for k in test.JWKS_DICT["keys"]]
    _ = [key_from_jwk_dict(k) for k in prod.JWKS_DICT["keys"]]
