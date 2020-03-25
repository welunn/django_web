from flask import Flask, render_template
from flask import request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name="张三")


@app.route("/userinfo")
def userInfo():
    if request.method == "GET":
        return "<h2>用户信息页面</h2>"
    else:
        return "<h2>用户信息存储功能</h2>"


if __name__ == "__main__":
    app.run(debug=True)