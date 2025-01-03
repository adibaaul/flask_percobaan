from flask import Flask, redirect, url_for, request, render_template
import pickle

app= Flask(__name__)

model_file = open('model_asuransi.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route("/")
def index():
    return render_template("index.html", insurance_cost=0)

@app.route('/predict', methods=['POST'])

def predict():
    age, sex, smoker = [x for x in request.form.values()]
    data = []
    data.append(int(age))
    if sex == 'Laki-laki':
        data.extend([0,1])
    else:
        data.extend([1,0])
    if smoker == 'Ya':
        data.extend([0,1])
    else:
        data.extend([1,0])
    prediction = model.predict([data])
    output = round(prediction[0], 2)
    return render_template('index.html', insurance_cost=output, age=age, sex=sex, smoker=smoker)

if (__name__=="__main__"):
    app.run(debug=True)

if(__name__=="__main__"):
    app.run(debug=True)