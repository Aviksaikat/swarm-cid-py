import pytest

from swarm_cid import decode_cid, decode_feed_cid, decode_manifest_cid, encode_reference

test_reference = "ca6357a08e317d15ec560fef34e4c45f8f19f01c372aa70f1da72bfa7f1a4338"
test_manifest_cid = "bah5acgzazjrvpieogf6rl3cwb7xtjzgel6hrt4a4g4vkody5u4v7u7y2im4a"
test_feed_cid = "bah5qcgzazjrvpieogf6rl3cwb7xtjzgel6hrt4a4g4vkody5u4v7u7y2im4a"

cid_v1_with_dag_pb = "bafybeiekkklkqtypmqav6ytqjbdqucxfwuk5cgige4245d2qhkccuyfnly"
cid_v1_with_dag_pb_reference = "8a5296a84f0f64015f627048470a0ae5b515d119062735ce8f503a842a60ad5e"


def test_encode_and_decode_to_same_reference():
    cid = encode_reference(test_reference, ReferenceType.MANIFEST)

    assert cid.code == SWARM_MANIFEST_CODEC
    assert str(cid) == test_manifest_cid

    assert decode_cid(cid) == {"reference": test_reference, "type": ReferenceType.MANIFEST}


def test_encode_and_decode_with_base32_string_to_same_reference():
    cid = encode_reference(test_reference, ReferenceType.FEED)
    cid_string = str(cid)

    assert decode_cid(cid_string) == {"reference": test_reference, "type": ReferenceType.FEED}


def test_encode_manifest_and_decode_with_base32_string_to_same_reference():
    cid = encode_manifest_reference(test_reference)
    cid_string = str(cid)

    assert cid.code == SWARM_MANIFEST_CODEC
    assert str(cid) == test_manifest_cid

    assert decode_cid(cid_string) == {"reference": test_reference, "type": ReferenceType.MANIFEST}
    assert decode_manifest_cid(cid_string) == test_reference
    with pytest.raises(ValueError):
        decode_feed_cid(cid_string)


def test_encode_feed_and_decode_with_base32_string_to_same_reference():
    cid = encode_feed_reference(test_reference)
    cid_string = str(cid)

    assert cid.code == SWARM_FEED_CODEC
    assert str(cid) == test_feed_cid

    assert decode_cid(cid_string) == {"reference": test_reference, "type": ReferenceType.FEED}
    assert decode_feed_cid(cid_string) == test_reference
    with pytest.raises(ValueError):
        decode_manifest_cid(cid_string)


def test_decode_cid_with_incompatible_codec():
    assert decode_cid(cid_v1_with_dag_pb) == {
        "reference": cid_v1_with_dag_pb_reference,
        "type": None,
    }


def test_decode_cid_with_specific_codec():
    with pytest.raises(ValueError):
        decode_feed_cid(cid_v1_with_dag_pb)
    with pytest.raises(ValueError):
        decode_manifest_cid(cid_v1_with_dag_pb)
