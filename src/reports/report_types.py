from .report_class import Report


class PayoutReport(Report):
    keyword = 'payout'

    def get_summary(self):
        return "sss"
