
from src.chroma_db import MyDb
from src.model import MyModel
from logging import logger

class Comapre():
    def __init__(self):
        self.model=MyModel()
        self.db=MyDb()
        self.collection=self.db.collection
        
            
     
    
    



    def compare_image(self, input_image_path):
        input_embedding = self.model.image_to_embedding( input_image_path)
        results = self.collection.query(query_embeddings=[input_embedding], n_results=1)  # Get the closest match
        logger.info("comparison between the images is completed")
        return results