#this program creates all datasets used for testing by calling the FRED api, as well as cleans and processes the datasets

import os
import pandas as pd
from fredapi import Fred
from functools import reduce


class create_dataset():
    def __init__(self):
        pass

    def get_all_data(self):
        # Get the directory where this script is running
        script_dir = os.path.dirname(__file__)

        # Get the generated datasets directory
        generated_datasets_dir = os.path.join(script_dir, '../../generated_datasets/')

        pulled_data_dir = os.path.join(generated_datasets_dir, 'pulled_data/')
        clean_data_dir = os.path.join(generated_datasets_dir, 'clean_data/')
        processed_data_dir = os.path.join(generated_datasets_dir, 'processed_data/')

        fred = Fred(api_key='2abb3d9b3ed2560c6b1f9fa93932a790')

        # pulling data from FRED using their api
        rec_data = fred.get_series_latest_release('USREC')
        rec_data = pd.DataFrame({'Date': rec_data.index, 'Recession': rec_data.values})
        rec_data = rec_data.set_index('Date')

        employ_data = fred.get_series_latest_release('UNRATE')
        employ_data = pd.DataFrame({'Date': employ_data.index, 'Unemployment Rate': employ_data.values})
        employ_data = employ_data.set_index('Date')

        yield_data = fred.get_series_latest_release('GS10')
        yield_data = pd.DataFrame({'Date': yield_data.index, 'Market Yield': yield_data.values})
        yield_data = yield_data.set_index('Date')

        industrial_data = fred.get_series_latest_release('INDPRO')
        industrial_data = pd.DataFrame({'Date': industrial_data.index, 'Industrial Production Rate': industrial_data.values})
        industrial_data = industrial_data.set_index('Date')

        treasurybill_data = fred.get_series_latest_release('TB3MS')
        treasurybill_data = pd.DataFrame({'Date': treasurybill_data.index, 'Treasury Bill Rate': treasurybill_data.values})
        treasurybill_data = treasurybill_data.set_index('Date')

        cpi_data = fred.get_series_latest_release('CPIAUCSL')
        cpi_data = pd.DataFrame({'Date': cpi_data.index, 'CPI': cpi_data.values})
        cpi_data = cpi_data.set_index('Date')

        capacity_data = fred.get_series_latest_release('CUMFNS')
        capacity_data = pd.DataFrame({'Date': capacity_data.index, 'Capacity Utilization': capacity_data.values})
        capacity_data = capacity_data.set_index('Date')

        #write pulled data to csv
        data_frames = [rec_data, cpi_data, employ_data, yield_data, industrial_data, treasurybill_data, capacity_data]
        data_frames_name = ["rec_data", "cpi_data", "employ_data", "yield_data", "industrial_data", "treasurybill_data", "capacity_data"]

        i = 0

        for k in data_frames:
            k.to_csv(pulled_data_dir + '{}.csv'.format(str(data_frames_name[i])))
            i = i + 1

        #select rows to use for training and testing
        clean_rec_data = rec_data["1971-01-01":"2021-08-01"]
        clean_cpi_data = cpi_data["1970-12-01":"2021-08-01"]
        clean_employ_data = employ_data["1970-12-01":"2021-08-01"]
        clean_yield_data = yield_data["1970-12-01":"2021-08-01"]
        clean_industrial_data = industrial_data["1970-12-01":"2021-08-01"]
        clean_treasurybill_data = treasurybill_data["1970-12-01":"2021-08-01"]
        clean_capacity_data = capacity_data["1970-12-01":"2021-08-01"]

        #write cleaned data to csv
        clean_data_frames = [clean_rec_data, clean_cpi_data, clean_employ_data, clean_yield_data, clean_industrial_data, clean_treasurybill_data, clean_capacity_data]
        clean_data_frames_name = ["clean_rec_data", "clean_cpi_data", "clean_employ_data", "clean_yield_data", "clean_industrial_data", "clean_treasurybill_data", "clean_capacity_data"]

        i = 0

        for k in clean_data_frames:
            k.to_csv(clean_data_dir + '{}.csv'.format(str(clean_data_frames_name[i])))
            i = i + 1

        #merging datasets and calculating the monthly increase or decrease for each column of data
        merged_data = reduce(lambda left, right: pd.merge(left, right, on=["Date"]), clean_data_frames)
        monthly_diff = merged_data.diff()[1:]
        monthly_diff = monthly_diff.drop(columns = ['Recession'])


        #export new datasets
        merged_data.to_csv(processed_data_dir + 'merged_data.csv')
        monthly_diff.to_csv(processed_data_dir + 'monthly_diff.csv')

        #get most recent data
        recent_cpi_data = cpi_data[-2:].diff()[1:]
        recent_employ_data = employ_data[-2:].diff()[1:]
        recent_yield_data = yield_data[-2:].diff()[1:]
        recent_industrial_data = industrial_data[-2:].diff()[1:]
        recent_treasurybill_data = treasurybill_data[-2:].diff()[1:]
        recent_capacity_data = capacity_data[-2:].diff()[1:]

        recent_data_frames = [recent_cpi_data, recent_employ_data, recent_yield_data, recent_industrial_data, recent_treasurybill_data, recent_capacity_data]
        recent_merged_data = reduce(lambda left, right: pd.merge(left, right, on=["Date"]), recent_data_frames)
        recent_merged_data.to_csv(processed_data_dir + 'recent_merged_data.csv')

