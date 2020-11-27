class HashTableInterface:

    def put_all(self, **kwargs):
        raise NotImplementedError("Method not implemented")

    def put(self, key, value):
        raise NotImplementedError("Method not implemented")

    def remove(self, key, value):
        raise NotImplementedError("Method not implemented")

    def clear(self):
        raise NotImplementedError("Method not implemented")

    def contains(self, key):
        raise NotImplementedError("Method not implemented")

    def __repr__(self):
        raise NotImplementedError("Method not implemented")

    def __hash__(self):
        raise NotImplementedError("Method not implemented")

    def __eq__(self, other):
        raise NotImplementedError("Method not implemented")

    def __contains__(self, key):
        raise NotImplementedError("Method not implemented")
