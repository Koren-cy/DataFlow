"""Top-level package for dataflow."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """Koren"""
__email__ = "koren.cai.cy@gmail.com"
__version__ = "0.0.1"

from .src.dataflow.nodes import NODE_CLASS_MAPPINGS
from .src.dataflow.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
