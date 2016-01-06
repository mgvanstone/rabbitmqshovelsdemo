
#!/usr/bin/env python
import pika
import sys

from flask import Flask, render_template, json, request
app = Flask(__name__)

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))
channel = connection.channel()
                         
channel.queue_declare(queue='wl_update_queue', durable=True)

def send(_id,_name):
	channel.basic_publish(exchange='',
        routing_key='wl_update2',
        body=str(_id+','+_name))
	print(" [x] Sent "+ _name)
	# connect:ion.close()
	return json.dumps({'html':'<span>All fields good !!</span>'})

@app.route("/")
def main():
    return render_template('index.html')
    
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')
    
@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _id = request.form['inputID']
    _name = request.form['inputName']
    _dob = request.form['inputDOB']
     
    # validate the received values
    if _name and _id:
        return send(_id,_name)
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()

