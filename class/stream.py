from abc import ABC, abstractmethod


class InValidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InValidOperationError("the Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InValidOperationError('the Stream is already closed')
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('reading data from a file')


class NetworkStream(Stream):
    def read(self):
        print('Reading data from a network')


class MemoryClass(Stream):
    def read(self):
        print('reading data from MemoryClass')


stream = MemoryClass()
