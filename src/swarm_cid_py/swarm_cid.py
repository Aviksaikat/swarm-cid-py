import binascii
from hashlib import sha256
from types import Reference, ReferenceType
from typing import Union

from eth_utils import keccak
from Exceptions import ReferenceError
from multiformats_cid import CIDv1, make_cid

# https://github.com/multiformats/multicodec/blob/master/table.csv

KECCAK_256_CODEC = 0x1B
SWARM_NS_CODEC = 0xE4
SWARM_MANIFEST_CODEC = 0xFA
SWARM_FEED_CODEC = 0xFB
REFERENCE_HEX_LENGTH = 64


def hexToBytes(ref: str) -> bytes:
    return bytes.fromhex(ref)


def _encodeReference(ref: Union[str, Reference], codec: int) -> CIDv1:
    hash_bytes = hexToBytes(ref)
    return make_cid(codec, keccak(hash_bytes))  # type: ignore


def encodeReference(ref: Union[str, Reference], type: ReferenceType) -> CIDv1:
    if type == ReferenceType.FEED:
        return _encodeReference(ref, SWARM_FEED_CODEC)
    elif type == ReferenceType.MANIFEST:
        return _encodeReference(ref, SWARM_MANIFEST_CODEC)
    return ReferenceError("Unknown reference type.")
