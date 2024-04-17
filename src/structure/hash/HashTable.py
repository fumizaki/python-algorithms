from typing import Any
import hashlib

class HashTable:

    def __init__(self, size: int = 10):

        if size < 1:
            raise ValueError("ハッシュテーブルのサイズは1以上にしてください")
        self.size = size
        self.table = [[] for _ in range(size)]


    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size


    def add(self, key: str, value: Any, priority: bool = True) -> None:
        index = self._hash(key)
        for record in self.table[index]:
            if record[0] == key and priority:
                # 後優先で上書きする
                record[1] = value
                break
            elif record[0] == key and not priority:
                # 先優先で上書きしない
                break
        else:
            self.table[index].append([key, value])

    def get(self, key: str) -> Any:
        index = self._hash(key)
        for record in self.table[index]:
            if record[0] == key:
                return record[1]


    def delete(self, key: str) -> None:
        index = self._hash(key)
        for record in self.table[index]:
            if record[0] == key:
                self.table[index].remove(record)
