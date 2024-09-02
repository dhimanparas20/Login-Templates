from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check credentials
        if username == 'anmol' and password == '12345':
            return redirect('https://www.youtube.com')
        else:
            flash('Invalid credentials. Please try again.', 'error')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
