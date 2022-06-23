import json

from .. import DATADIR

JWKS_FILE = DATADIR / "samtrafiken-prod.json"
JWKS_DICT = json.load(open(JWKS_FILE))

METADATA_URL = "https://bobmetadata.samtrafiken.se/api/v2/participantMetadata"
