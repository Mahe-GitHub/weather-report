## Weather Reporting 
This project reports hottest day, Temperature and Region for weather report files. 

## Assumption
 - Python3 already installed on the system
 - PyCharm is installed
 - The following are the expected output from the csv files when the ScreenTemperature is high
   1. ObservationDate
   2. ScreenTemperature
   3. Region
 - Input files will be dropped in `input_src_files` folder
 - Output parquet will be generated in `output_parquet\<DATASET_NAME>`
 
## Setup
 - Create python virtual env and install packages using `pipenv install -d`
 - Navigate to File -> Settings -> Project -> Project Interrupter 
 - Choose the newly created venv to run the program 
 - Run pytest from `tests\`
 - Run program `main.py` from PyCharm
 
 - From the command line, navigate to the root of the project
 - Run `pipenv shell`
 - set PYTHONPATH=<root of the project>
 - navigate to `src\weather`
 - Run `python main.py`
 