import main
import pandas as pd
import numpy as np
import json
from flask import Flask, render_template, jsonify, request, Response
from flask_cors import CORS
app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/api/data', methods=['POST'])
def get_calculated_data():
    simi_res = request.get_json()
    print(simi_res)
    result = main.Compute(simi_res)
    ans = result.getResult()
    print(ans)
    table_val = ans.values.tolist()
    table_val = [val[2:] for val in table_val]
    response = {
        'tdata': table_val
    }
    print(jsonify(response))
    return jsonify(response)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")