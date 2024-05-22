# import sys
# from streamlit.web import cli as stcli
#
# if __name__ == '__main__':
#     sys.argv = ["streamlit", "run", "txt_to_pdf.py"]
#     sys.exit(stcli.main())
import streamlit.web.cli as stcli
import os, sys
from fpdf import FPDF
pdf = FPDF()
import streamlit as st
import pandas as pd
from io import StringIO
import os
import shutil

def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("txt_to_pdf.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())