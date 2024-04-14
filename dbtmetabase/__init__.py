import logging

from .core import DbtMetabase
from .format import Filter
from ._models import ModelDescription

__all__ = [
    "DbtMetabase",
    "Filter",
    "ModelDescription"
]

try:
    from ._version import __version__ as version  # type: ignore

    __version__ = version
except ModuleNotFoundError:
    logging.warning("No _version.py file")
    __version__ = "0.0.0"
