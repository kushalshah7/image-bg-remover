# **Image Background Remover 🎨🖼️**  

An AI-powered image background removal tool using FastAPI and Streamlit. The backend processes images using `rembg`, while the frontend provides an intuitive interface for users to upload and remove backgrounds from images.  

## **Features**  
✅ FastAPI-based backend for efficient image processing  
✅ Streamlit frontend for user-friendly interaction  
✅ Uses `rembg` for background removal  
✅ Supports various image formats  

---


### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## **Running the Project**  

### **🚀 Start the Backend (FastAPI)**  
Run the FastAPI server:  
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
Once running, visit `http://127.0.0.1:8000/docs` to test the API.

### **💻 Start the Frontend (Streamlit)**  
Run the Streamlit app:  
```bash
streamlit run app.py
```
Access the UI at `http://localhost:8501/`.

---

## **Project Structure**  
```
📂 BGremover
├── 📜 main.py       # FastAPI backend
├── 📜 app.py        # Streamlit frontend
├── 📜 requirements.txt
```

---

## **Contributing**  
Feel free to fork the repo, open issues, or submit pull requests!  

---

## **License**  
This project is open-source under the **MIT License**.  
