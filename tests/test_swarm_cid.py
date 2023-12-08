import pytest

from swarm_cid import (
    ReferenceType,
    decode_cid,
    decode_feed_cid,
    decode_manifest_cid,
    encode_feed_reference,
    encode_reference,
)


def test_encode_and_decode_to_same_reference(
    test_swarm_reference, test_swarm_manifest_cid, SWARM_MANIFEST_CODEC
):
    cid = encode_reference(test_swarm_reference, ReferenceType.MANIFEST)

    assert cid.codec == SWARM_MANIFEST_CODEC
    assert cid.encode().decode() == test_swarm_manifest_cid

    assert decode_cid(cid).to_dict() == {
        "reference": test_swarm_reference,
        "type": ReferenceType.MANIFEST,
    }


def test_encode_and_decode_with_base32_string_to_same_reference(test_swarm_reference):
    cid = encode_reference(test_swarm_reference, ReferenceType.FEED)
    cid_string = str(cid)

    assert decode_cid(cid_string).to_dict() == {
        "reference": test_swarm_reference,
        "type": ReferenceType.FEED,
    }


def test_encode_manifest_and_decode_with_base32_string_to_same_reference(
    test_swarm_reference, test_swarm_manifest_cid, SWARM_MANIFEST_CODEC
):
    cid = encode_reference(test_swarm_reference, ReferenceType.MANIFEST)
    cid_string = str(cid)

    assert cid.codec == SWARM_MANIFEST_CODEC
    assert str(cid) == test_swarm_manifest_cid

    assert decode_cid(cid_string).to_dict() == {
        "reference": test_swarm_reference,
        "type": ReferenceType.MANIFEST,
    }
    assert decode_manifest_cid(cid_string) == test_swarm_reference

    with pytest.raises(ValueError):
        decode_feed_cid(cid_string)


def test_encode_feed_and_decode_with_base32_string_to_same_reference(
    test_swarm_reference, test_swarm_feed_cid, SWARM_FEED_CODEC
):
    cid = encode_feed_reference(test_swarm_reference)
    cid_string = str(cid)

    assert cid.codec == SWARM_FEED_CODEC
    assert cid.encode().decode() == test_swarm_feed_cid

    assert decode_cid(cid_string).to_dict() == {
        "reference": test_swarm_reference,
        "type": ReferenceType.FEED,
    }
    assert decode_feed_cid(cid_string) == test_swarm_reference
    with pytest.raises(ValueError):
        decode_manifest_cid(cid_string)


def test_decode_cid_with_incompatible_codec(cid_v1_with_dag_pb, cid_v1_with_dag_pb_reference):
    assert decode_cid(cid_v1_with_dag_pb).to_dict() == {
        "reference": cid_v1_with_dag_pb_reference,
        "type": None,
    }


def test_decode_cid_with_specific_codec(cid_v1_with_dag_pb):
    with pytest.raises(ValueError):
        decode_feed_cid(cid_v1_with_dag_pb)
    with pytest.raises(ValueError):
        decode_manifest_cid(cid_v1_with_dag_pb)
