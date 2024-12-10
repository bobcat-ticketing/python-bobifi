from jwcrypto.jwk import JWKSet

from . import DATADIR
from .metadata import MetadataKeys

DEFAULT_VERSION = 2

JWKS_TEST_FILENAME = str(DATADIR / "samtrafiken-test.json")
JWKS_PROD_FILENAME = str(DATADIR / "samtrafiken-prod.json")


_ENVIRONMENTS = {
    1: {
        "test": MetadataKeys.from_file(
            filename=JWKS_TEST_FILENAME,
            url="https://bobmetadata-pp.samtrafiken.se/api/v1/participantMetadata",
        ),
        "prod": MetadataKeys.from_file(
            filename=JWKS_PROD_FILENAME,
            url="https://bobmetadata.samtrafiken.se/api/v1/participantMetadata",
        ),
    },
    2: {
        "test": MetadataKeys.from_file(
            filename=JWKS_TEST_FILENAME,
            url="https://bobmetadata-pp.samtrafiken.se/api/v2/participantMetadata",
        ),
        "prod": MetadataKeys.from_file(
            filename=JWKS_PROD_FILENAME,
            url="https://bobmetadata.samtrafiken.se/api/v2/participantMetadata",
        ),
    },
}


def where(env: str = "prod", version: int = DEFAULT_VERSION) -> str:
    return _ENVIRONMENTS[version][env].keys_filename


def trusted_jwks(env: str = "prod", version: int = DEFAULT_VERSION) -> dict:
    return _ENVIRONMENTS[version][env].jwkset.export(private_keys=False, as_dict=True)


def trusted_jwkset(env: str = "prod", version: int = DEFAULT_VERSION) -> JWKSet:
    return _ENVIRONMENTS[version][env].jwkset


def metadata_url(env: str = "prod", version: int = DEFAULT_VERSION) -> str:
    return _ENVIRONMENTS[version][env].metadata_url
