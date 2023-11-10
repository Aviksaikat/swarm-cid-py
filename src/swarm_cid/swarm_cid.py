import binascii
from typing import Dict, Optional, Union

from multiformats import multihash  # type: ignore
from multiformats_cid import CIDv0, CIDv1, from_string  # type: ignore

from .Exceptions import ReferenceError
from .types import DecodeResult, Reference, ReferenceType

# https://github.com/multiformats/multicodec/blob/master/table.csv

# constants values on hex format which evaluates to ints
KECCAK_256_CODEC = "keccak-256"
SWARM_NS_CODEC = "swarm-ns"
SWARM_MANIFEST_CODEC = "swarm-manifest"
SWARM_FEED_CODEC = "swarm-feed"
REFERENCE_HEX_LENGTH = 64

TYPE_MAPPING: Dict[str, str] = {
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


def _encodeReference(ref: Union[str, Reference], codec: str, version: Optional[int] = 1) -> CIDv1:
    """Encode Swarm hex-encoded Reference into CID that has appropriate codec
    set based on `type` parameter.

    Args:
        ref: Hex encoded Reference
        codec: Codec to use

    Returns:
        CID
    """
    hash_bytes = hexToBytes(ref)

    _hash = multihash.digest(hash_bytes, KECCAK_256_CODEC).hex()
    new_hash = hexToBytes(_hash[:4] + ref)

    return CIDv1(codec, new_hash)


def _decodeReference(cid: Union[CIDv0, CIDv1, str]) -> DecodeResult:
    if isinstance(cid, str):
        cid = parse(cid)

    # remove the hashtype + lengh i.e. first 4 bytes
    reference = bytesTohex(cid.multihash)[4:]
    content_type = TYPE_MAPPING.get(cid.codec, None)  # type: ignore

    return DecodeResult(reference, content_type)  # type: ignore


def encodeReference(
    ref: Union[str, Reference], type: Optional[ReferenceType], version: Optional[int] = 1
) -> Union[CIDv1, ReferenceError]:
    if type:
        if type == ReferenceType.FEED:
            return _encodeReference(ref, SWARM_FEED_CODEC, version)
        elif type == ReferenceType.MANIFEST:
            return _encodeReference(ref, SWARM_MANIFEST_CODEC, version)
    else:
        if version:
            return _encodeReference(ref=ref, version=version)  # type: ignore
    return ReferenceError("Unknown reference type.")


def encodeFeedReference(ref: Union[str, Reference]) -> CIDv1:
    """
    Encode Swarm hex-encoded Reference into CID and sets Feed codec.
    @param ref
    """
    return _encodeReference(ref=ref, codec=SWARM_FEED_CODEC)  # type: ignore


def encodeManifestReference(ref: Union[str, Reference]) -> CIDv1:
    """
    Encode Swarm hex-encoded Reference into CID and sets Manifest codec.
    @param ref
    """
    return _encodeReference(ref=ref, codec=SWARM_MANIFEST_CODEC)  # type: ignore


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
