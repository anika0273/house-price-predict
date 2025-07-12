# House Price Predictor: From Script to System with Docker 🚀

Welcome! This project demonstrates how to turn a simple machine learning model into a full containerized system with a REST API and a user-friendly frontend.  
It uses **FastAPI** for the backend API, **Streamlit** for the frontend UI, and **Docker Compose** to orchestrate everything.

---

## Why This Project?

Building ML models is exciting, but deploying them as reliable, shareable systems is where the real-world magic happens.  
This project is **not** about squeezing out the best accuracy — it’s about learning how to package, deploy, and run ML apps in a reproducible and scalable way.

---

## What’s Inside?

- A simple Random Forest regression model trained on the California Housing dataset.
- A FastAPI backend that loads the model and serves prediction requests.
- A Streamlit frontend UI for easy user interaction.
- Dockerfiles for backend and frontend.
- A Docker Compose file to run the entire system with one command.

---

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running
- [Git](https://git-scm.com/downloads) installed
- (Optional) [Git LFS](https://git-lfs.github.com/) installed to handle the large model file

---

### Clone the Repository

git clone https://github.com/anika0273/house-price-predict.git
cd house-price-predict

If you don’t have Git LFS installed, you can install it following instructions [here](https://git-lfs.github.com/).

1. # For macOS using Homebrew
   brew install git-lfs
2. # Initialize Git LFS in your repository
   git lfs install
3. # Track your large model file
   git lfs track "models/\*.joblib"
4. # Commit the .gitattributes file and your model file again. Because Git LFS replaces the file pointer
   git add .gitattributes
   git add models/house_price_model.joblib
   git commit -m "Track large model file with Git LFS"

---

### Run the Application with Docker Compose

Build and start the backend and frontend containers:

docker-compose up --build

This command will:

- Build Docker images for the backend and frontend
- Start the FastAPI backend on port `8000`
- Start the Streamlit frontend on port `8501`

---

### Access the Application

- **Streamlit UI:** Open [http://localhost:8501](http://localhost:8501) in your browser
- **FastAPI Swagger docs:** Open [http://localhost:8000/docs](http://localhost:8000/docs) to explore the API endpoints interactively

---

## How It Works

1. **Train the Model:**  
   The model is trained on the California Housing dataset using a Random Forest regressor and saved as a `.joblib` file (`models/house_price_model.joblib`).

2. **Backend API:**  
   The FastAPI app loads the saved model and exposes a `/predict` endpoint that accepts feature inputs and returns predictions.

3. **Frontend UI:**  
   The Streamlit app provides a simple form for users to input house features and get price predictions by calling the backend API.

4. **Dockerization:**  
   Both backend and frontend are containerized with Docker, and Docker Compose manages running them together with proper networking.

---

## Troubleshooting & Tips

| Issue                                  | Solution                                                                              |
| -------------------------------------- | ------------------------------------------------------------------------------------- |
| Ports 8000 or 8501 already in use      | Find and kill the process: `lsof -i :8000` or `lsof -i :8501`, then `kill -9 <PID>`   |
| Streamlit frontend can’t reach backend | Use `http://backend:8000` (Docker service name) inside the frontend, not `localhost`  |
| Changes not reflected after rebuild    | Run `docker-compose down` then `docker-compose up --build`                            |
| Model file too large to push to GitHub | Use [Git LFS](https://git-lfs.github.com/) to track large files (already set up here) |

---

## Project Structure

house-price-predictor/
├── api/ # FastAPI backend code + Dockerfile
├── frontend/ # Streamlit frontend code + Dockerfile
├── ml_models/ # Model training script
├── models/ # Saved model file (.joblib)
├── requirements.txt # Python dependencies for backend & frontend
├── docker-compose.yml # Docker Compose configuration
├── .gitattributes # Git LFS tracking config
└── README.md # This file

text

---

## Next Steps (Coming Soon!)

- Add Continuous Integration / Continuous Deployment (CI/CD) pipelines
- Integrate MLflow for experiment tracking
- Automate model retraining with Apache Airflow
- Add monitoring with Prometheus or EvidentlyAI

---

## Contributing

Feel free to open issues or submit pull requests!  
If you find bugs or want to add features, I’d love your help.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Contact

Created by Anika — [GitHub Profile](https://github.com/anika0273)  
Questions? Feedback? Reach out or open an issue!

---

**Happy building!** 👩‍💻
