import json , os
from tornado import web , gen

class DefaultHTMLHandler(web.RequestHandler):

	async def get(self, *args, **kwargs):
		data = {'DefaultHTMLHandler':args}
		self.write(str(data))
		self.finish()

class DefaultJSONHandler(web.RequestHandler):

	async def get(self, *args, **kwargs):
		data = {'DefaultJSONHandler':args}
		for v in os.environ:
			data[v]=os.environ[v]
		self.write(json.dumps(data))
		self.finish()

class AuthHandler(web.RequestHandler):

	async def get(self,args):
		data_post = {
			'username': '',
			'password': ''
		}
		check = 1
		if check:
			authToken = '123'
			self.write(json.dumps({'authToken':authToken}))
		else:
			self.write(json.dumps({'status':'denied'}))
		self.finish()
		
class DbTestHandler(web.RequestHandler):

	async def get(self,args):

		collection = self.settings['db']['pilots']
		cursor = collection.find({},{'_id':0})
		document = await cursor.to_list(length=10000)

		collection = self.settings['db']['airports']
		document = await collection.find_one({},{'_id':0})

		self.write(json.dumps(document))
		self.finish()

	async def loadJSON(self):
		
		with open('./file.json', encoding="utf8") as f:
			file_data = json.load(f)

		collection = self.settings['db']['import']
		result = await collection.insert_many([{
			'_id':i,
			'icao':file_data[i]['icao'],
			'iata':file_data[i]['iata'],
			'name':file_data[i]['name'],
			'city':file_data[i]['city'],
			'state':file_data[i]['state'],
			'country':file_data[i]['country'],
			'elevation':file_data[i]['elevation'],
			'lat':file_data[i]['lat'],
			'lon':file_data[i]['lon'],
			'tz':file_data[i]['tz']
			} for i in file_data])
