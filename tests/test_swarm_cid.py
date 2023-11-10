import pytest

from swarm_cid import (
    ReferenceType,
    decodeCid,
    decodeFeedCid,
    decodeManifestCid,
    encodeFeedReference,
    encodeReference,
)


def test_encode_and_decode_to_same_reference(
    test_swarm_reference, test_swarm_manifest_cid, SWARM_MANIFEST_CODEC
):
    cid = encodeReference(test_swarm_reference, ReferenceType.MANIFEST, 1)

    assert cid.codec == SWARM_MANIFEST_CODEC
    assert cid.encode().decode() == test_swarm_manifest_cid

    assert decodeCid(cid).to_dict() == {
        "reference": test_swarm_reference,
        "type": ReferenceType.MANIFEST,
    }


def test_encode_and_decode_with_base32_string_to_same_reference(test_reference):
    cid = encodeReference(test_reference, ReferenceType.FEED)
    cid_string = str(cid)

    assert decodeCid(cid_string) == {"reference": test_reference, "type": ReferenceType.FEED}


def test_encode_manifest_and_decode_with_base32_string_to_same_reference(
    test_reference, test_manifest_cid, SWARM_MANIFEST_CODEC
):
    cid = test_reference
    cid_string = str(cid)

    assert cid.code == SWARM_MANIFEST_CODEC
    assert str(cid) == test_manifest_cid

    assert decodeCid(cid_string) == {"reference": test_reference, "type": ReferenceType.MANIFEST}
    assert decodeManifestCid(cid_string) == test_reference
    with pytest.raises(ValueError):
        decodeFeedCid(cid_string)


def test_encode_feed_and_decode_with_base32_string_to_same_reference(
    test_reference, test_feed_cid, SWARM_FEED_CODEC
):
    cid = encodeFeedReference(test_reference)
    cid_string = str(cid)

    assert cid.code == SWARM_FEED_CODEC
    assert str(cid) == test_feed_cid

    assert decodeCid(cid_string) == {"reference": test_reference, "type": ReferenceType.FEED}
    assert decodeFeedCid(cid_string) == test_reference
    with pytest.raises(ValueError):
        decodeManifestCid(cid_string)


def test_decodeCid_with_incompatible_codec(cid_v1_with_dag_pb, cid_v1_with_dag_pb_reference):
    assert decodeCid(cid_v1_with_dag_pb) == {
        "reference": cid_v1_with_dag_pb_reference,
        "type": None,
    }


def test_decodeCid_with_specific_codec(cid_v1_with_dag_pb):
    with pytest.raises(ValueError):
        decodeFeedCid(cid_v1_with_dag_pb)
    with pytest.raises(ValueError):
        decodeManifestCid(cid_v1_with_dag_pb)
