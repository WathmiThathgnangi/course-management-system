from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('login.html')

# Route for the course page
@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)