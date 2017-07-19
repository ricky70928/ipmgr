from pymongo import MongoClient
import datetime

import pprint
from bson.objectid import ObjectId

from setting import *

class database(setting):
    def __init__(self, DBInfo):
        #self.DBINFO = DBInfo.getDBInfo
        self.HOST = DBInfo.getDBInfo()[0]
        self.PORT = DBInfo.getDBInfo()[1]
        self.DBNAME  = DBInfo.getDBInfo()[2]
        self.COLNAME = DBInfo.getDBInfo()[3]
        self.CMD = DBInfo.getDBInfo()[4]
        
    def connectDB(self):
        self.MCLIENT = MongoClient(self.HOST, self.PORT)
        self.MDB = self.MCLIENT[self.DBNAME]
        self.MCOL = self.MDB[self.COLNAME] 

    def setDocData(self, CLIENTINFO):
        self.CMD = {
            "time": datetime.datetime.utcnow(),
            "hostname": CLIENTINFO[0],
            "ipaddr": CLIENTINFO[1],
            "macaddr": CLIENTINFO[2]
        }

    def getDocData(self):
        return self.CMD
    
    def insertDoc(self):
        RESULT = self.MCOL.insert_one(self.CMD)
        ID = RESULT.inserted_id
        if self.searchDoc('_id', ID) == 1:
            return 0
        else:
            return 1

    def removeDoc(self, OPTION, VALUE):
        RESULT = self.MCOL.delete_one({OPTION: VALUE})
        if RESULT.deleted_count == 1:
            return 0
        else:
            return 1

    def modifyDoc(self, OPTION, VALUE, NEWVALUE):
        RESULT = self.MCOL.update_one({OPTION: VALUE}, {'$set': {OPTION: NEWVALUE}})
        if RESULT.matched_count == 1 and RESULT.modified_count == 1:
            return 0
        else:
            return 1

    def searchDoc(self, OPTION, VALUE):
        RESULT = self.MCOL.count({OPTION: VALUE})
        if RESULT == 0:
            return 1
        else:
            return 0
