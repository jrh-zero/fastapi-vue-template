import os
import sys

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/api/hello")
def hello():
    return {"msg": "Hello FastAPI + Vue 🎉"}

# ✅ 运行时路径处理
if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONTEND_DIST = os.path.join(BASE_DIR, "frontend", "dist")

print("BASE_DIR =", BASE_DIR)
print("FRONTEND_DIST exists?", os.path.exists(FRONTEND_DIST))

if os.path.exists(FRONTEND_DIST):
    app.mount("/", StaticFiles(directory=FRONTEND_DIST, html=True), name="frontend")

# ✅ exe 入口
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)