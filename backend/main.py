import os
import sys
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# 处理 PyInstaller 打包时的临时目录
# _MEIPASS 是 PyInstaller 解压缩资源的临时目录
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 前端静态文件路径
frontend_dist = os.path.join(BASE_DIR, "frontend", "dist")

# 如果存在前端构建目录，则挂载静态文件
if os.path.exists(frontend_dist):
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")

    # 让 FastAPI 处理前端的路由（例如 Vue Router history 模式）
    @app.get("/{full_path:path}")
    async def serve_vue(full_path: str):
        index_path = os.path.join(frontend_dist, "index.html")
        if os.path.exists(index_path):
            return FileResponse(index_path)
        return {"error": "index.html not found"}

# 示例 API
@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI + Vue!"}
