import time

query = [
	"""curl --header "Content-Type: application/json" --request POST --data '{"access":"0","start_time":""",
	  ""","endtime":""",
	  ""","place":"73f8413e-1918-11eb-ab52-00155d3c2f56","controlplace":0,"zone":"Холл в центре завода","activezone":0,"videostream":"0","videostreamid":"fad1d66d-0c81-11eb-8133-00155d3c2b05","regulationid":"00000000-0c81-11eb-8133-00155d3c2b05","objective":"00000000-f41c-11ea-a41e-4cedfb43b7af","bodyguard":["helmet"],"active":1,"pointx":0,"pointy":0,"width":0,"height":0,"departmentid":"54dfb77b-bcfa-11e9-ab42-00155d3c2f56","organizationid":"327dd46a-8819-11e9-a060-d0c637a676fa","is_empty":0}' http://0.0.0.0:5001/api"""
]

print(query[0], int(time.time() + 10), query[1], int(time.time() + 300), query[2], sep='')
