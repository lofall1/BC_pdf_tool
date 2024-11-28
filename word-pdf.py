# import os
# import win32com.client as win32
# from docx import Document
# import shutil
# import streamlit as st
# import pythoncom  # 用于初始化 COM 库
# def convert_to_pdf(input_path, output_path):
#     pythoncom.CoInitialize()
#     # 创建Word应用程序实例
#     word_app = win32.gencache.EnsureDispatch('Word.Application')
#     # 设置应用程序可见性为False（不显示Word界面）
#     word_app.Visible = False
#
#     try:
#         # 打开Word文档
#         doc = word_app.Documents.Open(input_path)
#         # 保存为PDF
#         doc.SaveAs(output_path, FileFormat=17)
#         doc.Close()
#         return True
#     except Exception as e:
#         print("转换失败：" + str(e))
#         return False
#     finally:
#         # 关闭Word应用程序
#         word_app.Quit()
#     print("转换完毕")
# # 删除临时文件夹及其中内容的函数
# def delete_temp_files(temp_dir):
#     if os.path.exists(temp_dir):
#         shutil.rmtree(temp_dir)
# def main():
#     st.title("Word 转 PDF 工具")
#     st.write("上传一个 Word 文件，它将被转换成 PDF 格式。")
#
#     # 上传文件
#     uploaded_file = st.file_uploader("选择一个 Word 文件", type=["docx", "doc"])
#     if uploaded_file is not None:
#         # 获取上传文件的临时路径
#         temp_dir = "temp_files"
#         if not os.path.exists(temp_dir):
#             os.makedirs(temp_dir)
#
#         word_path = os.path.join(temp_dir, uploaded_file.name)
#
#         # 将上传的文件保存到本地临时目录
#         with open(word_path, "wb") as f:
#             f.write(uploaded_file.getvalue())
#
#         # 设置 PDF 文件保存路径
#         pdf_path = os.path.join(temp_dir, uploaded_file.name.replace(".docx", ".pdf").replace(".doc", ".pdf"))
#
#         # 转换 Word 为 PDF
#         st.write("正在转换文件...")
#         pythoncom.CoInitialize()
#         # 创建Word应用程序实例
#         word_app = win32.gencache.EnsureDispatch('Word.Application')
#         # 设置应用程序可见性为False（不显示Word界面）
#         word_app.Visible = False
#
#         try:
#             # 打开Word文档
#             doc = word_app.Documents.Open(word_path)
#             # 保存为PDF
#             doc.SaveAs(pdf_path, FileFormat=17)
#             doc.Close()
#             return True
#         except Exception as e:
#             print("转换失败：" + str(e))
#             return False
#         finally:
#             # 关闭Word应用程序
#             word_app.Quit()
#         # 显示转换后的 PDF 文件下载链接
#         with open(pdf_path, "rb") as pdf_file:
#             st.download_button("下载 PDF 文件", pdf_file,file_name=uploaded_file.name.replace(".docx", ".pdf").replace(".doc", ".pdf"),mime="image/pdf")

        # 清理临时文件夹和文件
        # delete_temp_files(temp_dir)
        # st.write("临时文件夹已删除。")
# 输入和输出文件路径
# input_file = "C:\\Users\\zeiwazi\\Desktop\\GitHub\\word-pdf\\多图.docx"
# output_file = "C:\\Users\\zeiwazi\\Desktop\\GitHub\\word-pdf\\多图.pdf"









# 处理 Word 转 PDF 的函数
# def convert_word_to_pdf(word_path, pdf_path):
#     # 创建一个 Word 应用对象
#     word = client.Dispatch('Word.Application')
#     word.Visible = False  # 不显示 Word 窗口
#
#     # 打开 Word 文件
#     doc = word.Documents.Open(word_path)
#
#     # 保存为 PDF
#     doc.SaveAs(pdf_path, FileFormat=17)  # FileFormat=17 对应 PDF 格式
#     doc.Close()
#     word.Quit()
#
#
# # 删除临时文件夹及其中内容的函数
# def delete_temp_files(temp_dir):
#     if os.path.exists(temp_dir):
#         shutil.rmtree(temp_dir)
#
#
# # Streamlit 文件上传界面
# def main():
#     st.title("Word 转 PDF 工具")
#     st.write("上传一个 Word 文件，它将被转换成 PDF 格式。")
#
#     # 上传文件
#     uploaded_file = st.file_uploader("选择一个 Word 文件", type=["docx", "doc"])
#     if uploaded_file is not None:
#         # 获取上传文件的临时路径
#         temp_dir = "temp_files"
#         if not os.path.exists(temp_dir):
#             os.makedirs(temp_dir)
#
#         word_path = os.path.join(temp_dir, uploaded_file.name)
#
#         # 将上传的文件保存到本地临时目录
#         with open(word_path, "wb") as f:
#             f.write(uploaded_file.getvalue())
#
#         # 设置 PDF 文件保存路径
#         pdf_path = os.path.join(temp_dir, uploaded_file.name.replace(".docx", ".pdf").replace(".doc", ".pdf"))
#
#         # 转换 Word 为 PDF
#         st.write("正在转换文件...")
#         convert_word_to_pdf(word_path, pdf_path)
#
#         # 显示转换后的 PDF 文件下载链接
#         with open(pdf_path, "rb") as pdf_file:
#             st.download_button("下载 PDF 文件", pdf_file,
#                                file_name=uploaded_file.name.replace(".docx", ".pdf").replace(".doc", ".pdf"))
#
#         # 清理临时文件夹和文件
#         delete_temp_files(temp_dir)
#         st.write("临时文件夹已删除。")
#
#
# if __name__ == "__main__":
#     main()


import os
import shutil
import time
import streamlit as st
from win32com import client
import pythoncom  # 用于初始化 COM 库


# 处理 Word 转 PDF 的函数
def convert_word_to_pdf(word_path, pdf_path):
    pythoncom.CoInitialize()  # 显式初始化 COM 库

    # 使用绝对路径来确保文件路径正确
    word_path = os.path.abspath(word_path)
    pdf_path = os.path.abspath(pdf_path)

    # 创建一个 Word 应用对象
    word = client.Dispatch('Word.Application')
    word.Visible = False  # 不显示 Word 窗口

    try:
        # 打开 Word 文件
        doc = word.Documents.Open(word_path)

        # 保存为 PDF
        doc.SaveAs(pdf_path, FileFormat=17)  # FileFormat=17 对应 PDF 格式
        doc.Close()
        word.Quit()
    except Exception as e:
        word.Quit()
        raise e  # 重新抛出异常


# 删除临时文件夹及其中内容的函数
def delete_temp_files(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


# Streamlit 文件上传界面
def main():
    st.title("Word 转 PDF 工具")
    st.write("上传一个 Word 文件，它将被转换成 PDF 格式。")

    # 上传文件
    uploaded_file = st.file_uploader("选择一个 Word 文件", type=["docx", "doc"])

    if uploaded_file is not None:
        # 获取上传文件的临时路径
        temp_dir = "temp_files"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        word_path = os.path.join(temp_dir, uploaded_file.name)

        # 将上传的文件保存到本地临时目录
        with open(word_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 设置 PDF 文件保存路径
        pdf_path = os.path.join(temp_dir, uploaded_file.name.replace(".docx", ".pdf").replace(".doc", ".pdf"))

        # 使用 spinner 显示加载动画
        if st.button("点击进行转换"):
            with st.spinner('正在转换文件，请稍候...'):
                # 进行文件转换
                try:
                    convert_word_to_pdf(word_path, pdf_path)
                    st.success("文件转换完成！")
                except Exception as e:
                    st.error(f"转换失败: {e}")

        # 只有在 PDF 转换成功后，才显示下载按钮
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as pdf_file:
                st.download_button("下载 PDF 文件", pdf_file,
                                file_name=uploaded_file.name.replace(".docx", ".pdf").replace(".doc", ".pdf"))

        # 清理临时文件夹和文件
        delete_temp_files(temp_dir)


main()
