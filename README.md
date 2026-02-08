## 🧠 Background Remover – Backend API

Backend en FastAPI para eliminar fondos de imágenes usando IA (rembg). Está diseñado para usarse como servicio HTTP y ser consumido por un frontend (por ejemplo, React/Vite) o cualquier cliente que haga requests POST.

---

## 🚀 Demo en Producción

```bash
Base URL: https://yordinz-background-remover.hf.space

Health check: GET / → { "ok": true }

Swagger: /docs
```

---

## ✨ Features

Eliminación de fondo real usando modelos de IA (rembg)

Respuesta en PNG con transparencia

API simple y rápida

CORS habilitado (lista para frontend externo)

Contenedorizado con Docker (ideal para Hugging Face Spaces)

---

## 🧩 Stack

Python 3.10

FastAPI

rembg (U²-Net / ONNX)

Pillow

Uvicorn

Docker

Hugginface (API-BACKEND)

---

## 📦 Estructura del Proyecto

.
├── api.py            # FastAPI app
├── requirements.txt  # Dependencias
├── Dockerfile        # Build para Hugging Face Spaces
└── README.md

>🔌 Endpoints

GET /
Health check.

Response=
{ "ok": true }

POST /remove-bg

Elimina el fondo de una imagen.

Request=
multipart/form-data

Campo: file (PNG o JPG)

Response=
image/png (imagen con fondo transparente)

---

## 🧪 Probar localmente

1️⃣ Crear entorno virtual

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

2️⃣ Instalar dependencias

pip install -r requirements.txt

3️⃣ Ejecutar servidor

```bash
uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

Abre:

```bash
http://127.0.0.1:8000/

http://127.0.0.1:8000/docs
```

---

## 🐳 Docker (Hugging Face Spaces)

Este backend está listo para correr en Hugging Face Spaces (Docker → Blank).

Dockerfile

FROM python:3.10-slim

WORKDIR /app

```bash
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*
```

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]

---

## 🌐 Uso desde un Frontend (ejemplo)

const API_URL = "https://yordinz-background-remover.hf.space";

const formData = new FormData();
formData.append("file", imageFile);

const res = await fetch(`${API_URL}/remove-bg`, {
  method: "POST",
  body: formData,
});

const blob = await res.blob();
const imageUrl = URL.createObjectURL(blob);

---

## ⚠️ Notas

Tamaño recomendado de imagen: ≤ 8 MB

El primer request puede tardar un poco (cold start)
