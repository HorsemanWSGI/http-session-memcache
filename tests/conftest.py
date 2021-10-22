import pytest
from pymemcache.client.base import Client
from pymemcache import serde


@pytest.fixture(scope='session')
def memcache_client():
     return Client(('127.0.0.1', 11211), serde=serde.pickle_serde)
