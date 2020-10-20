from tornado import websocket
from tornado.ioloop import PeriodicCallback

import uuid, json , urllib
import base64
import time

import logging
logger = logging.getLogger('socket')

class API(websocket.WebSocketHandler):
	
	clients = set()

	def check_origin(self, origin):
		return True
	
	async def open(self,channel=''):
		
		self.id = uuid.uuid4()
		API.clients.add(self)

		outbound = {'alert':{'success':'Connected as '+str(self.id)}}

		self.callback = PeriodicCallback(lambda : self.track(),10*1000)
		self.callback.start()

		await self.broadcast({'alert':{'info':'Welcome '+str(self.id)}})
		self.write_message(outbound)

	def on_close(self):
				
		self.callback.stop()
		API.clients.remove(self)

	async def track(self):
		
		data = str(self.id)
		outbound = {'alert':{'info':data}}
		self.write_message(outbound)

	async def on_message(self,inbound={}):

		outbound=json.loads(inbound)
		self.write_message(json.dumps(outbound))
				
	async def broadcast(self,outbound={}):
		
		for client in self.clients:
			if not client.id == self.id:
				try:
					logging.info("broadcast" + str(outbound))
					client.write_message(outbound)
				except:
					logging.error("Error sending message")
