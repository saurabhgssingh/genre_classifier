from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask import Flask, render_template, request
import pickle
from tensorflow import keras
from sklearn.preprocessing import MultiLabelBinarizer
from clean_text import clean_text
import numpy as np
cleaner = clean_text()

embedding_dim = 100
max_length = 200
trunc_type='post'
padding_type='post'


# Load tect cleaner
#with open('cleaner.pickle', 'rb') as handle:
#   clean = pickle.load(handle)
   
#load tokenizer
with open('tokenizer.pickle', 'rb') as handle:
   tokenizer = pickle.load(handle)
   
#load multilabel binarizer
with open('binarizer.pickle', 'rb') as handle:
   binarizer = pickle.load(handle)
   
#load model
model = keras.models.load_model("model_glove.h5")

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        sent = cleaner.do_all(message)
        tokens = tokenizer.texts_to_sequences([sent])
        pad = pad_sequences(tokens,  maxlen=max_length, padding=padding_type, truncating=trunc_type)
        x = model.predict(pad)
        prediction = binarizer.inverse_transform((x>0.2).astype(np.int))
        return render_template('result.html', result=str(prediction)[2:-2])

if __name__ == '__main__':
	app.run(debug=True)
