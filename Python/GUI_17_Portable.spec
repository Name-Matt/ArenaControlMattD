# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['GUI_17_Portable.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Matt\\Documents\\GitHub\\ArenaControlMattD\\Python\\OBSPortable', '.')],
    hiddenimports=['tkinter.messagebox', 'tkinter', 'ttk', 'subprocess', 'os', 'threading', 'serial', 'serial.tools.list_ports', 'GUIStyles'],
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
    name='GUI_17_Portable',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Matt\\Downloads\\uolcrest.ico'],
)