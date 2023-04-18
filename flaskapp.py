from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://JayPatel:Jay123@cluster0.xixsv8j.mongodb.net/?retryWrites=true&w=majority')
db = client['stock_database']
collection = db['stock_collection']

@app.route('/')
def index():
    # Retrieve data from MongoDB database
    data = collection.find()
    # Render HTML template with data
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    data = collection.find()
    return render_template('about.html',)

@app.route('/charts')
def charts():
    data = collection.find()
    print
    return render_template('charts.html', data = data)

@app.route('/linechart')
def linechart():
    data = collection.find()
    return render_template('linechart.html', data = data)

if __name__ == '__main__':
    app.run(debug=True)
