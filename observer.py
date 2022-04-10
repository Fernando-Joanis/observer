from __future__ import annotations
from abc import ABC, abstractmethod
from main import Socket, IObservable
class IObserver(ABC):

    @abstractmethod
    def update(self) -> None:
        pass

class Upload(IObserver):
    def __init__(self, nome, observable: IObservable):
        self.nome = nome
        self.observable = observable

    def update(self, state):
        if state['connect'] == True:
            print('Iniciar upload')
        elif  state['connect'] == False:
            print('Parar Upload')

if __name__ == '__main__':
    sio = Socket()
    upload = Upload('Upload', sio)

    sio.add_observer(upload)

    sio.connect()
    sio.connect()
    sio.disconnect()
