import logging
from examples.hello_world import RustModule

logging.basicConfig(level=logging.INFO, format='[%(levelname)s | %(name)s %(filename)s:%(lineno)d] %(asctime)-15s %(message)s')
RustModule.hello_world()