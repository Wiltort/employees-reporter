from importlib.readers import FileReader
from typing import List
from src import reports
from src.cli import CLIError
from src.file_import import CSVReader
from src.utils.cls_loader import get_subclasses
from src.data_processing import DataSet
from src.views import print_table
import json


class ReportManager:
    """
    Класс, предназначенный для составления отчетов из файлов
    """

    report: type[reports.Report]
    files: List[str]

    def __init__(self, files: List[str], report_type: str):
        report_classes = get_subclasses(reports.Report)
        report_class = report_classes.get(report_type)
        if not report_class:
            raise CLIError("Неверный тип отчета")
        self.report = report_class()
        self.files = files

    def print_report(self, reader: FileReader = CSVReader()):
        data = DataSet()
        for file in self.files:
            if data.indexes:
                data.extend(reader.read_file(file=file).standardize())
            else:
                data = reader.read_file(file=file).standardize()
        report = self.report.get_summary(data)
        gr_index = self.report.conf.get("group_by_field_index")
        data = report.to_dict(
            order_by_ind=self.report.conf.get("order_by_field_index"),
            group_by_ind=gr_index,
        )
        grouped = gr_index is not None
        title = self.report.conf.get("title", "")
        print_table(data, title=title, grouped=grouped)
        with open("reports/data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
