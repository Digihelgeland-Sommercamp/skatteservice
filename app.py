from flask import Flask, request
import json
import os
import werkzeug

from skatt_exceptions import ItemNotFound

#Hent ut skattemeldinger.json
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'skattemeldinger.json'))
skatter = json.load(f)
f.close()

#Create app
app = Flask(__name__)

#Register exceptions
app.register_error_handler(ItemNotFound, 500)


#create routes
@app.route("/")
def root():
    return "<p>Root route! :D:D:D</p>"

@app.route("/skattemeldinger")
def get_all_skattemeldinger():
    return skatter


@app.route("/get_skattemelding/<inntektsaar>/<personidentifikator>")
def get_skattemelding(inntektsaar=None, personidentifikator=None):
    for k in skatter['skattemeldinger']:
        if (
            k['personidentifikator'] == personidentifikator 
            and k['inntektsaar'] == inntektsaar
        ): return json.dumps(k)

    return ItemNotFound()





if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)