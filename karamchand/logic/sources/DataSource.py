from abc import abstractmethod, ABCMeta

class DataSource(metaclass=ABCMeta):

    @abstractmethod
    def get_source_name(self):
        pass

    @abstractmethod
    def get_source_data(self):
        pass

