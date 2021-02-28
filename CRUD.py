from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:38152/AAC?authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    # Inserts a new document into the database as specified in the "data" parameter"
    def create(self, data):
        if data is not None:
            return self.database.animals.insert(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Reads the document specifed by the lookup pairs in the "query" parameter
    def read(self, query):
        if query is None:
            raise Exception("Must define parameters for your query")
        else:
            return self.database.animals.find_one(query) # query is the parameters for the find

    # Dumps all of the data from the database
    def read_all(self, data):
        return self.database.animals.find(data, {"_id":False})

    # Updates the document specified by the key/value pair in the "lookup" parameter. The "values"
    # parameter must contain the appropriate mongo update operator expressions (i.e. {$set: {key: "value}})
    def update(self, lookup, values):
        if lookup is None:
            raise Exception("Must provide the key/value pair for the document you wish to update!")
        elif values is None:
            raise Exception("Must provide updated values!")
        else:
            return self.database.animals.update_one(lookup, values)
        
    # Deletes the document specified by the key/value pair in the "lookup" parameter.
    def delete(self, lookup):
        if lookup is None:
            raise Exception("Must provide the key/value pair for the document you wish to delete!")
        else:
            return self.database.animals.delete_one(lookup)