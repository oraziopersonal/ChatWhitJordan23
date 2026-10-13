import pymongo  # type: ignore[reportMissingImports]

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
