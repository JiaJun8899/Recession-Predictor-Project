machinelearning.py
============================================================
This project is controlled from the `machinelearning.py` file. The program's main purpose is to
1. Crawl the data using fredapi
2. Running of the machine learning script
3. Plotting of graphs from datasets

`machinelearning.py` accepts arguments:

Arguments are optional, will only create datasets when run without arguments

**Argument 1**

>plot_all : plots graphs from all datasets 
 
>plot_pull : plots graphs from pulled datasets

>plot_clean : plots graphs from cleaned datasets

>plot_process : plots graphs from process datasets

**Argument 2**
>1 : runs the model training and testing and recession prediction, outputs results to results.txt.
<br>Testing accuracy for each model is shown in the graph in generated_datasets/misc_graphs.

Example of running `machinelearning.py` without argument 1 
```
python machinelearning.py none 1
```
This will run the data crawler and the model test scripts but will not create any graphs.
****************************************************************
The data crawling is run daily at midnight using the below crontab. 
-----------------------------------------------------------------
```
0 0 * * * python /var/www/1002/app/scripts/machinelearning.py >/dev/null 2>&1 
```