from typing import Dict, NewType, Union

# Constants
KECCAK_256_CODEC = 0x1B
SWARM_NS_CODEC = 0xE4
SWARM_MANIFEST_CODEC = 0xFA
SWARM_FEED_CODEC = 0xFB
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
    def __init__(self, reference: Union[Reference, str], type: ReferenceType):
        self.reference = reference
        self.type = type

    def to_dict(self) -> Dict:
        return {"reference": self.reference, "type": self.type}
