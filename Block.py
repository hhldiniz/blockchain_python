import datetime
import hashlib
import json


class Block:
    def __init__(self, previous_hash):
        self.__previous_hash = previous_hash
        self.__data = {}
        self.__hash = hashlib.sha3_256(
            f'{json.dumps(self.get_data())}{self.get_previous_hash()}{datetime.datetime.now()}'.encode("utf-8"))

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def get_previous_hash(self):
        return self.__previous_hash

    def get_hash(self):
        return self.__hash
