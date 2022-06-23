# BoB Metadata Keys and URLs

This repository contains a Python module with the current [BoB](https://bob.samtrafiken.se/) Metadata keys and URLs. Inspired by [certifi](https://github.com/certifi/python-certifi).


## Usage

### Swedish Test Environment

    from bobifi.samtrafiken.test import trusted_jwks, metadata_url
    print(trusted_jwks())
    print(metadata_url())

### Swedish Production Environment

    from bobifi.samtrafiken.prod import trusted_jwks, metadata_url
    print(trusted_jwks())
    print(metadata_url())
