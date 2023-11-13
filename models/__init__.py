#!/usr/bin/python3
"""Creates unique FilesStorage instance"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
