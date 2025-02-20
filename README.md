Multi-Modal Image Retrieval System
This project implements a Multi-Modal Image Retrieval system that uses OpenAI's CLIP (Contrastive Language-Image Pretraining) model to search for images based on text queries. The backend is powered by Flask, and the frontend is built using React in Visual Studio Code (VS Code).
Features
Text-based Image Search: The system retrieves relevant images based on user input descriptions.
- Backend: Developed in Jupyter Notebook, processes the text query, compares it to precomputed image embeddings, and returns relevant images.
- Frontend: Built with React using VS Code, allows users to enter a query and displays top-k relevant images.

Prerequisites
Should have the below installed before starting.
- Python 3.x (f backend)
- Node.js (React frontend)
- pip (for installing Python packages)
- npm (for managing React dependencies)
- CUDA (for GPU acceleration, optional)
Installation

Backend Setup (Jupyter Notebook)
1. Clone the repository:
   git clone https://github.com/Siziphiwe24/Image-Retrieval/tree/main
   cd my-repository-folder

2. Navigate to the backend directory:
   cd backend

3. Install required Python dependencies:
   pip install -r requirements.txt

Frontend Setup (React in VS Code)
1. Navigate to the frontend directory:
   cd frontend
2. Install required Node.js dependencies:
   npm install
Backend Setup (Jupyter Notebook)

Run the code (MultiModalRetrieval) in Jupyter Notebook to generate image embeddings using the CLIP model

Frontend Setup (React in VS Code)
1. Run the code in image-retrieval folder
2. Open VS Code and navigate to the frontend directory.
3. Install Dependencies:
   npm install
4. Run the React App:
   npm start
6. Start the Backend:
   First, start the Flask API (as shown in the Backend Setup section).
   python app.py
7. Start the Frontend:
   Then, run the React app in a separate terminal:
   npm start
8. Access the App using th provided URL as an oupt.


