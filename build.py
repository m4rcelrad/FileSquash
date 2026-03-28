import os
import PyInstaller.__main__


def build_app():
    build_args = [
        os.path.join("src", "main.py"),
        "--name=FileSquash",
        "--onefile",
        "--windowed",
        "--noconfirm",
        "--clean"
    ]

    PyInstaller.__main__.run(build_args)


if __name__ == "__main__":
    build_app()
