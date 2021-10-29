Project 11: Recession Predictor
===================================================================
This application is a recession predictor for the United States of America.
This project used multiple economic indicators to predict a possible recession.
It uses K-Nearest Neighbors Algorithm to predict the recession.
The project is coded in python and has a front-end of HTML and Javascript
This project comes with a telegram bot

Our hosted webpage: http://34.87.128.123/

Data used is from [Federal Reserve Economic Data](https://fred.stlouisfed.org/)
********************************************************************
Main Scripts
--------------------------------------------------------------------
1. `start.bat` is the batch file to start the application on local server.
2. `app.py` is the source code for the flask UI
3. `machinelearning.py` is the source code for our machine learning
   1.  `create_dataset.py` is the datacrawler to generate the needed csv files for the entire program
   2.  `create_plots.py` is to create a .png of each data crawled
   3.  `model_train.py` is the our machine learning script
4. `telegrambot.py` is the source code for our telegram bot
   1. `telegramchart.py` has functions to assist the creation of the graphs in the telegram bot
********************************************************************
Viewing or installing our application:
--------------------------------------------------------------------
1. Visit our website: [Click here](http://34.87.128.123/)
2. Installation the application locally using `start.bat`
> Note that it will take awhile for the necessary libararies and data to be crawled.
4. Hosting on your own public server view instructions down below
********************************************************************
To install on a public server:
--------------------------------------------------------------------
1. Copy `ICT1002_P1_G5_Project_11.tar.gz` to the server
Run the below commands to complete the installation

2. Set-up and update the server:
```bash
sudo dnf -y update
sudo dnf -y install gcc zlib-devel libjpeg-devel freetype-devel python3-devel httpd
sudo mkdir /var/www/1002_P1_G5
sudo unzip ICT1002_P1_G5_Project_11.zip -d "/var/www/1002_P1_G5/"
cd /var/www/1002_P1_G5
sudo python3 -m pip install -r requirements.txt
```

3. Set-up telegram server
```
cat > /etc/systemd/system/telegrambot.service <<'endmsg'

[Unit] 
Description=Telegram Bot Service 
After=multi-user.target

[Service] 
Type=simple 
Restart=always 
ExecStart=/usr/bin/python3 /var/www/1002_P1_G5/app/scripts/addon_telegram/telegrambot.py

[Install] 
WantedBy=multi-user.target
endmsg

bash sudo systemctl daemon-reload
sudo systemctl start telegrambot
sudo systemctl enable telegrambot
```
4. Making of flask server
```bash cat > /etc/systemd/system/flask.service <<'endmsg'
[Unit]
Description=Flask Service

[Service]
ExecStart = /bin/bash /var/www/1002_P1_G5/flaskrun.sh

[Install]
WantedBy = multi-user.target
endmsg

sudo systemctl daemon-reload
sudo systemctl start flask
sudo systemctl enable flask
```
********************************************************************
There are two ways to start Flask (For public server)
--------------------------------------------------------------------
1. ```bash ./flaskrun.sh``` 
2. Create a system process using the below config. (Assuming the full path is /var/www/1002_P1_G5/) 
The process will be started automatically during the system boot up. 
```bash
[Unit] 
Description=Flask Service 
 
[Service] 
ExecStart = /bin/bash /var/www/1002_P1_G5/flaskrun.sh 
 
[Install] 
WantedBy = multi-user.target 
```
********************************************************************
Further improvements:
-------------------------------------------------------------------
1. The function `addrect()` can be more dynamic such that be shown properly in the filter data.
2. Using more modules 
********************************************************************
File directory:
--------------------------------------------------------------------
```
├── app 
│   ├── generated_datasets 
│   │   ├── clean_data 
│   │   │   ├── Capacity_Utilization_graph.png 
│   │   │   ├── clean_capacity_data.csv 
│   │   │   ├── clean_cpi_data.csv 
│   │   │   ├── clean_employ_data.csv 
│   │   │   ├── clean_industrial_data.csv 
│   │   │   ├── clean_rec_data.csv 
│   │   │   ├── clean_treasurybill_data.csv 
│   │   │   ├── clean_yield_data.csv 
│   │   │   ├── CPI_graph.png 
│   │   │   ├── Industrial_Production_Rate_graph.png 
│   │   │   ├── Market_Yield_graph.png 
│   │   │   ├── Recession_graph.png 
│   │   │   ├── Treasury_Bill_Rate_graph.png 
│   │   │   └── Unemployment_Rate_graph.png 
│   │   ├── misc_graphs 
│   │   │   └── xvalidation.png 
│   │   ├── processed_data 
│   │   │   ├── change_in_Capacity_Utilization_graph.png 
│   │   │   ├── change_in_CPI_graph.png 
│   │   │   ├── change_in_Industrial_Production_Rate_graph.png 
│   │   │   ├── change_in_Market_Yield_graph.png 
│   │   │   ├── change_in_Treasury_Bill_Rate_graph.png 
│   │   │   ├── change_in_Unemployment_Rate_graph.png 
│   │   │   ├── merged_data.csv 
│   │   │   ├── monthly_diff.csv 
│   │   │   ├── recent_merged_data.csv 
│   │   │   └── recent_merged_data.png 
│   │   └── pulled_data 
│   │       ├── capacity_data.csv 
│   │       ├── Capacity_Utilization_graph.png 
│   │       ├── cpi_data.csv 
│   │       ├── CPI_graph.png 
│   │       ├── employ_data.csv 
│   │       ├── industrial_data.csv 
│   │       ├── Industrial_Production_Rate_graph.png 
│   │       ├── Market_Yield_graph.png 
│   │       ├── rec_data.csv 
│   │       ├── Recession_graph.png 
│   │       ├── treasurybill_data.csv 
│   │       ├── Treasury_Bill_Rate_graph.png 
│   │       ├── Unemployment_Rate_graph.png 
│   │       └── yield_data.csv 
│   ├── init.py 
│   ├── routes.py 
│   ├── scripts 
│   │   ├── addon_telegram 
│   │   │   ├── telegrambot.py 
│   │   │   └── telegramchart.py 
│   │   ├── data 
│   │   │   ├── create_dataset.py 
│   │   │   └── create_plots.py 
│   │   ├── machinelearning.py 
│   │   ├── model 
│   │   │   └── model_train.py 
│   │   └── results.txt 
│   ├── static 
│   │   ├── graph_stock.png 
│   │   ├── main.js 
│   │   ├── task_stock2.png 
│   │   ├── task_stock.png 
│   │   ├── tele_icon.png 
│   │   └── xvalidation.png 
│   ├── telegram_charts 
│   │   ├── bill.png 
│   │   ├── cpi.png 
│   │   ├── employ.png 
│   │   ├── industrial.png 
│   │   ├── recession.png 
│   │   ├── rec.png 
│   │   ├── unemployment.png 
│   │   └── yield.png 
│   └── templates 
│       ├── about.html 
│       ├── approach.html 
│       ├── data.html 
│       ├── index.html 
│       ├── layout.html 
│       ├── model_testing.html 
│       └── task.html 
├── README.md
├── Requirements.txt
└── app.py
```
