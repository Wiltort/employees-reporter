import pytest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.cli import Parser, CLIError


class TestParser:
    """Тесты для класса парсера командной строки"""
    
    def test_valid_args(self):
        test_args = ["file1.csv", "--report", "summary"]
        with patch.object(sys, 'argv', ['main.py'] + test_args):
            parser = Parser()
            assert parser.files == ["file1.csv"]
            assert parser.report_type == "summary"

    def test_missing_report(self):
        test_args = ["file1.csv"]
        with patch.object(sys, 'argv', ['main.py'] + test_args), pytest.raises(CLIError):
            Parser()

    def test_extra_args(self):
        test_args = ["file1.csv", "--report", "summary", "extra"]
        with patch.object(sys, 'argv', ['main.py'] + test_args), pytest.raises(CLIError):
            Parser()

    def test_invalid_option(self):
        test_args = ["file1.csv", "--invalid", "value"]
        with patch.object(sys, 'argv', ['main.py'] + test_args), pytest.raises(CLIError):
            Parser()
