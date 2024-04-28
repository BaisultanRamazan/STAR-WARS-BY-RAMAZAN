from flask import Flask,render_template
app = Flask(__name__, static_url_path='/static')

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template("mainpage.html")

@app.route('/pickasidepage')
def pickaside():
    return render_template("pickasidepage.html")

@app.route('/whiteregistration')
def whitereg():
    return render_template("whiteregistration.html")

@app.route('/darkregistration')
def darkreg():
    return render_template("darkregistration.html")

@app.route('/whitesidepage')
def whitepage():
    return render_template("whitesidepage.html")

@app.route('/darksidepage')
def darkpage():
    return render_template("darksidepage.html")



if __name__ == "__main__":
    app.run(debug=True)