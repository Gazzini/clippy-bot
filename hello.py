from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/message')
def show_message():
    return 'hello message!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
