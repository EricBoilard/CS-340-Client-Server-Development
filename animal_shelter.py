from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, aacuser1, aacuser2):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:52130/AAC' % (aacuser1, aacuser2))
        self.database = self.client['AAC']

    def create(self, data):
        # Checks to see if the data is null or empty and returns false in either case
        if data is not None:
            if data:
                self.database.animals.insert_one(data)
                return True
        else:
            return False

    def read(self, search):
        # Checks to see if the data is null or empty and returns exception in either case
        if search is not None:
            if search:
                searchResult = self.database.animals.find(search)
                return searchResult
        else:
            exception = "Nothing to search, because search parameter is empty"
            return exception
        
    def update(self, updateData):
        # Checks to see if the data is null or empty and returns exception in either case
        if updateData is not None:
            if updateData:
                updateResult = self.database.animals.update(updateData)
                return updateResult
        else:
            exception = "Nothing to delete, update parameter is empty"
        
    def delete(self, data):
        # Checks to see if the data is null or empty and returns exception in either case
        if data is not None:
            if data:
                deleteResult = self.database.animals.delete_one(data)
                return deleteResult
        else:
            exception = "Nothing to delete, delete parameter is empty"
            