#this program plots graphs for all the datasets created by create_dataset

import os
import pandas as pd
import matplotlib.pyplot as plt
import glob


class create_plots():
    def __init__(self):
        pass

    def recent_monthly_change(self):

        # Get the directory where this script is running
        script_dir = os.path.dirname(__file__)

        # Get the generated datasets directory
        generated_datasets_dir = os.path.join(script_dir, '../../generated_datasets/')

        processed_data_dir = os.path.join(generated_datasets_dir, 'processed_data/')

        #generate graph based on the most recent monthly change
        recent_merged_data = pd.read_csv(processed_data_dir + "recent_merged_data.csv", index_col=0)
        col_names = list(recent_merged_data.columns)
        row_data = []
        for k in range(6):
            row_data.append(recent_merged_data.iloc[0][str(col_names[k])])

        plt.figure(figsize=(12, 12), dpi = 100)
        plt.bar(col_names, row_data, width = 0.4)
        plt.xlabel('Datasets')
        plt.ylabel('Change from previous month')
        plt.savefig(processed_data_dir + "recent_merged_data.png")
        plt.close()

    def monthly_change(self):

        # Get the directory where this script is running
        script_dir = os.path.dirname(__file__)

        # Get the generated datasets directory
        generated_datasets_dir = os.path.join(script_dir, '../../generated_datasets/')

        processed_data_dir = os.path.join(generated_datasets_dir, 'processed_data/')

        #generate graphs for monthly change
        monthly_diff = pd.read_csv(processed_data_dir + "monthly_diff.csv")
        diff_col_names = list(monthly_diff.columns)
        diff_row_data = []

        for k in diff_col_names:
            diff_row_data.append(monthly_diff[k].tolist())

        for k in range(1, len(diff_col_names)):
            x_axis = monthly_diff.iloc[:, 0]
            y_axis = diff_row_data[k]
            plt.figure()
            plt.plot(x_axis, y_axis)
            plt.xlabel('Date')
            plt.ylabel('Change in {} per month'.format(diff_col_names[k]))
            plt.savefig(processed_data_dir + "change_in_{}_graph.png".format((diff_col_names[k]).replace(" ", "_")))
            plt.close()

    #function to create graphs for pulled and cleaned data
    def create_pulled_graph(self):

        # Get the directory where this script is running
        script_dir = os.path.dirname(__file__)

        # Get the generated datasets directory
        generated_datasets_dir = os.path.join(script_dir, '../../generated_datasets/')

        pulled_data_dir = os.path.join(generated_datasets_dir, 'pulled_data/')

        #get names of all csv files to be used
        all_files = glob.glob(pulled_data_dir + "*.csv")

        #read csv files and map to list
        datasets = map(lambda filename: pd.read_csv(filename), all_files)
        datasets = list(datasets)
        #print(datasets[0])

        #get csv column names
        li = []
        for k in range(len(datasets)):
            li.append(list(datasets[k].columns))

        #print(li)

        for k in range(len(datasets)):
            x_axis = datasets[k].iloc[:, 0]
            y_axis = datasets[k].iloc[:, 1]
            plt.figure()
            plt.plot(x_axis, y_axis)
            plt.xlabel('Date')
            plt.ylabel(li[k][1])
            plt.savefig('{}{}_graph.png'.format(pulled_data_dir, (li[k][1]).replace(" ","_")))
            plt.close()
            #plt.show()


    def create_clean_graph(self):

        # Get the directory where this script is running
        script_dir = os.path.dirname(__file__)

        # Get the generated datasets directory
        generated_datasets_dir = os.path.join(script_dir, '../../generated_datasets/')

        clean_data_dir = os.path.join(generated_datasets_dir, 'clean_data/')

        # get names of all csv files to be used
        all_files = glob.glob(clean_data_dir + "clean_*.csv")

        # read csv files and map to list
        datasets = map(lambda filename: pd.read_csv(filename), all_files)
        datasets = list(datasets)
        # print(datasets[0])

        # get csv column names
        li = []
        for k in range(len(datasets)):
            li.append(list(datasets[k].columns))

        # print(li)

        for k in range(len(datasets)):
            x_axis = datasets[k].iloc[:, 0]
            y_axis = datasets[k].iloc[:, 1]
            plt.figure()
            plt.plot(x_axis, y_axis)
            plt.xlabel('Date')
            plt.ylabel(li[k][1])
            plt.savefig('{}{}_graph.png'.format(clean_data_dir, (li[k][1]).replace(" ", "_")))
            plt.close()
            # plt.show()
