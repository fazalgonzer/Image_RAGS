from flask import Flask, request, render_template, redirect
from PIL import Image
import os
from src.save_image import Store_img

# Configuration
db_path = "Chroma_path"
collection_name = "image_embeddings"
dataset_path = "artifacts/data"  # Path to your dataset containing 4 cat categories

# Initialize Store_img instance
st = Store_img(db_path, collection_name)
# Uncomment the following line if you want to initialize a new collection
# st.process_dataset_and_store_embeddings(dataset_path)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    # Check file extension
    if file and file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Save the uploaded file temporarily
        temp_file_path = os.path.join('temp', file.filename)
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
        file.save(temp_file_path)

        # Open the image and process it
        test_image = Image.open(temp_file_path).convert('RGB')
        label, closest_image_path = st.compare_image(test_image)

        # Remove the temporary file
        os.remove(temp_file_path)

        # Return the result page with the label and image path
        return render_template('result.html', label=label, image_path=closest_image_path)
    
    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)
