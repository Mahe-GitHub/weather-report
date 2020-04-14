import glob
import shutil

import pandas as pd
from pandas.testing import assert_frame_equal
from pytest import mark

from src.weather.weather_report import WeatherReport

test_read_csv_data = [('test.csv', pd.DataFrame(data=[[0, 0, 0, 0], [1, 2, 3, 4]], columns=['A', 'B', 'C', 'D']))]
test_parquet_data = [
    (pd.DataFrame(data=[[0, 0, 0, 0], [1, 2, 3, 4]], columns=['A', 'B', 'C', 'D']), "test_dataset")]


class TestWeatherReport:
    @mark.parametrize("input_file, expected_df", test_read_csv_data)
    def test_read_csv(self, input_file, expected_df):
        df = WeatherReport.read_csv(input_file)
        assert_frame_equal(df, expected_df)

    @mark.parametrize("df, dataset_name", test_parquet_data)
    def test_write_parquet(self, df, dataset_name):
        WeatherReport.write_parquet(df, dataset_name)
        assert len(glob.glob(f'{dataset_name}\\*.parquet')) > 0
        shutil.rmtree(f'{dataset_name}\\', ignore_errors=True)

    @mark.parametrize("df, dataset_name", test_parquet_data)
    def test_read_data(self, df, dataset_name):
        WeatherReport.write_parquet(df, dataset_name)
        table = WeatherReport.read_data(dataset_name)
        output_df = table.to_pandas()
        assert_frame_equal(df, output_df)
        shutil.rmtree(f'{dataset_name}\\', ignore_errors=True)
