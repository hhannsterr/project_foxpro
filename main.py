import os
import subprocess
import warnings

from dotenv import dotenv_values
from src.data_population import process
from src.data_population import load_excel, clean_path
from src.general import get_date, save_date


def main():

    config = dotenv_values('.env')

    year, month, day = get_date()
    subprocess.call(['bash', './fetch_data.sh', year, month, day])

    path_to_data = 'data'
    process_col = {
        'tap': ['F', 'G'],
        'mould': ['M', 'N'],
        'melt': ['Q', 'R'],
        'grind': ['U', 'V'],
        'sht': ['Y', 'Z'],
        'galv': ['AC', 'AD'],
        'dmg': ['AG', 'AH'],
        'loc': ['I', 'J']
    }

    excel_path = config['EXCEL_PATH']
    sheet_name = 'data of Foxpro'

    print('Processing excel file...')
    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
    workbook, sheet = load_excel(excel_path, sheet_name) # type: ignore

    process_paths = os.listdir(path_to_data)
    for process_path in process_paths:
        temp = process(sheet)
        temp.fetch_summary(path_to_data, process_path)

        columns = process_col[clean_path(process_path)]
        temp.populate_data(columns)

    workbook.save('test.xlsx') # directory to be changed
    # save_date()


if __name__ == '__main__':
    main()
