import streamlit.web.cli as stcli
import os, sys
from fpdf import FPDF
import streamlit as st
import pandas as pd
from io import StringIO
import shutil
import tempfile
import pytesseract
from pdf2image import convert_from_path
import zipfile
from PIL import Image
from pptx import Presentation
from pptx.util import Inches
from docx import Document
import pythoncom
import comtypes.client
from win32com import client
from docx.shared import Inches

def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("run.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())