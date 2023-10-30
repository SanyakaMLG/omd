import json
from unittest.mock import patch, MagicMock

import pytest

from what_is_year_now import what_is_year_now


def test_ymd():
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_resp = MagicMock()
        mock_resp_json = {'currentDateTime': '2023-10-30'}
        mock_resp.read.return_value = json.dumps(mock_resp_json).encode()

        mock_urlopen.return_value.__enter__.return_value = mock_resp

        assert what_is_year_now() == 2023


def test_dmy():
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_resp = MagicMock()
        mock_resp_json = {'currentDateTime': '30.10.2023'}
        mock_resp.read.return_value = json.dumps(mock_resp_json).encode()

        mock_urlopen.return_value.__enter__.return_value = mock_resp

        assert what_is_year_now() == 2023


def test_raise():
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_resp = MagicMock()
        mock_resp_json = {'currentDateTime': '1234567890'}
        mock_resp.read.return_value = json.dumps(mock_resp_json).encode()

        mock_urlopen.return_value.__enter__.return_value = mock_resp

        with pytest.raises(ValueError):
            what_is_year_now()
