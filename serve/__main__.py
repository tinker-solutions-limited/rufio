from flask import Flask
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)

@app.route('/uwu-bot/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=environ['RUFIO_PORT'])