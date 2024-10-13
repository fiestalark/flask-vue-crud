from flask import Flask, jsonify
from flask_cors import CORS

# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Sanity check route

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()