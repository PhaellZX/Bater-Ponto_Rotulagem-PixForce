import sys
from cx_Freeze import setup, Executable

# Adicione aqui as dependências necessárias, se houver
build_exe_options = {
    "packages": ["os", "json", "tkinter", "PIL", "datetime", "cryptography"],
    "include_files": [
        ("C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/pix_force_logo.png", "pix_force_logo.png"),
        ("C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/Lib", "Lib"),
        ("C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/Scripts", "Scripts"),
        ("C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/Future-80_icon-icons.com_57322.ico", "Future-80_icon-icons.com_57322.ico")
    ]
}

# Cria o executável
executables = [
    Executable(
        "C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/RotulagemBaterPonto.py",
        base="Win32GUI" if sys.platform == "win32" else None,
        icon="C:/Users/Rapha/Desktop/BaterPontoV2/BaterPontoRotulagem/Future-80_icon-icons.com_57322.ico",
        target_name="Registro de Trabalho da Rotulagem - PIX FORCE"
    )
]

# Configuração do setup
setup(
    name="Registro de Trabalho da Rotulagem - PIX FORCE",
    version="1.0",
    description="Aplicação de Registro de Ponto",
    options={"build_exe": build_exe_options},
    executables=executables
)
