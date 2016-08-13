from flask import Flask, request
from message.protobuf import Employee_pb2

empl = Employee_pb2.Employee()

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def hello():
	try:
	
		if request.headers['Content-Type'] == 'application/x-protobuf':
			empl.ParseFromString(request.stream.read())
			print "Request message received is a Protobuf"

			print empl

			return "Protobuf Message Received"

		else:
			print "Request message received is not a protobuf"
			print "Content-type :", request.headers['Content-Type']
			print "Request body :", request.data
			return "Message Received but it was not a protocol buffer"

	except Exception as err:
		print "Some exception has occurred"
		print err
		return "Server could not process the message"
		


if __name__ == "__main__":
    app.run(port=8000)