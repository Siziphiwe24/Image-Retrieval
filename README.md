                                                         Mutli-Modal-Image-Retrieval
                                                         
This project implements a simple image search functionality using OpenAI's CLIP model, FAISS, and a dataset of images. It processes and computes image embeddings using CLIP, stores them in a FAISS index, and allows querying for similar images based on a text input. The app uses Jupyter widgets to create an interactive UI.

Requirements
Before running the project, you need to install the required libraries. You can do this by running:

pip install torch torchvision transformers faiss-cpu pillow ipywidgets matplotlib

Setup
1. Load the CLIP model: The project uses the pre-trained CLIP model from OpenAI's model hub to convert images and text into embeddings for similarity matching.
2. Image Preprocessing: The images are preprocessed using the CLIP processor and converted into embeddings.
3. FAISS Indexing: After generating embeddings, the images are indexed in a FAISS index to enable efficient similarity search.
4. Search Functionality: Users can enter a text description (e.g., "A Food" or "Hous") into a search box, and the system will return the top-k most similar images from the dataset.
Steps
- Download the uploaded Jupyter Notebook File
Running the Application
1. Ensure that your images are placed in the directory specified by `IMAGE_DIR`.
2. Run the script in a Jupyter notebook or IPython environment.
3. Enter a text query in the input box, click the 'Search' button, and view the top-k most relevant images displayed.
Notes
- This implementation works in environments with GPU support (CUDA). If not, it will default to CPU.
- You can adjust the number of top results displayed by changing the `top_k` parameter in the `search_images()` function.
- The dataset is limited to 500 images by default. You can modify the line:
  
image_paths = image_paths[:500]

to include more images if desired.



