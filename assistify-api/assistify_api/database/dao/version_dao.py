from fastapi import Depends
from pymongo.database import Database

from ..dao.dao import Dao
from ..mongodb import MongoDb


class VersionDao(Dao):
    def __init__(self, db: Database = Depends(MongoDb.instance)):
        super().__init__(db, collection="version")
