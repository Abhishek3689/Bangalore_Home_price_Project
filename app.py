from flask import Flask,render_template,request
import pandas as pd
import json
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

preprocessor=pickle.load(open('models/preprocessor_price.pkl','rb'))
model=pickle.load(open('models/model_price.pkl','rb'))

columns=pd.read_json("columns.json")
locations=columns.iloc[4:]
# print(locations[:10])
locations=list(locations['data_columns'])

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    #return render_template('home.html',locations=locations)
@app.route("/predict",methods=['GET','POST'])
def predict_house_price():
    if request.method=="POST":
        location=request.form['location']
        total_sqft=float(request.form['total_sqft'])
        Bathroom=float(request.form['Bathroom'])
        Balcony=float(request.form['Balcony'])
        BHK_Size=float(request.form['BHK_Size'])


        data=pd.DataFrame({'location':location,'total_sqft':total_sqft,'bath':Bathroom,'balcony':Balcony,'BHK_size':BHK_Size},index=[1])
        new_scaled_data=preprocessor.transform(data)
        result=model.predict(new_scaled_data)
        print("Clear")
        return render_template('home.html',locations=locations,results=result)
    else:
        print("Error in post")
        return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)
