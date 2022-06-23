import json

from .. import DATADIR

_JWKS_FILE = DATADIR / "samtrafiken-prod.json"
_JWKS_DICT = json.load(open(_JWKS_FILE))

_METADATA_URL = "https://bobmetadata.samtrafiken.se/api/v2/participantMetadata"


def where() -> str:
    return _JWKS_FILE


def trusted_jwks() -> dict:
    return _JWKS_DICT


def metadata_url() -> str:
    return _METADATA_URL
