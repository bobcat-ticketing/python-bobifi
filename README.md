# BoB Metadata Keys and URLs

This repository contains a Python module with the current [BoB](https://bob.samtrafiken.se/) Metadata keys and URLs. Inspired by [certifi](https://github.com/certifi/python-certifi).


## Usage

### Swedish Production Environment

    from bobifi.samtrafiken import trusted_jwks, metadata_url, where
    print(trusted_jwks())
    print(where())
    print(metadata_url())

### Swedish Test Environment

    from bobifi.samtrafiken import trusted_jwks, metadata_url, where
    print(trusted_jwks(env="test"))
    print(where(env="test"))
    print(metadata_url(env="test"))
