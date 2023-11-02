import unittest

import pytest

from tests.log_analyzer import extract_errors


######## Answer the point 1B ########

@pytest.mark.test
class TestExtractErrors(unittest.TestCase):

    def test_basic_without_error(self):
        log_data = "This is a log ok"
        result = extract_errors(log_data)
        self.assertFalse(any("ERROR" in error.upper() for error in result))

    def test_basic_errors_uppercase(self):
        log_data = "This is a log with an ERROR in the same line"
        result = extract_errors(log_data)
        self.assertTrue(any("ERROR" in error.upper() for error in result))

    def test_case_errors_lowercase(self):
        log_data = "This is a log with an error in lowercase in the same line"
        result = extract_errors(log_data)
        self.assertTrue(any("ERROR" in error.upper() for error in result))

    def test_multiline_errors(self):
        log_data = "This is a log with an ERROR\nthat spans\nmultiple lines"
        result = extract_errors(log_data)
        self.assertEqual(result, ["This is a log with an ERROR that spans multiple lines"])
        self.assertTrue(any("ERROR" in error.upper() for error in result))

######## Test cases are created to make the scope more robust ########

    def test_case_other_word(self):
        log_data = "This is a log with other WORD"
        result = extract_errors(log_data, "WORD")
        self.assertEqual(result, ["This is a log with other WORD"])
        self.assertTrue(any("WORD" in error.upper() for error in result))

    def test_multiline_other_word(self):
        log_data = "This is a log with other WORD\nthat spans\nmultiple lines"
        result = extract_errors(log_data, "WORD")
        self.assertEqual(result, ["This is a log with other WORD that spans multiple lines"])
        self.assertTrue(any("WORD" in error.upper() for error in result))
