# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/RotulagemBaterPonto.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/pix_force_logo.png', '.'), ('C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/Lib', 'Lib/'), ('C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/Scripts', 'Scripts/')],
    hiddenimports=['cryptography', 'PIL', 'pkg_resources.py2_warn'],
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
    name='Registro de Trabalho da Rotulagem - PIX FORCE',
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
    icon=['C:\\Users\\Rapha\\Desktop\\BaterPontoV2\\BaterPontoRotulagem\\Future-80_icon-icons.com_57322.ico'],
)
