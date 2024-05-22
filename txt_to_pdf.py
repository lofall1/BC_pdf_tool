from fpdf import FPDF
import streamlit as st
import pandas as pd
from io import StringIO
import os
import shutil
pdf = FPDF()
# uploaded_file = st.file_uploader("Choose a file")
#
# # 添加字体（第一个参数是字体类型，第二个是字体样式，第三个是字体文件名）
# pdf.add_font(family='YouYuan', style='', fname='YouYuan.ttf', uni=True)
# # 创建一个新页面
# pdf.add_page()
# # 设置字体
# pdf.set_font('YouYuan', '', 20)
#
# # 写入文本
# if uploaded_file:
#     for uploaded_file in uploaded_file:
#         file_contents = uploaded_file.getvalue()
#         file_path = os.path.join("D:\\", uploaded_file.name)
#         # 将文件保存到本地文件系统
#         with open(file_path, "wb") as f:
#             f.write(file_contents)
#         fp=open(file_path,'r',encoding='utf-8')
#         for i in fp:
#             pdf.cell(200, 8, txt=i, ln=1, align='C')
# # 保存文档
#         pdf.output('text2.pdf')
#         text_contents = '''text2.pdf'''
#         st.download_button('下载这pdf', text_contents)
def upload_Save():
    # 创建一个文件夹用于保存上传的文件（若存在则清空，若不存在，则新建）
    dirs = 'uploads'
    if not os.path.exists(dirs):#不存在就创建
        os.makedirs(dirs)
    else:
        shutil.rmtree(dirs)#如果存在就删除再创建
        os.makedirs(dirs)
    # 选择文件
    uploaded_files = st.file_uploader("请选择文件:",accept_multiple_files =True, type=["pdf","txt","docx"])
    # 保存文件
    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_contents = uploaded_file.getvalue()
            file_path = os.path.join(dirs, uploaded_file.name)
            # 将文件保存到本地文件系统
            with open(file_path, "wb") as f:
                f.write(file_contents)
            # 获取文件路径
            st.write(f"文件地址: {file_path}")
            #转换pdf部分
            fp = open(file_path, 'r', encoding='utf-8')
            pdf.add_font(family='YouYuan', style='', fname='YouYuan.ttf', uni=True)
            # 创建一个新页面
            pdf.add_page()
            # 设置字体
            pdf.set_font('YouYuan', '', 20)
            for i in fp:
                pdf.cell(200, 8, txt=i, ln=1, align='C')
            pdf.output('text3.pdf')
            with open('text3.pdf', "rb") as f:
                st.download_button('下载这pdf', data=f, file_name='text3.pdf',mime="image/pdf")

upload_Save()