import numpy as np
from flask import Flask, request, jsonify, render_template
import fasttext

app = Flask(__name__)
model = fasttext.load_model('Fasttextmodel.bin')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    description = [x for x in request.form.values()]
    prediction = model.predict(description)

    group = str(prediction[0]) [12:-3]
    output = float(prediction[1][0])
    
    if output > 0.80:
        return render_template('index.html', prediction_text='Ticket is Assigned to {} Thanks.'.format(group),score ='Score : {:.4f}'.format(output ))
    else:
        return render_template('index.html', prediction_text='Our team is reviewing your ticket. Group will be assigned shortly. Thanks',score ='Score : {:.4f}'.format(output ))


if __name__ == "__main__":
    app.run(debug=True)