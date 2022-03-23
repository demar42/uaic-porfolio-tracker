from flask import Flask, request
import app.chart_data_builder

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>UAIC Portfolio Tracker</h1>Docs to appear here soon...'

@app.route('/get-chart', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json['body']
        return app.chart_data_builder.main(data)
    else:
        return 'Content-Type not supported!'