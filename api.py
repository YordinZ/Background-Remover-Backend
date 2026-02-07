from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://yordinz.github.io"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    from rembg import remove  # ✅ import aquí adentro (lazy)
    if not file.content_type or not file.content_type.startswith("image/"):
        return Response(b"Invalid file type", status_code=400, media_type="text/plain")

    data = await file.read()
    out = remove(data)
    return Response(content=out, media_type="image/png")
