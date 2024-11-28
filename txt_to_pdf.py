# from fpdf import FPDF
# import streamlit as st
# import pandas as pd
# from io import StringIO
# import os
# import shutil
# pdf = FPDF()
# def upload_Save():
#     # 创建一个文件夹用于保存上传的文件（若存在则清空，若不存在，则新建）
#     # dirs = 'uploads'
#     # if not os.path.exists(dirs):#不存在就创建
#     #     os.makedirs(dirs)
#     # else:
#     #     shutil.rmtree(dirs)#如果存在就删除再创建
#     #     os.makedirs(dirs)
#     # 选择文件
#     uploaded_files = st.file_uploader("请选择文件:",accept_multiple_files =True, type=["pdf","txt","docx"])
#     # 保存文件
#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             #file_contents = uploaded_file.getvalue()
#             #file_path = os.path.join(dirs, uploaded_file.name)
#             fp = open(uploaded_file.name, 'r', encoding='utf-8')
#             # # 将文件保存到本地文件系统
#             # with open(file_path, "wb") as f:
#             #     f.write(file_contents)
#             # # 获取文件路径
#             #st.write(f"文件地址: {file_path}")
#             #转换pdf部分
#             # fp = open(file_path, 'r', encoding='utf-8')
#             pdf.add_font(family='YouYuan', style='', fname='YouYuan.ttf', uni=True)
#             # 创建一个新页面
#             pdf.add_page()
#             # 设置字体
#             pdf.set_font('YouYuan', '', 20)
#             pdf.multi_cell(200, 8, txt=fp.read(), align='C')
#             file_name=uploaded_file.name+".pdf"
#             pdf.output(file_name)
#             with open('text3.pdf', "rb") as f:
#                 st.download_button('下载这pdf', data=f, file_name=file_name,mime="image/pdf")
#
# upload_Save()
import time

#
# from fpdf import FPDF
# import streamlit as st
# import pandas as pd
# from io import StringIO
# import os
# import shutil
# pdf = FPDF()
# def upload_Save():
#     # 创建一个文件夹用于保存上传的文件（若存在则清空，若不存在，则新建）
#     dirs = 'uploads'
#     if not os.path.exists(dirs):#不存在就创建
#         os.makedirs(dirs)
#     else:
#         shutil.rmtree(dirs)#如果存在就删除再创建
#         os.makedirs(dirs)
#     # 选择文件
#     uploaded_files = st.file_uploader("请选择文件:",accept_multiple_files =True, type=["pdf","txt","docx"])
#     # 保存文件
#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             file_contents = uploaded_file.getvalue()
#             file_path = os.path.join(dirs, uploaded_file.name)
#             # 将文件保存到本地文件系统
#             with open(file_path, "wb") as f:
#                 f.write(file_contents)
#             # 获取文件路径
#             st.write(f"文件地址: {file_path}")
#             #转换pdf部分
#             fp = open(file_path, 'r', encoding='utf-8')
#             pdf.add_font(family='YouYuan', style='', fname='YouYuan.ttf', uni=True)
#             # 创建一个新页面
#             pdf.add_page()
#             # 设置字体
#             pdf.set_font('YouYuan', '', 20)
#             for i in fp:
#                 pdf.cell(200, 8, txt=i, ln=1, align='C')
#             pdf.output('text3.pdf')
#             with open('text3.pdf', "rb") as f:
#                 st.download_button('下载这pdf', data=f, file_name='text3.pdf',mime="image/pdf")
#     #os.remove(dirs)
#
# upload_Save()
from fpdf import FPDF
import streamlit as st
import os
import shutil
pdf = FPDF()
dirs = 'temp'

def delete_temp_files(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


def upload_Save():
    st.title('txt转pdf工具')
    uploaded_files = st.file_uploader("请选择文件,一次仅能处理一个文件:", accept_multiple_files=True, type=["txt"])
    # 保存文件
    if uploaded_files:
        st.session_state['text_input_active'] = True
        st.session_state['output_pdf_path'] = None
        if not os.path.exists(dirs):  # 不存在就创建
            os.makedirs(dirs)
        # 选择文件
        for uploaded_file in uploaded_files:

            file_contents = uploaded_file.getvalue()
            file_path = os.path.join(dirs, uploaded_file.name)

            with open(file_path, "wb") as f:
                f.write(file_contents)
            pdf.add_font(family='YouYuan', style='', fname='YouYuan.ttf', uni=True)
            # 创建一个新页面
            pdf.add_page()
            # 设置字体
            pdf.set_font('YouYuan', '', 20)
            fp = open(file_path, 'r', encoding='utf-8')
            pdf.multi_cell(200, 8, txt=fp.read(), align='C')
            file_name = uploaded_file.name[:-4:] + ".pdf"
            #导出pdf
            path=os.path.join(dirs,file_name)
            pdf.output(path)
            if st.session_state.get('text_input_active', False):
                output_pdf_path = st.text_input(label='重命名你要生成pdf文档的名字', value=file_name[:-4:])
                # 处理用户输入
                if output_pdf_path :
                    st.session_state['output_pdf_path'] = output_pdf_path
                    st.session_state['text_input_active'] = False  # 禁用输入框，表示流程完成
            if st.session_state.get('output_pdf_path'):
                st.write('您的输入是', output_pdf_path)
                if os.path.exists(path):
                    with open(path, "rb") as f:
                        st.download_button('下载这pdf', data=f, file_name=output_pdf_path+".pdf", mime="image/pdf")
                del st.session_state['output_pdf_path']
def main():
        upload_Save()
        delete_temp_files(dirs)


main()




# from fpdf import FPDF
# import streamlit as st
# import os
# import shutil
# pdf = FPDF()
# def delete_temp_files(temp_dir):
#     if os.path.exists(temp_dir):
#         shutil.rmtree(temp_dir)
# def upload_Save(dirs):
#     uploaded_files = st.file_uploader("请选择文件,一次仅能选一个文件:", accept_multiple_files=True, type=["txt"])
#     # 保存文件
#     if uploaded_files:
#         st.session_state['text_input_active'] = True
#         st.session_state['output_pdf_path'] = None
#         if not os.path.exists(dirs):  # 不存在就创建
#             os.makedirs(dirs)
#         # 选择文件
#         st.session_state['path']=None
#         if st.button('文件上传完毕'):
#             for uploaded_file in uploaded_files:
#
#                 file_contents = uploaded_file.getvalue()
#                 file_path = os.path.join(dirs, "a.txt")
#                 path = os.path.join(dirs, "a.pdf")
#                 st.write(st.session_state['path'])
#                 st.session_state['path'] = path
#                 st.session_state['path']=False
#                 with open(file_path, "ab+") as f:
#                     f.write(file_contents)
#                 pdf.add_font(family='YouYuan', style='', fname='YouYuan.ttf', uni=True)
#                 # 创建一个新页面
#                 pdf.add_page()
#                 # 设置字体
#                 pdf.set_font('YouYuan', '', 20)
#                 fp = open(file_path, 'r', encoding='utf-8')
#                 pdf.multi_cell(200, 8, txt=fp.read(), align='C')
#                 file_name = "a" + ".pdf"
#                 #导出pdf
#                 pdf.output(path)
#         st.write(st.session_state['path'])
#         if st.session_state.get('text_input_active', False):
#             output_pdf_path = st.text_input(label='重命名你要生成pdf文档的名字', value='None')
#             # 处理用户输入
#             if st.button('输入完毕后按空格并且点击此按钮'):
#                 st.session_state['output_pdf_path'] = output_pdf_path
#                 st.session_state['text_input_active'] = False  # 禁用输入框，表示流程完成
#         if st.session_state.get('output_pdf_path'):
#             st.write('您的输入是', output_pdf_path)
#             st.write(st.session_state['path'])
#             if st.session_state.get('path'):
#                 with open(st.session_state['path'], "rb") as f:
#                     st.download_button('下载这pdf', data=f, file_name=output_pdf_path+".pdf", mime="image/pdf")
#
#             del st.session_state['output_pdf_path']
# def main():
#     dirs = 'temp'
#     upload_Save(dirs)
#     delete_temp_files(dirs)
#
# if __name__ == '__main__':
#     main()
