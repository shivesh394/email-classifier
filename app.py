import streamlit as st 
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for t in text:
        if t.isalnum():
            y.append(t)
    text = y[:]
    y.clear()
    for t in text:
        if t not in stopwords.words('english') and t not in string.punctuation:
            y.append(t)
    text = y[:]
    y.clear()
    for t in text:
        y.append(ps.stem(t))
    return ' '.join(y)

ps = PorterStemmer()
tfid = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
st.title('SMS/Spam Classifier')
input_sms = st.text_area("Enter a message")
if st.button("predict"):
    transformed_sms = transform_text(input_sms)
    vector_input = tfid.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    print(result)
    if result == 1:
        st.header("Sapm")
    else:
        st.header("Not Spam")