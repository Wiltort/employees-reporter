from abc import ABC, abstractmethod


class Report(ABC):
    """Абстрактный отчет"""
    keyword: str

    @abstractmethod
    def get_summary(self):
        pass
