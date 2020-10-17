import os
import logging
import json

logger = logging.getLogger('app')
logging.basicConfig(level=logging.WARNING)

if __name__ == "__main__":

  for k, v in sorted(os.environ.items()):
    logger.warning(k+':', str(v))
  
  print('Hello world')
