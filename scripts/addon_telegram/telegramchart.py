import os
import pandas as pd
import matplotlib.pyplot as plt


def telegramchart(datatype_input='cpi', startdate_input='2020-01-01', enddate_input='2021-01-01'):
    # Get the directory where this script is running
    script_dir = os.path.dirname(__file__)
    
    # Get the pulled data directory
    pulled_data_dir = os.path.join(script_dir, '../../generated_datasets/pulled_data/')
    
    # Get the datapng directory
    datapng_dir = os.path.join(script_dir, '../../telegram_charts/')
    
    # Valid datatype: recession, cpi, unemployment, bill, yield, industrial
    datatype = datatype_input
    startdate = startdate_input
    enddate = enddate_input
    
    # Set the csv filename
    filename = os.path.join(pulled_data_dir,  datatype + '_data.csv')
    
    # Import data using datetime and no data value
    df = pd.read_csv(filename, parse_dates=['Date'], index_col= ['Date'])
    df = df[startdate:enddate]
    
    # Plot to chart
    df.plot()
    
    # Beautify the x-labels
    plt.gcf().autofmt_xdate()
    
    # Save as PNG
    plt.savefig(datapng_dir + datatype + ".png")

