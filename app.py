from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import torch
import faiss
import numpy as np
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import os
import pickle

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Set image directory
IMAGE_DIR = r"C:\Users\phiwe\Downloads\test_data_v2"

# Load precomputed image embeddings
EMBEDDINGS_FILE = "image_embeddings.pkl"

if os.path.exists(EMBEDDINGS_FILE):
    with open(EMBEDDINGS_FILE, "rb") as f:
        image_embeddings = pickle.load(f)
else:
    image_embeddings = np.array([])

# Initialize FAISS index
if isinstance(image_embeddings, np.ndarray) and image_embeddings.size > 0:
    index = faiss.IndexFlatL2(image_embeddings.shape[1])
    index.add(image_embeddings.astype(np.float32))
else:
    index = faiss.IndexFlatL2(512)  # Assuming CLIP outputs 512-dimensional embeddings

# Store only filenames (not full paths)
image_paths = [os.path.basename(path) for path in os.listdir(IMAGE_DIR) if path.endswith((".jpg", ".png"))]

def preprocess_image(image_path):
    """Preprocess an image for CLIP model"""
    image = Image.open(image_path).convert("RGB")
    return processor(images=image, return_tensors="pt")["pixel_values"].to(device)

def encode_text(text):
    """Generate embedding from text using CLIP"""
    inputs = processor(text=[text], return_tensors="pt", padding=True)
    with torch.no_grad():
        text_embedding = model.get_text_features(**inputs).cpu().numpy()
    return text_embedding

@app.route('/search', methods=['POST'])
def search():
    """Search for images based on text or embedding"""
    data = request.get_json()

    if "query_text" in data:
        query_embedding = encode_text(data["query_text"])
    elif "query_embedding" in data:
        query_embedding = np.array(data["query_embedding"]).astype(np.float32).reshape(1, -1)
    else:
        return jsonify({"error": "Provide 'query_text' or 'query_embedding'"}), 400

    if query_embedding.shape[1] != index.d:
        return jsonify({"error": "Invalid embedding dimension"}), 400

    D, I = index.search(query_embedding, k=5)
    results = [{"path": image_paths[i], "distance": float(D[0][idx])} for idx, i in enumerate(I[0]) if i < len(image_paths)]

    return jsonify({"results": results})

@app.route('/images/<path:image_name>')
def serve_image(image_name):
    """Serve images from IMAGE_DIR"""
    return send_from_directory(IMAGE_DIR, image_name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

