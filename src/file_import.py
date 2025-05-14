from abc import ABC, abstractmethod
from typing import List
from src.data_processing import DataSet, DataError


class FileError(Exception):
    pass

class FileReader(ABC):
    """Класс чтения файлов"""
    type: str

    @abstractmethod
    def read_file(self, file: str, **kwargs):
        pass

    def file_is_valid(self, file: str):
        return "." in file and file.rsplit(".", 1)[1].lower() == self.type

class CSVReader(FileReader):
    type = 'csv'

    def read_file(self, file: str, sep: str = ',') -> DataSet:
        if not self.file_is_valid(file):
            raise FileError('Неверный формат файла')
        data = DataSet()
        with open(file, 'r') as f: 
            data.set_fields(f.readline().strip().split(sep))
            for line in f.readlines():
                data.add_record(line.strip().split(sep))
        return data