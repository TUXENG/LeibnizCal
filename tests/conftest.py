import sys
import os

# Añade la carpeta raíz del proyecto al path, de modo que 'src' sea importable
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT_DIR)
