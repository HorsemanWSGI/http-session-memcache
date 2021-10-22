import time
from http_session_memcache.store import MemcacheStore


def test_store(memcache_client):
    store = MemcacheStore(memcache_client, 300)
    store.set('test', {'someid': 42})
    assert store.get('test') == {'someid': 42}


def test_clear(memcache_client):
    store = MemcacheStore(memcache_client, 300)
    store.set('test', {'someid': 42})
    store.clear('test')
    assert store.get('test') == {}


def test_delete(memcache_client):
    store = MemcacheStore(memcache_client, 300)
    store.set('test', {'someid': 42})
    store.delete('test')
    assert store.get('test') == {}


def test_timeout(memcache_client):
    store = MemcacheStore(memcache_client, 1)
    store.set('test', {'someid': 42})
    time.sleep(1)
    assert store.get('test') == {}


def test_touch(memcache_client):
    store = MemcacheStore(memcache_client, 2)
    store.set('test', {'someid': 42})
    time.sleep(1)
    store.touch('test')
    time.sleep(1)
    assert store.get('test') == {'someid': 42}
    time.sleep(1)
    assert store.get('test') == {}
