import sys
from typing import List


class CLIError(Exception):
    """Неверные параметры командной строки"""

    pass


class Parser:
    files: List[str] = []
    report_type: str = ""

    def __init__(self):
        args = sys.argv[:0:-1]
        while args:
            arg = args.pop()
            if not arg.startswith("-"):
                self.files.append(arg)
            else:
                if arg == "--report":
                    try:
                        self.report_type = args.pop()
                    except IndexError:
                        raise CLIError("Не указан тип отчета")
                    if args:
                        raise CLIError("Лишние аргументы!")
                else:
                    raise CLIError(f"Неверный аргумент: '{arg}'")
        if not self.files:
            raise CLIError("Не указан ни один файл")
        if not self.report_type:
            raise CLIError("Не указан тип отчета")
