
# To-Do CLI Application – CI/CD Pipeline using Jenkins & Docker

This repository contains a **To-Do List Command Line Application** implemented in Python, fully automated using a **Jenkins CI/CD Pipeline** that:

- Pulls source code from GitHub  
- Installs dependencies using a virtual environment  
- Runs automated tests using pytest  
- Builds a Docker image  
- Pushes the image to Docker Hub  

This project was created as part of a Software Engineering CI/CD assignment.

---

## 📌 Features of the To-Do CLI App

The To-Do application supports:

- Add a task  
- List all tasks  
- Mark a task as done  
- Delete a task  
- Persistent storage using a JSON file (`todos.json`)

### 🟦 Example Commands

```
python app.py add "Buy groceries"
python app.py list
python app.py done 1
python app.py delete 1
```

---

## 📁 Project Structure

```
.
├── app.py              # To-Do CLI main application
├── test_app.py         # Automated tests using pytest
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build configuration
└── Jenkinsfile         # Jenkins CI/CD pipeline script
```

---

## 🚀 CI/CD Pipeline (Jenkins)

The Jenkinsfile automates the entire workflow:

### 1️⃣ **Checkout Code**
Pulls the latest version from GitHub.

### 2️⃣ **Create Python Virtual Environment**
```
python3 -m venv venv
```

### 3️⃣ **Install Dependencies**
Uses the venv to install packages from requirements.txt.

### 4️⃣ **Run Tests**
Automated unit tests using PyTest.

### 5️⃣ **Build Docker Image**
Jenkins builds the Docker image using:

```
docker build -t <dockerhub_username>/<repo>:<tag> .
```

### 6️⃣ **Push to Docker Hub**
Authenticated push to your Docker Hub repository.

---

## 🐳 Docker Usage

After Jenkins pushes the image, you can pull and run it:

### Pull the image
```
docker pull svnsaisathvik/imt2023001:<tag>
```

### Run the application
```
docker run svnsaisathvik/imt2023001:<tag> list
```

---

## 🛠 Technologies Used

- **Python 3.12**
- **PyTest**
- **Docker**
- **Jenkins**
- **Git/GitHub**

---

## 📦 Installation (Manual Run Without Docker)

### 1. Clone the repository
```
git clone https://github.com/svnsaisathvik/TO-DO-CLI.git
cd TO-DO-CLI
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the app
```
python app.py add "Task example"
python app.py list
```

---

## 🧪 Running Tests

```
pytest -q
```

---

## 🙌 Author

**SVN Sai Sathvik**  
IIIT Bangalore  
Roll Number: **IMT2023001**

---

## 📄 License

This project is for educational purposes only.
