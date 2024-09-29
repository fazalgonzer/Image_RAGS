

import chromadb
#from logging import logger
from chromadb.config import Settings


 # Empties and completely resets the database. ⚠️ This is destructive and not reversible.



class MyDb():
    def __init__(self,db_path,collection_name):
    
        settings = Settings(persist_directory=db_path)

        self.client = chromadb.Client(settings=settings)
        self.collection = self.client.get_or_create_collection(collection_name)
#        logger.info("INtilization of DB is completed")

# 4. Store Image Embedding in ChromaDB
    def store_embedding(self, embedding, image_id, label, image_path):
        self.collection.add(embeddings=[embedding], ids=[image_id], metadatas=[{'label': label, 'image_path': image_path}])