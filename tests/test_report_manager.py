import pytest
from src.report_processing import ReportManager
from src.cli import CLIError


class TestReportManager:
    """Тесты для класса управления отчетами"""

    def test_valid_report_type(self, mocker):
        mock_report = mocker.Mock()
        mocker.patch(
            "src.report_processing.get_subclasses",
            return_value={"valid_report": mock_report},
        )

        manager = ReportManager(files=[], report_type="valid_report")
        assert manager.report == mock_report()

    def test_invalid_report_type(self, mocker):
        mocker.patch("src.report_processing.get_subclasses", return_value={})

        with pytest.raises(CLIError):
            ReportManager(files=[], report_type="invalid")
