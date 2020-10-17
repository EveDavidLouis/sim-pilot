import os
import logging
import json

from tornado import ioloop , gen , web
from motor.motor_tornado import MotorClient
from server import config
from server.handlers import webHandler

logger = logging.getLogger('app')
logging.basicConfig(level=logging.WARNING)

if __name__ == "__main__":
  
  for c in config.server:
    print(str(c))
