from abc import ABC, abstractmethod
from . import WebmentionCollection


class SerpAdaptorBase(ABC):

    @abstractmethod
    def search(self) -> WebmentionCollection:
        return WebmentionCollection()
