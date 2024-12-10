from dataclasses import dataclass

from jwcrypto.jwk import JWKSet


@dataclass(frozen=True)
class MetadataKeys:
    metadata_url: str
    keys_filename: str
    jwkset: JWKSet

    @classmethod
    def from_file(cls, filename: str, url: str):
        with open(filename) as fp:
            jwkset = JWKSet.from_json(fp.read())

        return cls(
            metadata_url=url,
            keys_filename=filename,
            jwkset=jwkset,
        )
