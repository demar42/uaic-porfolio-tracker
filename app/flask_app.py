from flask import Flask, request
import chart_data_builder

app = Flask(__name__)

@app.route('/get_chart', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json['body']
        return chart_data_builder.main(data)
    else:
        return 'Content-Type not supported!'