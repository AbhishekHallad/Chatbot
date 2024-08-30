from flask import Flask , render_template , request

import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pharma')
def pharma():
    return render_template('pharma.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    user_input = request.form['user_input']

    pickle_in = open("model.pickle","rb")
    model = pickle.load(pickle_in)

    data = user_input.split(",")
    pickle_in = open("array.pickle","rb")
    input_vector = pickle.load(pickle_in)
    

    pickle_in = open("dict.pickle","rb")
    symptoms_dict = pickle.load(pickle_in)

    a = symptoms_dict[data[0]]
    b = symptoms_dict[data[1]]
    c = symptoms_dict[data[2]]

    input_vector[[a, b, c]] = 1

    prediction = model.predict([input_vector])

    output = prediction

    return render_template('index.html', user_input=user_input, prediction_text='Most likely you have {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
