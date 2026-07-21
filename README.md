# 🖼️ FastAPI Image Mask Generator

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight **FastAPI** application that generates **binary masks** from uploaded images using **OpenCV** and **NumPy**. The API supports **batch image uploads** and uses Python's **multiprocessing** module to process multiple images simultaneously for improved performance.

---

# ✨ Features

- 📤 Upload one or multiple images
- ⚡ Parallel image processing using multiprocessing
- 🎭 Automatic binary mask generation
- 💾 Save generated masks automatically
- 📊 Count white pixels in each mask
- 🚀 High-performance FastAPI backend
- 📖 Interactive Swagger UI
- 🔄 Batch image processing

---

# 🏗️ Architecture

```text
                Upload Images
                      │
                      ▼
              FastAPI Endpoint
                      │
                      ▼
          Temporary Image Storage
                      │
                      ▼
          Multiprocessing Pool
                      │
      ┌───────────────┴───────────────┐
      ▼                               ▼
 Read Image                    Generate Mask
      │                               │
      └───────────────┬───────────────┘
                      ▼
             Save Mask as PNG
                      │
                      ▼
            Count White Pixels
                      │
                      ▼
             Return JSON Response
```

---

# 🛠️ Tech Stack

- Python 3.11+
- FastAPI
- OpenCV
- NumPy
- Multiprocessing
- Uvicorn

---

# 📂 Project Structure

```text
image-mask-api/
│
├── app.py
├── requirements.txt
├── output/
├── README.md
└── .gitignore
```

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/image-mask-api.git
cd image-mask-api
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ requirements.txt

```text
fastapi
uvicorn
opencv-python
numpy
python-multipart
```

---

## 5️⃣ Run the API

```bash
uvicorn app:app --reload
```

or

```bash
python app.py
```

---

## 6️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📤 Generate Image Masks

### Endpoint

```
POST /generate-mask
```

Upload one or multiple images (`.jpg`, `.jpeg`, `.png`).

---

## Using Swagger UI

1. Open `/docs`
2. Click **POST /generate-mask**
3. Click **Try it out**
4. Upload one or more images
5. Click **Execute**

---

## Using cURL

```bash
curl -X POST "http://127.0.0.1:8000/generate-mask" \
-F "files=@image1.jpg" \
-F "files=@image2.jpg"
```

---

## Example Response

```json
{
  "total_images": 2,
  "total_white_pixels": 45873,
  "results": [
    {
      "filename": "image1.jpg",
      "white_pixels": 18598,
      "mask_path": "output/image1_mask.png"
    },
    {
      "filename": "image2.jpg",
      "white_pixels": 27275,
      "mask_path": "output/image2_mask.png"
    }
  ]
}
```

---

# 🧠 How It Works

1. Upload one or more images.
2. FastAPI stores uploaded images temporarily.
3. Images are distributed across available CPU cores.
4. OpenCV reads each image.
5. Pixels satisfying:

```text
R > 200
G > 200
B > 200
```

are converted into white (255), while all other pixels become black (0).

6. The generated mask is saved as a PNG file.
7. White pixels are counted.
8. Results are returned as JSON.

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API information |
| POST | `/generate-mask` | Generate image masks |

---

# 📊 Sample Output

Original Image

```
⬜⬜⬛
⬜🟥⬛
⬛⬜⬜
```

Generated Mask

```
⬜⬜⬛
⬜⬛⬛
⬛⬜⬜
```

Where

- White = Selected pixels (255)
- Black = Background (0)

---

# 📈 Use Cases

- Medical image preprocessing
- Computer vision datasets
- Satellite image analysis
- Industrial quality inspection
- Background removal
- Image segmentation preprocessing
- Bright object detection
- Pixel statistics

---

# ⚙️ Configuration

Current threshold:

```python
mask = np.all(img > 200, axis=2).astype(np.uint8) * 255
```

You can adjust the threshold value (`200`) depending on your use case.

---

# 📋 Requirements

- Python 3.11+
- FastAPI
- OpenCV
- NumPy
- Uvicorn

---

# 🔒 Security

This project:

- ✅ Does not use API keys
- ✅ Does not require authentication
- ✅ Does not collect user information

For production deployment consider adding:

- Authentication
- Rate limiting
- HTTPS
- File validation
- Maximum upload size

---

# 🚀 Future Improvements

- GPU (CUDA) acceleration
- Adjustable threshold API
- ZIP download of masks
- Docker support
- Kubernetes deployment
- Progress bar
- Image preview endpoint
- Background removal
- Color-based masking
- Morphological operations
- Histogram statistics

---

# 🧪 Run Tests

```bash
pytest
```

---

# 🤝 Contributing

Fork the repository.

Create a branch.

```bash
git checkout -b feature/new-feature
```

Commit changes.

```bash
git commit -m "Add new feature"
```

Push branch.

```bash
git push origin feature/new-feature
```

Open a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.
