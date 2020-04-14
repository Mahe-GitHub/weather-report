import glob
import shutil

from src.weather.weather_report import WeatherReport

DATASET_NAME = 'weather'
OUTPUT_PARQUET_PATH = '..\\..\\output_parquet\\'


def main():
    shutil.rmtree(f'{OUTPUT_PARQUET_PATH}\\{DATASET_NAME}', ignore_errors=True)
    weather_report = WeatherReport()

    for src_file in glob.glob('..\\..\\input_src_files\\weather.*.csv'):
        df = weather_report.read_csv(src_file)
        weather_report.write_parquet(df, DATASET_NAME, OUTPUT_PARQUET_PATH)

    table = weather_report.read_data(DATASET_NAME, OUTPUT_PARQUET_PATH)
    df = table.to_pandas()
    result_df = df.loc[df['ScreenTemperature'].idxmax()]
    result = result_df[['ObservationDate', 'ScreenTemperature', 'Region']].values
    return result


if __name__ == "__main__":
    output = main()
    print(output)
