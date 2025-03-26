from pymongo.mongo_client import MongoClient

url = "mongodb+srv://arunkumr6006:arunkumr09@cluster0.ajnhqmn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(url)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)