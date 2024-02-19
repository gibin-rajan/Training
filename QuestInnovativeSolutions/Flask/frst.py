from flask import Flask
 
# class - 107 (13/06/2022)

app =Flask(__name__)

@app.route("/")
def hello():
    return 'Welcome to Flask'

# @app.route('/sc')     # instead of this we can use "app.add_url_rule('/sc','sc',second)" after the function
def second():
    return 'This is second function'

app.add_url_rule('/sc','sc',second)

@app.route('/nm/<name>')
def third(name):
    # return 'Your name is: %s'%name
    return 'Your name is: '+name





if __name__=='__main__':
    app.run(debug=True)
    
    
#app.run(host,portnumber, debug, options)
# 127.0.0.1-- host
# 5000 -- port number
# debug-flase
