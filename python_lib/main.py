import logging
from rust_lib import RustModule

logging.basicConfig(level=logging.INFO)
RustModule.hello_world()