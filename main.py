from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List

class IObservable(ABC):

    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass

class Socket(IObservable):
    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict):
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._state)

    def connect(self):
        self.state = {'connect': True}

    def disconnect(self):
        self.state = {'connect': False}


