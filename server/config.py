import os
import json
import base64

#server
server = dict(
	host 			= os.environ.get('SERVER_HOST','0.0.0.0')
	,port 			= int(os.environ.get('SERVER_PORT',8081))
	,secret 		= os.environ.get('SERVER_SECRET','asecrect')
)
if os.environ.get('PORT'): server['port'] = int(os.environ.get('PORT'))

#mongodb
mongodb = dict(
	host 		= os.environ.get('MONGO_HOST','localhost')
	,port 		= int(os.environ.get('MONGO_PORT',27017))
	,user 		= os.environ.get('MONGO_USER','admin')
	,pwd 		= os.environ.get('MONGO_PWD','1234')
	,db 		= os.environ.get('MONGO_DB','test')
)
mongodb['url'] = 'mongodb://'+mongodb['user']+':'+ mongodb['pwd'] +'@'+str(mongodb['host'])+':'+str(mongodb['port']) +'/' + mongodb['db'] 
