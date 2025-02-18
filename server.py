from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'welcome to the server'

@app.route('/version')
def version():
    return "<h1>v1.5</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
