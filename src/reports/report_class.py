from abc import ABC, abstractmethod
from src.data_processing import DataSet, ReportDataSet


class Report(ABC):
    """Абстрактный отчет"""
    keyword: str
    conf: dict

    @abstractmethod
    def get_summary(self, data: DataSet) -> ReportDataSet:
        pass
