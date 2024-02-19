from flask import *

# class - 109 

app= Flask(__name__)

@app.route("/postdata",methods=['POST'])
def login():
    un=request.form['uname']
    ps=request.form['pass']
    if un=='admin' and ps=='admin':
        return "Welcome "+un
    return "Not Worked"


@app.route("/getdata",methods=['GET'])
def log():
    un=request.args.get('uname')
    ps=request.args.get('pass')
    if un=='admin' and ps=='admin':
        return "Welcome "+un
    return "Not Worked"


@app.route("/disp")
def display():
    return render_template('thrd.html')


if __name__=='__main__':
    app.run(debug=True)