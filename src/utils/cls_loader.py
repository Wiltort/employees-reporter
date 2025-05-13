from inspect import isabstract
from typing import Dict
from src.reports.report_class import Report


def get_subclasses(cls: type[Report]) -> Dict[str, type]:
    """
    Возвращает словарь, содержащий все неабстрактные подклассы.
    Args:
        cls: Класс, который является либо корневым Report, либо потомком.
    Returns:
        Словарь классов.
    """
    subclasses = {}

    for subclass in cls.__subclasses__():
        if not isabstract(subclass):
            subclasses[subclass.keyword] = subclass
        subclasses.update(get_subclasses(subclass))
    return subclasses
