import typing as t
from cromlech.marshallers import Marshaller, PickleMarshaller
from http_session.meta import Store, SessionData
from pymemcache.client.base import Client


class MemcacheStore(Store):
    """Memcached based HTTP session.
    """
    def __init__(self,
                 memcache: Client,
                 delta: int,
                 prefix: str='session:',
                 marshaller: Marshaller = PickleMarshaller):
        self.delta = delta  # timedelta in seconds.
        self.memcache = memcache
        self.marshaller = marshaller
        self.prefix = prefix

    def get(self, sid: str) -> SessionData:
        key = self.prefix + sid
        data = self.memcache.get(key)
        if data is None:
            return self.new()
        if self.memcache.deserializer is None:
            return self.marshaller.loads(data)
        return data  # already readable

    def set(self, sid: str, session: SessionData) -> t.NoReturn:
        key = self.prefix + sid
        if self.memcache.serializer is None:
            data = self.marshaller.dumps(session)
        else:
            data = session  # will be marshalled
        self.memcache.set(key, data, expire=self.delta)

    def clear(self, sid: str) -> t.NoReturn:
        key = self.prefix + sid
        self.memcache.delete(key)

    delete = clear

    def touch(self, sid: str)  -> t.NoReturn:
        key = self.prefix + sid
        self.memcache.touch(key, expire=self.delta)
