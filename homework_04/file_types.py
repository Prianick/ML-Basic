from abc import abstractmethod
from typing import Self
from storage_types import OtusAbstractFileStorage
from pathlib import Path


class AbstractFileType:
    def __init__(self, name: str = None, path: str = None, content: str = None, storage: object = None):
        self._name = None
        self._path = None
        self._content = None
        self._storage = None

    @property
    def content(self) -> Self:
        return self._content
    
    @content.setter
    def content(self, value: str) -> Self:
        self._content = value
        return self
    
    @property
    def storage(self) -> OtusAbstractFileStorage:
        return self._storage
    
    @storage.setter
    def storage(self, value: object) -> Self:
        if not isinstance(value, OtusAbstractFileStorage):
            raise TypeError("Storage must be an instance of OtusAbstractFileStorage.")
        self._storage = value
        return self

    def save(self) -> Self:
        """Save"""
        if self.storage is None:
            raise Exception("Storage is not set.")
        if self.name is None or self.path is None:
            raise Exception("File name or path is not set.")
        self.storage.save(Path(self.path) / self.name, self.content)
        return self

    def read(self) -> str:
        if self.storage is None:
            raise Exception("Storage is not set.")
        if self.path is None:
            raise Exception("File path is not set.")
        return self.storage.load(self.path)

    def delete(self) -> bool:
        """Delete the file."""
        pass


class Image(AbstractFileType):
    pass

class Text(AbstractFileType):
    pass

class Video(AbstractFileType):
    pass

class Audio(AbstractFileType):
    pass
