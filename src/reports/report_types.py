from .report_class import Report
from src.data_processing import DataSet, ReportDataSet
from config import Config


class PayoutReport(Report):
    keyword = 'payout'
    conf = Config.PAYOUT_REPORT_FIELDS


    def get_summary(self, data: DataSet) -> ReportDataSet:
        fields=Config.PAYOUT_REPORT_FIELDS
        report = ReportDataSet()
        report = report.standardize(fields)
        for record in data.to_dict().values():
            report_record = []
            for field in fields['existing_fields']:
                report_record.append(record[field])
            report_record.append(f"$ {record['rate'] * record['hours']}")
            report.add_record(report_record)
        return report




