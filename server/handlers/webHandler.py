import json, os
from tornado import web

class BaseHandler(web.RequestHandler):

	async def get(self, *args, **kwargs):
		#self.render('../../docs/index.html')
		#self.redirect('./index.html')
		f = open("./docs/index.html", "r")
		self.write(f.read())
		self.finish()

class RedditBrowser(web.RequestHandler):
	async def get(self, *args, **kwargs):

		fe = self.settings['fe']

		url = 'https://www.reddit.com/r/'+args[0][1:]+'/new.json'
		headers = {}
		chunk = { 'kwargs':{'method':'GET', 'headers':headers } , 'url':url }
		response = await fe.asyncFetch(chunk)
		size = '400'
		payload = ''
		if response.code == 200:
			dataSet = (json.loads(response.body.decode()))
			for d in dataSet['data']['children']:
				if 'content' in d['data']['secure_media_embed']:
					payload += '<iframe  width="'+size+'" height="'+size+'" src="'+d['data']['secure_media_embed']['media_domain_url']+'"></iframe>'
				else :
					payload += ('<img src="'+d['data']['url']+'" width="'+size+'" height="'+size+'"></img>')
	
		self.write(str(payload))