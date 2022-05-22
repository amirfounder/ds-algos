"""Started off too big. Memory issues with this approach.
"""

from enum import Enum


def sip_hash(obj):
    return hash(obj)


class HashingStrategy(Enum):
    SipHash = hash


class CollisionResolutionStrategy(Enum):
    Chaining = 0
    LinearProbing = 1
    DoubleHashing = 2
    OpenAddressing = 3


class HashTable:
    def __init__(self):
        self.table = []
        self._hashing_strategy = HashingStrategy.SipHash
        self._collision_resolution_strategy = CollisionResolutionStrategy.Chaining

    def __extend_table(self, hash_value):
        self.table += ([0] * (hash_value + 1 - len(self.table)))

    def set_hashing_strategy(self, strategy: HashingStrategy):
        self._hashing_strategy = strategy

    def set_collision_resolution_strategy(self, strategy: CollisionResolutionStrategy):
        self._collision_resolution_strategy = strategy

    def set_item(self, key, value):
        hash_value = abs(self._hashing_strategy.value(key))

        if hash_value >= len(self.table):
            self.__extend_table(hash_value)

        if self.table[hash_value] is 0:
            if self._collision_resolution_strategy == CollisionResolutionStrategy.Chaining:
                self.table[hash_value] = [value]
            else:
                self.table[hash_value] = value
        else:
            if self._collision_resolution_strategy == CollisionResolutionStrategy.Chaining:
                self.table[hash_value].append(value)

    def get_item(self, key):
        hash_value = self._hashing_strategy.value(key)

        if hash_value >= len(self.table):
            raise KeyError('No key in hashtable')

        value = self.table[hash_value]

        if value is 0:
            raise KeyError('No key in hashtable')

        return value


if __name__ == '__main__':
    print('hello world')
    table = HashTable()
    table.set_item('hello', 'goodbye')
    table.get_item('hello')

