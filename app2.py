import time 
from flask import Flask, jsonify 
from flask_cors import CORS 
import skripta as s 
 
app = Flask(__name__) 
CORS(app) 
@app.route('/') 
 
def home(): 
    return "Startovanje aplikacije je na adresi /start, informacije o sigurnosti nalaze na adresi /safety" 
 
 
@app.route('/safety') 
def safety(): 
        vrednost = s.distance() 
        if(int(vrednost)<5000): 
            return jsonify({"distanca":vrednost, "poruka":"Nedozvoljen pristup"}) 
        else: 
            return jsonify({"distanca":vrednost, "poruka":"Sigurnost je na maksimalnom nivou"}) 
 
     
@app.route('/start') 
def pokreni(): 
    s.setup() 
    s.main() 
    return jsonify({"poruka":"Pokrenuta aplikacija"}) 
 
 
if __name__==("__main__"): 
    app.run(debug=True, host="0.0.0.0")  