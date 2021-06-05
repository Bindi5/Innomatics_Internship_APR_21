from flask import Flask, render_template, request, session, redirect, url_for
import random
import string
N = 7
app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return '<h3>Logged in as ' + username + '</h3>' + '<br>' + "<b><a href = '/inp_data'> Task Management System</a></b>" + "<br><b><a href = '/logout'>Click here to log out</a></b>"
    return "<h4>You are not logged in </h4><br><a href = '/login'>" + "Click here to log in</a>"
    


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'username' not in session:
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return '''

        <form action = "" method = "post">
            <p><input type = 'text' name = 'username' placeholder = 'Username'/></p>
            <p><input type = 'submit' value = 'Login'/></p>
        </form>	
        '''
    else:
        return redirect(url_for('index'))

    

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


notes = []

@app.route('/inp_data', methods=["GET", "POST"])
def inp_data():
    # notes = []   
    if 'username' in session: 
        if request.method == 'POST':
            if request.form.get('note'):
                note = request.form.get("note")
                notes.extend([session['username'], note])
            print(notes)
    else:
        return redirect(url_for('index'))

    return render_template("home.html", notes=notes, k=session['username'])

if __name__ == '__main__':
    app.run(debug=True)