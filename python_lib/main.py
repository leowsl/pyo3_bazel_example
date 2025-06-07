# Uses sys.modules
from python_lib.importer import load_so_module
load_so_module(
    path="rust_lib/rust_module.so",
    module_name="RustModule",
)

import RustModule
RustModule.hello_world()