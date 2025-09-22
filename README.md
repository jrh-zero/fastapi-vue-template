# fastapi-vue-template
🔥 A full-stack template with FastAPI + Vue3. Supports Windows/Linux packaging via PyInstaller, and CI/CD automation with GitHub Actions &amp; Jenkins. （FastAPI + Vue3 前后端一体化模板，支持 Windows/Linux 打包和 CI/CD 自动化部署）
=======
# FastAPI + Vue3 模板 🚀

这是一个 **前后端一体化模板**，基于 **FastAPI + Vue3 + PyInstaller**，支持在 **Windows/Linux** 下打包为独立可执行文件。

## ✨ 功能特性
- ✅ Vue3 + Vite 前端工程
- ✅ FastAPI 后端 API
- ✅ 前后端一体化打包（PyInstaller）
- ✅ 支持 Windows/Linux 双平台运行
- ✅ 支持 CI/CD 自动化构建与打包（Jenkins / GitHub Actions）

## 📦 本地运行

```bash
# 克隆项目
git clone https://github.com/yourname/fastapi-vue-template.git
cd fastapi-vue-template

# 安装后端依赖
pip install fastapi uvicorn pyinstaller

# 启动后端
uvicorn backend.main:app --reload

# 安装并构建前端
cd frontend
npm install
npm run build
```

## 🔨 打包

### Windows
```bash
pyinstaller myapp.spec
```

### Linux
```bash
pyinstaller myapp.spec
./dist/myapp/myapp
```

或运行：
```bash
chmod +x run.sh
./run.sh
```

## 🚀 CI/CD 自动化构建

### GitHub Actions
项目内置 `.github/workflows/build.yml`，push 到 main 分支后会自动构建：
- Linux ELF
- Windows EXE

### Jenkins
项目内置 `Jenkinsfile`，可在多平台节点分别打包。

## 📂 构建产物
- `dist/myapp/myapp.exe` → Windows 可执行文件
- `dist/myapp/myapp` → Linux 可执行文件
>>>>>>> ab3a59a ('init')
