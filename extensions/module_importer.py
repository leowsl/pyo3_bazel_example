# This is the __init__.py file that goes with the pyo3 library to ensure correct loading of the modules
import importlib.util
import sys
import os
import glob
import logging

# Configure logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s | %(name)s] %(asctime)s %(message)s', datefmt='%H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

def find_so_files()->list[str]:
    """Find all .so files in the current directory"""

    current_dir = os.path.dirname(os.path.abspath(__file__))
    return glob.glob(os.path.join(current_dir, "*.so"))

def load_so_module(path: str, module_name: str):
    """Load a .so file into this module's namespace"""

    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None:
        raise ImportError("Could not find module spec for" + module_name)
    
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise ImportError("Module " + module_name + " has no loader")
    spec.loader.exec_module(module)

    # Register the module in the current module's namespace
    sys.modules[__name__].__dict__[module_name] = module

# Load all the .so files in the current directory
for so_file_path in find_so_files():
    module_name = os.path.splitext(os.path.basename(so_file_path))[0]
    try:
        load_so_module(so_file_path, module_name)
        logger.debug(f"Successfully loaded PyO3 module: {module_name}")
    except Exception as e:
        logger.error(f"Failed to load PyO3 module: {module_name}: {str(e)}")
        continue