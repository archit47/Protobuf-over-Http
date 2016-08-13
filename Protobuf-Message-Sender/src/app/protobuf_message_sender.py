from protobuf import Employee_pb2
import requests

employee_details = Employee_pb2.Employee()


employee_details.name="Archit Kapoor"
employee_details.email="xyz@gmail.com"
employee_details.id=201

print employee_details

#if employee_details.HasField('isBOEmployee'):
#	print employee_details.isBOEmployee

print employee_details.isBOEmployee



url = "http://localhost:8000"
headers = {'Content-Type': 'application/x-protobuf', 'Accept': 'application/x-protobuf'}

try:
	ses = requests.Session()
	ses.headers.update(headers)
	resp = ses.post(url, data=employee_details.SerializeToString())

	print "Status Code of the response: " , resp.status_code
	print "Response from Python-Service ", resp

except Exception as err:
	print "Some error has occurred while sending the message"
	print err