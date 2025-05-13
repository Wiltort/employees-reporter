from . import reports
from .utils.cls_loader import get_subclasses
from typing import List
from .cli import CLIError


class ReportManager:
    """
    Класс, предназначенный для составления отчетов из файлов
    """
    report_class: type[reports.Report]
    files: List[str]

    def __init__(self, files: List[str], report_type: str):
        report_classes = get_subclasses(reports.Report)
        report_class = report_classes.get(report_type)
        if not report_class:
            raise CLIError("Неверный тип отчета")
        self.report_class = report_class()
        self.files = files
