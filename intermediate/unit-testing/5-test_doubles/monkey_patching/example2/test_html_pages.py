import io
from unittest.mock import mock_open
from unittest.mock import patch

from html_pages import HtmlPagesConverter

'''
patch "builtins.open" with mock_open
mock_open is a fake file
read_data is the contents of that file
'''
@patch("builtins.open", new_callable=mock_open,
       read_data="quote: ' ")
def test_convert_quotes(fake_file):
    with HtmlPagesConverter(filename="filename.txt") as converter:
        converted_text = converter.get_html_page(0)
        assert converted_text == "quote: &#x27;<br />"
