import numpy as np
from flask import Flask, jsonify, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods = ['POST'])
def predict():
    '''
    For rendering prediction on HTML GUI
    '''
    try:

       feature = [float(x) for x in request.form.values()]
       final_feature = [np.array(feature)]
       prediction = model.predict(final_feature)
       if prediction[0] == 0:
        result = "breast cancer report is negative"
       else:
        result = "breast cancer report is positive"
        return render_template("index.html", prediction_text = result)
    
@app.route('/predict_api', methods= ['POST'])
def predict_api():
    '''
    For direct api call through request
    '''
    data = request.get_json(force = True)
    prediction = model.predict([np.array(list(data.values()))])
    output = "breast cancer is positive" if prediction[0] == 1 else "breast cancer is negative"
    return josify(output)
if __name__ = "__main":
    app.run(debug=True)