from flask import Flask, redirect, session, render_template
app = Flask(__name__)
app.secret_key = "passw0rd"
@app.route("/")
def counter():
    session['count'] = 0
    if 'count' in session:
        print("KEY EXIST")
    else:
        print("key 'count' does NOT exist")
    return redirect("/show")
@app.route("/show")
def show_page():
    session['count']+=1
    return render_template("index.html")
@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")
@app.route("/bytwo")
def by_two():
    session['count']+=2
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)