from flask import Flask

app = flask(__name__) # hace ref al nombre del archivo
@app.route('/')
def hellow_Flask():
    return 'Hello Flask'


if __name__ == '__main__':
    app.run(debug= True, host='127.0.0.1',port=5000)
