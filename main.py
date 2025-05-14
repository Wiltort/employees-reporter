import sys
from src.cli import Parser, CLIError
from src.report_processing import ReportManager


def main():
    try:
        arg_parser = Parser()
        report_manager = ReportManager(
            files=arg_parser.files, report_type=arg_parser.report_type
        )
        report_manager.print_report()
    except CLIError as e:
        print(f"Ошибка: {e}")
        return 1
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
