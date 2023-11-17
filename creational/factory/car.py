from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @staticmethod
    def get_subclasses():
        return Car.__subclasses__()

