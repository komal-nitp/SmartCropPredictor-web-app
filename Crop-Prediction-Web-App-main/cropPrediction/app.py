from flask import Flask, render_template, request
from main import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/predict')
def page():
    syn  = [[90 ,42, 43 , 20.879744,82.002744 , 6.502985 , 202.935536]]
    it = predict(syn)

    it = it[0]

    return render_template("predict.html", it = it)


@app.route('/result', methods=["POST"])
def result():

    Nitrogen = float(request.form['Nitrogen'])
    Phosphorus = float(request.form['Phosphorus'])
    Potassium = float(request.form['Potassium'])
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Ph = float(request.form['ph'])
    Rainfall = float(request.form['Rainfall'])
     
    values = [Nitrogen , Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]

    val = [values]
    if Ph > 14 or Ph < 0 :
        return render_template("result.html", ans = "Ph value is not in range")
    else:
        ans  = predict(val)
        ans = (ans[0]).upper()
        return render_template("result.html", ans = ans)
        


if __name__ == "__main__":
    app.run( debug = True)

