import os
import cv2
import shutil
import tempfile
import multiprocessing as mp
import numpy as np

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI(title="Image Mask Generator API")

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def process_image(file_path):
    """
    Read image, generate binary mask,
    save mask and return white pixel count.
    """
    img = cv2.imread(file_path)

    if img is None:
        return {
            "filename": os.path.basename(file_path),
            "white_pixels": 0,
            "mask_path": None
        }

    # Generate mask
    mask = np.all(img > 200, axis=2).astype(np.uint8) * 255

    mask_filename = os.path.basename(file_path).replace(".jpg", "_mask.png")
    mask_path = os.path.join(OUTPUT_DIR, mask_filename)

    cv2.imwrite(mask_path, mask)

    white_pixels = int(np.sum(mask == 255))

    return {
        "filename": os.path.basename(file_path),
        "white_pixels": white_pixels,
        "mask_path": mask_path
    }


@app.post("/generate-mask")
async def generate_mask(files: list[UploadFile] = File(...)):
    """
    Upload one or multiple JPG images.
    Generates masks in parallel.
    """

    temp_files = []

    try:
        # Save uploaded files temporarily
        for file in files:
            suffix = os.path.splitext(file.filename)[1]

            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
                shutil.copyfileobj(file.file, temp)
                temp_files.append(temp.name)

        # Parallel processing
        with mp.Pool(processes=mp.cpu_count()) as pool:
            results = pool.map(process_image, temp_files)

        total_pixels = sum(r["white_pixels"] for r in results)

        return JSONResponse({
            "total_images": len(results),
            "total_white_pixels": total_pixels,
            "results": results
        })

    finally:
        # Remove temp files
        for file in temp_files:
            if os.path.exists(file):
                os.remove(file)


@app.get("/")
def home():
    return {
        "message": "Image Mask Generator API",
        "endpoint": "/generate-mask"
    }
