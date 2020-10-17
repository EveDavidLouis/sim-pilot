import os
import logging
import json

from server import config

logger = logging.getLogger('app')
logging.basicConfig(level=logging.WARNING)

if __name__ == "__main__":
  
  for c in config:
    print(str(c))
