import typing as t
from http_session.meta import Store, SessionData
from pymemcache.client.base import Client


class MemcacheStore(Store):
    """Memcached based HTTP session.
    """
    def __init__(self,
                 memcache: Client,
                 delta: int,
                 prefix: str='session:'):
        self.delta = delta  # timedelta in seconds.
        self.memcache = memcache
        self.prefix = prefix

    def get(self, sid: str) -> SessionData:
        key = self.prefix + sid
        data = self.memcache.get(key)
        if data is None:
            return self.new()
        return data

    def set(self, sid: str, session: SessionData) -> t.NoReturn:
        key = self.prefix + sid
        self.memcache.set(key, session, expire=self.delta)

    def clear(self, sid: str) -> t.NoReturn:
        key = self.prefix + sid
        self.memcache.delete(key)

    delete = clear

    def touch(self, sid: str)  -> t.NoReturn:
        key = self.prefix + sid
        self.memcache.touch(key, expire=self.delta)
