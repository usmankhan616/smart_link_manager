from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import qrcode
import io
from fastapi.responses import StreamingResponse
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class URLItem(BaseModel):
    url: str

app = FastAPI()

# --- Google Gemini API Configuration ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
# ------------------------------------

# Shared headers for browser-like requests
browser_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

@app.get("/")
def read_root():
    return {"message": "Smart Link Manager API is running! 🚀"}

# UPDATED: Using the unshorten.me API
@app.post("/expand/")
async def expand_link(item: URLItem):
    api_url = f"https://unshorten.me/api/v2/unshorten?url={item.url}"
    try:
        response = requests.get(api_url, headers=browser_headers, timeout=10)
        response.raise_for_status() # This will raise an error for bad responses (4xx or 5xx)
        
        data = response.json()
        if data.get("unshortened_url"):
            return {"original_url": item.url, "expanded_url": data["unshortened_url"]}
        else:
            # If the API doesn't return the expected key, return the original URL
            return {"original_url": item.url, "expanded_url": item.url}

    except requests.RequestException:
        raise HTTPException(status_code=400, detail="Invalid or unreachable URL provided.")

@app.post("/qrcode/")
async def create_qrcode(item: URLItem):
    img = qrcode.make(item.url)
    buf = io.BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

@app.post("/shorten/")
async def shorten_link(item: URLItem):
    api_url = f"http://tinyurl.com/api-create.php?url={item.url}"
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return {"original_url": item.url, "shortened_url": response.text}
        else:
            raise HTTPException(status_code=400, detail="Failed to shorten URL.")
    except requests.RequestException:
        raise HTTPException(status_code=500, detail="Error connecting to shortening service.")

@app.post("/correct/")
async def correct_link_ai(item: URLItem):
    if not GOOGLE_API_KEY:
        raise HTTPException(status_code=500, detail="Google API Key is not configured.")
    
    prompt = f"Please correct the following broken URL. Only return the corrected URL and nothing else. If it looks correct, return it as is. Broken URL: '{item.url}'"
    try:
        response = model.generate_content(prompt)
        return {"original_url": item.url, "corrected_url": response.text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred with the AI model: {str(e)}")
