#!/usr/bin/env python
import os

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ.get('MONGO_HOST_PORT', 'mongo:27017'))

@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return 'Server not available'
    return 'Hello from the MongoDB client!\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

