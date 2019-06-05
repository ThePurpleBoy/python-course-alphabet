from flask import Flask, render_template, redirect, url_for
from blue import blue


app = Flask(__name__)
app.register_blueprint(blue)


@app.errorhandler(404)
def error(error):
    return render_template('error.html')


@app.route("/dont_click")
def dont_click():
    return render_template("dont_click.html")


@app.route("/redirect")
def my_redirect():
    return redirect(url_for("dont_click"))


if __name__ == '__main__':
    app.run(debug=True)
