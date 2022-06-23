import json

from .. import DATADIR

JWKS_FILE = DATADIR / "samtrafiken-test.json"
JWKS_DICT = json.load(open(JWKS_FILE))

METADATA_URL = "https://bobmetadata-pp.samtrafiken.se/api/v2/participantMetadata"
