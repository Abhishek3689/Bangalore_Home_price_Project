import pandas as pd
import json
from flask import Flask,render_template,request

columns=pd.read_json("columns.json")
locations=columns.iloc[4:]
# print(locations[:10])
locations=list(locations['data_columns'])


app = Flask(__name__)
@app.route("/")
def hello_world1():
    #return render_template('index.html')
    return render_template('home.html',locations=locations)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)