import binascii
from typing import Union, Dict

from eth_utils import keccak
from multiformats_cid import CIDv0, CIDv1, from_string, make_cid

from .Exceptions import ReferenceError
from .types import DecodeResult, Reference, ReferenceType

# https://github.com/multiformats/multicodec/blob/master/table.csv

# constants values on hex format which evaluates to ints
KECCAK_256_CODEC = 0x1B
SWARM_NS_CODEC = 0xE4
SWARM_MANIFEST_CODEC = 0xFA
SWARM_FEED_CODEC = 0xFB
REFERENCE_HEX_LENGTH = 64

TYPE_MAPPING: Dict[int, str] = {
    SWARM_FEED_CODEC: ReferenceType.FEED,
    SWARM_MANIFEST_CODEC: ReferenceType.MANIFEST,
}


def hexToBytes(ref: str) -> bytes:
    """
    converts a string to a byte array
    """
    # if ref starts with 0x remove it
    if ref.startswith("0x"):
        ref = ref[2:]
    return binascii.unhexlify(ref)


def bytesTohex(ref: bytes) -> str:
    return binascii.hexlify(ref).decode("utf8")


# TODO: make A PR in the https://github.com/pinnaculum/py-multiformats-cid
# TODO: repo to make it a class method
def parse(source: str) -> Union[CIDv0, CIDv1]:
    cid = from_string(source)
    if cid.version == 0 and source[0] != "Q":
        raise ValueError("Version 0 CID string must not include multibase prefix")
    return cid  # type: ignore


def _encodeReference(ref: Union[str, Reference], codec: int) -> CIDv1:
    hash_bytes = hexToBytes(ref)
    return make_cid(codec, keccak(hash_bytes))  # type: ignore


def _decodeReference(ref: Union[CIDv0, CIDv1, str]) -> DecodeResult:
    if isinstance(ref, str):
        cid = parse(ref)

    reference = bytesTohex(cid.multihash)
    content_type = TYPE_MAPPING.get(cid.codec, "")  # type: ignore

    return DecodeResult(reference, content_type)


def encodeReference(
    ref: Union[str, Reference], type: ReferenceType
) -> Union[CIDv1, ReferenceError]:
    if type == ReferenceType.FEED:
        return _encodeReference(ref, SWARM_FEED_CODEC)
    elif type == ReferenceType.MANIFEST:
        return _encodeReference(ref, SWARM_MANIFEST_CODEC)
    return ReferenceError("Unknown reference type.")


def encodeFeedReference(ref: Union[str, Reference]) -> CIDv1:
    """
    Encode Swarm hex-encoded Reference into CID and sets Feed codec.
    @param ref
    """
    return _encodeReference(ref, SWARM_FEED_CODEC)


def encodeManifestReference(ref: Union[str, Reference]) -> CIDv1:
    """
    Encode Swarm hex-encoded Reference into CID and sets Manifest codec.
    @param ref
    """
    return _encodeReference(ref, SWARM_MANIFEST_CODEC)


def decodeFeedCid(cid: Union[CIDv0, CIDv1, str]) -> Union[Reference, str]:
    """
    Function to decode Feed CID (both from string or CID instance) into hex
    encoded Swarm reference.

    @param cid
    @throws Error if the decoded codec did not matched Swarm Feed codec
    """
    result = _decodeReference(cid)

    if result.type != ReferenceType.FEED:
        raise ValueError("CID did not have Swarm Feed codec!")

    return result.reference


def decodeManifestCid(cid: Union[CIDv0, CIDv1, str]) -> Union[Reference, str]:
    """
    Function to decode Manifest CID (both from string or CID instance) into
    hex encoded Swarm reference.

    @param cid
    @throws Error if the decoded codec did not matched Swarm Manifest codec
    """

    result = _decodeReference(cid)
    if result.type != ReferenceType.MANIFEST:
        raise ValueError("CID did not have Swarm Manifest codec!")

    return result.reference


def decodeCid(cid: Union[CIDv0, CIDv1, str]) -> DecodeResult:
    """
    * Decode CID or base encoded CID string into DecodeResult interface.
    * Does not throw exception if the codec was not Swarm related. In that
    case `type` is undefined.
    *
    * @see DecodeResult
    * @param cid
    """
    return _decodeReference(cid)
