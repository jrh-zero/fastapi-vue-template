# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None

# 获取 backend/main.py 路径
script_path = os.path.join(os.path.dirname(__file__), "backend", "main.py")

# 获取前端 dist 路径
dist_path = os.path.join(os.path.dirname(__file__), "frontend", "dist")

# 不同平台的 add-data 分隔符
if sys.platform.startswith("win"):
    sep = ";"
else:
    sep = ":"

datas = [
    (dist_path, f"frontend{sep}dist")
]

a = Analysis(
    [script_path],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="myapp",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,   # 如果你不想要黑框，可以改成 False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

