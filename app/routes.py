from app import app
import os
import json
import plotly
import plotly.express as px
import pandas as pd
from flask import Flask,render_template,request, send_file, redirect

#app = Flask(__name__)
#configuring the cache timing to be 0s
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

#find the direcory for the dataset
generated_dataset_dir = os.path.join(app.root_path, 'generated_datasets', 'clean_data')

#function to generate the years for the dropdown filter
def make_list():
    dwpath = os.path.join(app.root_path,'generated_datasets/processed_data/merged_data.csv')
    yearlist = pd.read_csv(dwpath)
    yearlist = yearlist.rename(columns={'Date': 'Year'})
    yearlist = yearlist["Year"].tolist()
    return yearlist

def Addrect(fig):
    fig.add_vrect(x0="1973-12-01", x1="1975-03-01", fillcolor="Yellow", opacity=0.5, layer="below", line_width=0)
    fig.add_vrect(x0="1980-02-01", x1="1980-07-01", fillcolor="Yellow", opacity=0.5, layer="below", line_width=0)
    fig.add_vrect(x0="1981-08-01", x1="1982-11-01", fillcolor="Yellow", opacity=0.5, layer="below", line_width=0)
    fig.add_vrect(x0="1990-08-01", x1="1991-03-01", fillcolor="Yellow", opacity=0.5, layer="below", line_width=0)
    fig.add_vrect(x0="2001-03-01", x1="2001-11-01", fillcolor="Yellow", opacity=0.5, layer="below", line_width=0)
    fig.add_vrect(x0="2007-03-01", x1="2009-11-01", fillcolor="Yellow", opacity=0.5, layer="below", line_width=0)
    fig.add_vrect(x0="2020-02-01", x1="2020-04-01", fillcolor="Yellow", opacity=0.5, layer="below", line_width=0)
    return fig

#Variables for the drop down filter
DATELIST = make_list()
DATELIST2 = sorted(DATELIST,reverse=True)

#routings for different wepages
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/model_testing")
def model_testing():
    reader = open(os.path.join(app.root_path,'scripts','results.txt'), "r") #reads the results.txt generated after the machine learning
    Results = reader.readline()
    reader.close()
    #making of the bar graph using plotly
    model_df = pd.read_csv(os.path.join(app.root_path,'generated_datasets','processed_data','recent_merged_data.csv'))
    x_Axis = list(model_df)
    #removal of the unwanted variable for x-axis
    x_Axis.remove("Date")
    #getting the values for each variable and removing the date for y-axis
    y_Axis = list(model_df.iloc[0])
    del y_Axis[0]
    #plotly coming up with the graph
    fig = px.bar(x=x_Axis, y=y_Axis, orientation='v', barmode='group', title="Monthly Difference")
    #updating axes names
    fig.update_xaxes(title_text='Variables')
    fig.update_yaxes(title_text='Change from the previous month')
    #converting python object to json string for javascript to parse
    modelJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("model_testing.html",modelJSON=modelJSON,results=Results)

@app.route("/approach")
def approach():
    return render_template("approach.html")

@app.route("/task")
def task():
    return render_template("task.html")

@app.route("/about_us")
def about_us():
    return render_template("about.html")

@app.route('/download')
def downloadFile():
    #checking what graph needs to be downloaded then redirect accordingly
    if dwngraph == "cpi":
        return redirect('/downloadcpi')
    if dwngraph =="unemployment":
        return redirect('/downloademploy')
    if dwngraph == "data_yield":
        return redirect("/downloaddata_yield")
    if dwngraph == "data_industrial":
        return redirect("/downloaddata_industrial")
    if dwngraph == "treasurybill":
        return redirect("/downloadtreasurybill")
    if dwngraph == "recession":
        return redirect("/downloadrecession")
    if dwngraph == "capcity":
        return redirect("/downloadcapcity")
    if dwngraph == "multiple":
        return redirect("/downloadmultiple")
    else:
        return render_template('/data.html')

#the redirections for specific graph downloads
@app.route('/downloadcpi')
def downloadcpi():
    return send_file(dwpath,as_attachment=True,cache_timeout=0)

@app.route('/downloademploy')
def downloademploy():
    return  send_file(dwpath,as_attachment=True,cache_timeout=0)

@app.route('/downloaddata_yield')
def downloaddata_yield():
    return send_file(dwpath,as_attachment=True,cache_timeout=0)

@app.route('/downloaddata_industrial')
def downloaddata_industrial():
    return send_file(dwpath,as_attachment=True,cache_timeout=0)

@app.route('/downloadtreasurybill')
def downloadtreasurybill():
    return send_file(dwpath,as_attachment=True,cache_timeout=0)

@app.route('/downloadrecession')
def downloadrecession():
    return send_file(dwpath,as_attachment=True,cache_timeout=0)

@app.route('/downloadcapcity')
def downloadcapcity():
    return send_file(dwpath,as_attachment=True,cache_timeout=0)

@app.route('/downloadmultiple')
def downloadmultiple():
    return send_file(dwpath,as_attachment=True,cache_timeout=0)

#main dataset page route and the making for the graphs
@app.route("/data")
def datasets():
    global dwpath
    global dwngraph
    #checking of variable in the form submission
    Diff = request.args.getlist("diff")
    testv = request.args.getlist("chk")
    datefilter1 = request.args.get("filter1")
    datefilter2 = request.args.get("filter2")
    thedata = request.args.get("graph")
    dwngraph = thedata
    if thedata == "cpi":
        dwpath = os.path.join(generated_dataset_dir,'clean_cpi_data.csv')
        cpi = pd.read_csv(dwpath)
        cpi = cpi.rename(columns={'Date': 'Year'})
        fig = px.line(cpi, x="Year", y="CPI",title="Consumer Price Index")
        Addrect(fig)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        datamsg = """The Consumer Price Index (CPI) is a measure that examines the weighted average of prices of a basket of consumer goods and services, such as transportation, food, and medical care. It is calculated by taking price changes for each item in the predetermined basket of goods and averaging them."""
        return render_template("data.html", graphJSON=graphJSON,datelist=DATELIST,datelist2=DATELIST2,datamsg=datamsg)

    if thedata == "unemployment":
        dwpath = os.path.join(generated_dataset_dir,'clean_employ_data.csv')
        ue = pd.read_csv(dwpath)
        ue = ue.rename(columns={'Date': 'Year'})
        fig = px.line(ue, x= "Year", y="Unemployment Rate",title="Unemployment Rates")
        Addrect(fig)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        datamsg = """The unemployment rate is the percent of the labor force that is jobless. It is a lagging indicator, meaning that it generally rises or falls in the wake of changing economic conditions, rather than anticipating them."""
        return render_template("data.html", graphJSON=graphJSON,datelist=DATELIST,datelist2=DATELIST2,datamsg=datamsg)

    if thedata == "data_yield":
        dwpath = os.path.join(generated_dataset_dir,'clean_yield_data.csv')
        dy = pd.read_csv(dwpath)
        dy = dy.rename(columns={'Date': 'Year'})
        fig = px.line(dy, x= "Year", y="Market Yield",title="Market Yield")
        Addrect(fig)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        datamsg = """The money market yield is the interest rate earned by investing in securities with high liquidity and maturities of less than one year such as negotiable certificates of deposit, U.S. Treasury bills, and municipal notes."""
        return render_template("data.html", graphJSON=graphJSON,datelist=DATELIST,datelist2=DATELIST2,datamsg=datamsg)

    if thedata == "data_industrial":
        dwpath = os.path.join(generated_dataset_dir,'clean_industrial_data.csv')
        di = pd.read_csv(dwpath)
        di = di.rename(columns={'Date': 'Year'})
        fig = px.line(di, x= "Year", y="Industrial Production Rate",title="Industrial Production Rates")
        Addrect(fig)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        datamsg = """The industrial production rate (IPR) is a monthly economic indicator measuring real output in the manufacturing, mining, electric, and gas industries, relative to a base year."""
        return render_template("data.html", graphJSON=graphJSON,datelist=DATELIST,datelist2=DATELIST2,datamsg=datamsg)

    if thedata == "treasurybill":
        dwpath = os.path.join(generated_dataset_dir,'clean_treasurybill_data.csv')
        di = pd.read_csv(dwpath)
        di = di.rename(columns={'Date': 'Year'})
        fig = px.line(di, x= "Year", y="Treasury Bill Rate",title="Treasury Bill Rates")
        Addrect(fig)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        datamsg = """The interest rate of Treasury Bill (T-Bill) is a short-term U.S. government debt obligation backed by the Treasury Department with a maturity of one year or less."""
        return render_template("data.html", graphJSON=graphJSON,datelist=DATELIST,datelist2=DATELIST2,datamsg=datamsg)

    if thedata== "recession":
        dwpath = os.path.join(generated_dataset_dir,'clean_rec_data.csv')
        rec = pd.read_csv(dwpath)
        rec = rec.rename(columns={'Date': 'Year'})
        fig = px.bar(rec, x= "Year", y="Recession",title="Recession")
        Addrect(fig)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        datamsg = """A recession is a macroeconomic term that refers to a significant decline in general economic activity in a designated region. It had been typically recognized as two consecutive quarters of economic decline, as reflected by GDP in conjunction with monthly indicators such as a rise in unemployment."""
        return render_template("data.html", graphJSON=graphJSON,datelist=DATELIST,datelist2=DATELIST2,datamsg=datamsg)

    if thedata== "capcity":
        dwpath = os.path.join(generated_dataset_dir,'clean_capacity_data.csv')
        cap = pd.read_csv(dwpath)
        cap = cap.rename(columns={'Date': 'Year'})
        fig = px.line(cap, x= "Year", y="Capacity Utilization",title="Capacity Utilization")
        Addrect(fig)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        datamsg = """Capacity utilization rate measures the percentage of an organization's potential output that is actually being realized. The capacity utilization rate of a company or a national economy may be measured in order to provide insight into how well it is reaching its potential."""
        return render_template("data.html", graphJSON=graphJSON,datelist=DATELIST,datelist2=DATELIST2,datamsg=datamsg)

    if thedata=="multiple":
        Message=" "
        if 'diff' in Diff:
            dwpath = os.path.join(app.root_path,'generated_datasets/processed_data/monthly_diff.csv')
            if 'Recession' in testv:
                testv.remove('Recession')
                Message = "There is no monthly difference for recession"
        else:
            dwpath = os.path.join(app.root_path,'generated_datasets/processed_data/merged_data.csv')
        md = pd.read_csv(dwpath)
        md = md.rename(columns={'Date': 'Year'})
        md = md[~(md['Year'] > datefilter2)]
        md = md[~(md['Year'] < datefilter1)]
        fig = px.line(md, x="Year", y=testv, title="Filtered Graph")
        Addrect(fig)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template("data.html", graphJSON=graphJSON,datelist=DATELIST,datelist2=DATELIST2,message=Message)
    else:
        return render_template("data.html", message="Select a graph",datelist=DATELIST,datelist2=DATELIST2)