import importlib.util
import sys
import os

def load_so_module(path: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None:
        raise ImportError(f"Could not find module spec for {module_name}")
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise ImportError(f"Module {module_name} has no loader")
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
