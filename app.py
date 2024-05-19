from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import pickle
import string
import nltk
from nltk.stem import PorterStemmer
import mysql.connector
from sklearn.exceptions import NotFittedError
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pandas as pd
from nltk.corpus import stopwords

app = Flask(__name__)
app.secret_key = '1c8073775dbc85a92ce20ebd44fd6a4fd832078f59ef16ec'  # Replace with a secure secret key

ps = PorterStemmer()

def transform_text(text):
    text = str(text).lower() # Converting to lowercase
    text = nltk.word_tokenize(text)  # Tokenizing the text.
    # Removing special characters and retaining alphanumeric words.
    text = [word for word in text if word.isalnum()]
    # Removing stopwords and punctuation
    text = [word for word in text if word not in stopwords.words('english') and word not in string.punctuation]
    # Applying stemming
    text = [ps.stem(word) for word in text]
    
    return " ".join(text)


# @app.route('/train', methods=['POST'])
# def train():
#     global vect, model, model_trained

#     # Load and preprocess data
#     data = pd.read_csv('spam.csv')  # Ensure this path is correct
#     X = data['message']
#     y = data['label']

#     # Transform and train the model
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     X_train_transformed = vect.fit_transform(X_train)
#     model.fit(X_train_transformed, y_train)
#     model_trained = True

#     # Save the trained model and vectorizer
#     pickle.dump(vect, open('vectorizer1.pkl', 'wb'))
#     pickle.dump(model, open('model.pkl', 'wb'))

#     return "Model trained successfully!"

# Load vectorizer and model from pickle files if they exist


# Define your database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SAI#01kmmhyd",
    database="mysql"
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    # Check if the 'user' session variable exists (i.e., the user is logged in)
    if 'user' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('signin'))  # Redirect to the sign-in page if the user is not logged in
    
    
vect = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))    

@app.route('/predict', methods=['POST'])
def predict():
    input_sms = request.form.get('message')
    transformed_sms = transform_text(input_sms)
    vector_input = vect.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    prediction = "Spam" if result == 1 else "Not Spam"
    return render_template('result.html', prediction=prediction)

@app.route('/signin')
def signin():
    if 'user' in session:
        return redirect(url_for('index'))
    return render_template('signin.html')

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        # Ensure the password and confirm_password match
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            return "Password and Confirm Password do not match."

        # Insert data into MySQL
        cur = db.cursor()
        cur.execute("INSERT INTO users (full_name, username, email, phone, password) VALUES (%s, %s, %s, %s, %s)",
                    (full_name, username, email, phone, password))
        db.commit()
        cur.close()

        flash('Registration successful', 'success')
        return redirect('/signin')

    return "Invalid request method"

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember_me = request.form.get('remember_me')  # Get the 'remember_me' checkbox value

        # Query the database to check if the email and password match
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()

        if user:
            session['user'] = user

            if remember_me:
                session.permanent = True
            return redirect(url_for('index'))
        else:
            return "Login failed. Check your email and password."

    return "Invalid request method"

@app.route('/logout')
def logout():
    # Clear the user session to log out
    session.pop('user', None)
    return redirect(url_for('home'))  # Redirect to the sign-in page after logging out

if __name__ == '__main__':
    app.run(debug=True)
