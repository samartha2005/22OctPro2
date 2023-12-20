'''Create a Flask app that consumes data from external APIs and displays it to users.
Try to find an public API which will give you a data and based on that call it and 
deploy it on cloud platform'''
# Code
from flask import Flask, render_template,request
import requests

app = Flask(__name__)

# Function to fetch data from the external API
@app.route('/PublicAPIapp',methods=['POST','GET'])
def get_data():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    param={
        'id':request.form.get("id")
    }
    response = requests.get(api_url,params=param)
    data = response.json()
    return data

@app.route('/')
def index():
    # Get data from the external API
    data = get_data()
    
    # Pass data to the template
    return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(host="0.0.0.0")




