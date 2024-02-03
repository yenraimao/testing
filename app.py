# this is a simple web app using flask, made for testing
# routes accessed e.g http://localhost:5000/ api/data

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello, API!"})

@app.route('/api/nonexistent', methods=['GET'])
def nonexistent_data():
    return jsonify({"message": "hmmmmmmm!"})
if __name__ == '__main__':
    app.run(debug=True)
