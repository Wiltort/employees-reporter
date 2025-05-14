from typing import List
from config import Config


class DataError(Exception):
    """Класс ошибок данных"""
    pass


class DataSet:
    def __init__(self):
        self._index_counter = self._next_index()
        self.indexes = []
        self.records = {}

    def set_fields(self, fields: List[str]):
        self.records = {field: [] for field in fields}

    def to_list(self):
        records = []
        for index in self.indexes:
           records.append([value[index] for value in self.records.values()])
        return records
    
    def _next_index(self):
        ind = 0
        while True:
            yield ind
            ind += 1

    def to_dict(self, order_by_ind: int | None = None, group_by_ind: int | None = None):
        data = {}
        ds = self
        if order_by_ind is not None:
            ds = ds.order_by(order_by_ind)
        if group_by_ind is not None:
            gr_field = list(ds.records.keys())[group_by_ind]
            for i in ds.indexes:
                record = {field: value[i] for field, value in ds.records.items()}
                value = record[gr_field]
                data[value] = data.get(value, [])
                record[gr_field] = '------'
                data[value].append(record)
            return data
        for i in ds.indexes:
            data[i] = {field: value[i] for field, value in ds.records.items()}
        return data

    def add_record(self, record: List[str]):
        if len(record) != len(self.records):
            raise DataError('Неверное количество полей')
        self.indexes.append(next(self._index_counter))
        for number, field in enumerate(self.records.keys()):
            value = record[number]
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass
            self.records[field].append(value)

    def standardize(self) -> 'DataSet':
        new_ds = DataSet()
        standart_fields = Config.FIELD_NAME_DICT.keys()
        new_ds.set_fields(standart_fields)
        if self.indexes:
            for index in self.indexes:
                new_record = []
                for field in standart_fields:
                    options = Config.FIELD_NAME_DICT[field]
                    for option in options:
                        value = self.records.get(option)
                        if value:
                            value = value[index]
                            break
                    new_record.append(value)
                new_ds.add_record(new_record)    
        return new_ds
    
    def extend(self, other: 'DataSet'):
        data_dict = other.to_dict()
        for ind in other.indexes:
            self.add_record(list(data_dict[ind].values()))
    
    def order_by(self, field_index: int, desc: bool = False):
        if field_index > len(self.records) + 1:
            raise ValueError
        records = sorted(self.to_list(), key=lambda x: x[field_index], reverse=desc)
        new_ds = type(self)()
        new_ds.set_fields(list(self.records.keys()))
        for record in records:
            new_ds.add_record(record)
        return new_ds
    

class ReportDataSet(DataSet):

    def standardize(self, fields: dict):
        new_report = ReportDataSet()
        fields = fields['existing_fields'] + fields['calculated_fields']
        new_report.set_fields(fields)
        data = self.to_dict()
        if self.indexes:
            for index in self.indexes:
                new_report.add_record(list(data[index].values()))
        return new_report






