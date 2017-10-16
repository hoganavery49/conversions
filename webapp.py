from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/pounds-to-kilos")
def render_pounds_conversion():
    return render_template('lbs-to-kgs.html')

@app.route("/grams-to-moles")
def render_grams_conversion():
    return render_template('grams-to-moles.html')

@app.route("/meters-to-femtometers")
def render_meters_conversion():
    return render_template('meters-to-femtometers.html')

@app.route("/response")
def render_response():
    if 'pounds' in request.args:
        try:
            reply = round(float(request.args['pounds'])*0.45359237, 2)
            unit = 'kilograms'
        except ValueError:
            return render_template('response.html', response = 'Error, invalid input', unit = '')
    elif 'grams' in request.args:
        try:
            reply = float(request.args['grams'])/float(request.args['molar-mass'])
            unit = 'moles'
        except ValueError:
            return render_template('response.html', response = 'Error, invalid input', unit = '')
    else:
        try:
            reply = float(request.args['meters'])*0.0000000000000015
            unit = 'femtometers'
        except ValueError:
            return render_template('response.html', response = 'Error, invalid input', unit = '')

    return render_template('response.html', response = reply, unit = unit)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)