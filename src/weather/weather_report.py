import logging
import os

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WeatherReport:

    @staticmethod
    def read_csv(src_file: str, delimiter: str = ','):
        """
        Reads a csv and returns pandas dataframe
        :param src_file:
        :param delimiter:
        :return: dataframe
        """
        logger.info(f"Reading {src_file} file")
        df = pd.read_csv(src_file, delimiter=delimiter)
        return df

    @staticmethod
    def write_parquet(df: pd.DataFrame, dataset_name: str, path: str = '.'):
        """
        Writes into a parquet file for a given dataframe with dataset
        :param df:
        :param dataset_name:
        :param path:
        :return: None
        """
        logger.info(f"Writing into parquet file for {dataset_name} dataset")
        root_path = os.path.join(path, dataset_name)
        table = pa.Table.from_pandas(df)
        pq.write_to_dataset(table, root_path=root_path)

    @staticmethod
    def read_data(dataset_name: str, path: str = '.'):
        """
        Reads data from parquet files for a given dataset and return pyarrow parquet table
        :param dataset_name:
        :param path:
        :return:
        """
        logger.info("Reading data from parquet files")
        root_path = os.path.join(path, dataset_name)
        table = pq.read_table(root_path)
        return table
