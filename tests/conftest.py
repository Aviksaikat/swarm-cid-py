import pytest


@pytest.fixture
def test_reference():
    return "4c949794d617238d928ef1dc544ee07cbdcfd6b946e5202fa06c4d32088d7e69"


@pytest.fixture
def test_manifest_cid():
    # return "bah5acgzazjrvpieogf6rl3cwb7xtjzgel6hrt4a4g4vkody5u4v7u7y2im4a"
    return "bah5acgzaukog5d75a3uftpeeikfy35gnw2mmvulh4ktwebzfbsbqxskto6ha"


@pytest.fixture
def test_feed_cid():
    return "bah5qcgzazjrvpieogf6rl3cwb7xtjzgel6hrt4a4g4vkody5u4v7u7y2im4a"


@pytest.fixture
def cid_v1_with_dag_pb():
    return "bafybeiekkklkqtypmqav6ytqjbdqucxfwuk5cgige4245d2qhkccuyfnly"


@pytest.fixture
def cid_v1_with_dag_pb_reference():
    return "8a5296a84f0f64015f627048470a0ae5b515d119062735ce8f503a842a60ad5e"


@pytest.fixture
def SWARM_FEED_CODEC():
    return "swarm-feed"


@pytest.fixture
def SWARM_MANIFEST_CODEC():
    return "swarm-manifest"
