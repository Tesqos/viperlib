import logging

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.addHandler(console)

from .src import misc as misc
from .src import vtime as vtime
from .src.jsd import jsondata as jsondata
