# app.py

import streamlit as st

page1 = st.Page("pdf_to_txt.py", title="pdf_to_txt")
page2 = st.Page("pdf-png.py", title="pdf-png")
page3 = st.Page("pdf-ppt 图像无等比压缩.py", title='pdf-ppt 图像无等比压缩')
page4 = st.Page('pdf-ppt 图像有等比压缩.py', title='pdf-ppt 图像有等比压缩')
page5 = st.Page('pdf-word.py', title='pdf-word')
page6 = st.Page('png-pdf.py', title='png-pdf')
#page7 = st.Page('png-word.py', title='png-word')
page8 = st.Page('ppt-pdf.py', title='ppt-pdf')
page9 = st.Page('txt_to_pdf.py', title='txt-pdf')
page10 = st.Page('word-pdf.py', title='word-pdf')
page11 = st.Page('将pdf转为图像存为word.py', title='将pdf转为图像存为word')

pg = st.navigation([page1, page2, page3, page4, page5, page6, page8, page9, page10, page11])
pg.run()
