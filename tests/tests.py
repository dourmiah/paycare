from unittest.mock import patch, MagicMock
from etl import extract_data, transform_data, load_data
import pandas as pd
import os

input_file = '/home/app/data/input_data_test.csv'
output_file = '/home/app/data/output_data_test.csv'


def test_extract_data():
    data_return = extract_data(input_file)
    data_expected = pd.DataFrame(data=[[1, "John Doe", 28, "New York", 70000], [2,"Charlie Brown", None,"Houston",65000]], 
                                 columns=["id", "name", "age", "city", "salary"])
    pd.testing.assert_frame_equal(data_return, data_expected)


def test_transform_data():
    data_input = pd.DataFrame(data={"id": [1,2], "name": ["John Doe", None], "salary": [70000, None]})
    data_return = transform_data(data_input)
    data_expected = pd.DataFrame(data={"id": [1], "name": ["John Doe"], "salary": [70000.0], "tax": [7000.0], "net_salary": [63000.0]}, 
                                 columns=["id", "name", "salary", "tax", "net_salary"])
    pd.testing.assert_frame_equal(data_return, data_expected)

@patch('pandas.DataFrame.to_csv')
def test_load_data(mock_to_csv):
    data_input = pd.DataFrame(data={"id": [1,2], "name": ["John Doe", None], "salary": [70000, None]})
    load_data(data_input, output_file)
    mock_to_csv.assert_called_once()
    args, kwargs = mock_to_csv.call_args
    assert kwargs['index'] == False 
    assert args[0] == output_file # Check file path