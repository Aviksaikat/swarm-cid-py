from typing import Dict, NewType, Union

# Constants
KECCAK_256_CODEC = "0x1b"
SWARM_NS_CODEC = "swarm-ns"
SWARM_MANIFEST_CODEC = "swarm-manifest"
SWARM_FEED_CODEC = "swarm-feed"
REFERENCE_HEX_LENGTH = 64

# Define a type alias for Reference
Reference = NewType("Reference", str)


class ReferenceType:
    FEED = "feed"
    MANIFEST = "manifest"


CODEC_TYPE_MAPPING = {
    SWARM_FEED_CODEC: ReferenceType.FEED,
    SWARM_MANIFEST_CODEC: ReferenceType.MANIFEST,
}


class DecodeResult:
    def __init__(self, reference: Union[Reference, str], type: Union[ReferenceType, str]):
        self.reference = reference
        self.type = type

    def to_dict(self) -> Dict:
        return {"reference": self.reference, "type": self.type}
