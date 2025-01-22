from flask import Flask, request

app = Flask(__name__, static_folder='web/static', static_url_path='',)

@app.route("/api/hello")
def helloworld():
    return "Hello World!"

@app.route("/api/data")
def getdata():
    return {"message":"You clicked!"}

if __name__ == "__main__":
    app.run(debug=True, port=8080)


