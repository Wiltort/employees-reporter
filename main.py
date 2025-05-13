from src.cli import Parser
from src.data_processing import ReportManager


arg_parser = Parser()
report_manager = ReportManager(
    files=arg_parser.files,
    report_type=arg_parser.report_type
)
#report_manager.print_report()