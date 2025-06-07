import importlib.util
import sys

def load_extension_module(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module

# usage
module_path = "rust_lib/rust_lib.so"
mymodule = load_extension_module(module_path, "rust_lib")

# now you can use mymodule as usual
print(mymodule.hello_world())
