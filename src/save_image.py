
import os 
from src.model import MyModel
from src.chroma_db import MyDb
#from logging import logger 
from PIL import Image

class Store_img():
    def __init__(self,dataset_path,collection):
        self.model=MyModel()
        self.db=MyDb(dataset_path,collection)
        self.collection=self.db.collection
        self.dataset_path=dataset_path
        

        

    
    def process_dataset_and_store_embeddings(self, dataset_path):
        for root, _, files in os.walk(dataset_path):
            label = os.path.basename(root)  # Folder name as label
            for idx, file in enumerate(files):
                image_path = os.path.join(root, file)
                embedding = self.image_to_embedding(Image.open(image_path).convert('RGB'))
                image_id = f"{label}_{idx+1}"
                self.store_embedding(embedding, image_id, label, image_path)
                print(f"Stored embedding for {file} with ID: {image_id} and label: {label}")
    
    def compare_image(self, image):
        input_embedding = self.model.image_to_embedding(image)
        print(input_embedding)
        results = self.collection.query(query_embeddings=[input_embedding], n_results=1)  # Get the closest match
        print(results)
        if results['metadatas']:
            closest_metadata = results['metadatas'][0][0]
            return closest_metadata['label'], closest_metadata['image_path']
        return "No match found", None

