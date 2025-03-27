
import os
import shutil
import tempfile
import pytesseract
import streamlit as st
from pdf2image import convert_from_path

# 设置 Tesseract 的路径（如果需要）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 替换为实际的tesseract安装路径

# 将 PDF 转换为图像
def pdf_to_images1(pdf_path):
    """将 PDF 转换为图像"""
    images = convert_from_path(pdf_path, dpi=300)  # 300 DPI 提供较高的图像质量
    return images


# 将图像内容转换为文本
def images_to_text1(images):
    """将图像内容转换为文本"""
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image) + "\n"
    return text


# 删除临时文件夹及其中内容的函数
def delete_temp_files1(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


# Streamlit 界面
def main1():
    st.title("PDF OCR 转换工具")
    st.write("上传一个 PDF 文件，它将被转换为图像并进行 OCR 识别，最终生成一个文本文件。")

    # 上传 PDF 文件
    uploaded_file = st.file_uploader("选择一个 PDF 文件", type=["pdf"])

    # 输入自定义文件名前缀
    if uploaded_file:
        custom_filename = st.text_input("自定义输出 TXT 文件名称（不包含扩展名）", uploaded_file.name.replace('.pdf',''))

    # 只有在上传新文件时，才执行 OCR 识别
    if uploaded_file and (uploaded_file.name not in st.session_state or st.session_state[uploaded_file.name] is None):
        # 创建临时目录存放文件
        temp_dir = tempfile.mkdtemp()

        # 将上传的 PDF 文件保存到临时目录
        pdf_path = os.path.join(temp_dir, uploaded_file.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 使用 spinner 显示加载动画
        with st.spinner('正在转换文件并进行 OCR 识别，请稍候...'):
            try:
                # 将 PDF 转换为图像并进行 OCR 识别
                images = pdf_to_images(pdf_path)
                extracted_text = images_to_text(images)

                # 保存 OCR 识别的文本为 TXT 文件
                txt_filename = custom_filename + ".txt"
                txt_path = os.path.join(temp_dir, txt_filename)
                with open(txt_path, "w", encoding="utf-8") as txt_file:
                    txt_file.write(extracted_text)

                # 将处理结果保存在 session_state 中
                st.session_state[uploaded_file.name] = {
                    "txt_path": txt_path,
                    "custom_filename": custom_filename + ".txt",
                    "temp_dir": temp_dir  # 保存临时目录路径
                }

                st.success("文件转换完成！")

            except Exception as e:
                st.error(f"转换失败: {e}")

    # 显示下载按钮（如果转换完成）
    if uploaded_file and uploaded_file.name in st.session_state and st.session_state[uploaded_file.name] is not None:
        result = st.session_state[uploaded_file.name]
        txt_path = result["txt_path"]
        txt_filename = result["custom_filename"]

        # 提供 TXT 文件下载按钮
        with open(txt_path, "rb") as txt_file:
            st.download_button("下载转换后的 TXT 文件", txt_file, file_name=txt_filename)

        # 清理临时文件夹和文件
        if st.button('下载完后，清理临时文件'):
            delete_temp_files(result["temp_dir"])
# 将 PDF 转换为图像
def pdf_to_images(pdf_path):
    """将 PDF 转换为图像"""
    images = convert_from_path(pdf_path, dpi=600)  # 300 DPI 提供较高的图像质量
    return images


# 将图像内容转换为文本
def images_to_text(images):
    """将图像内容转换为文本"""
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image,lang='chi_sim+eng') + "\n"
    return text


# 删除临时文件夹及其中内容的函数
def delete_temp_files(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


# Streamlit 界面
def main():
    st.title("PDF OCR 转换工具")
    st.write("上传一个 PDF 文件，它将被转换为图像并进行 OCR 识别，最终生成一个文本文件。")

    # 上传 PDF 文件
    uploaded_file = st.file_uploader("选择一个 PDF 文件", type=["pdf"])

    # 输入自定义文件名前缀
    if uploaded_file:
        custom_filename = st.text_input("自定义输出 TXT 文件名称（不包含扩展名）", uploaded_file.name.replace('.pdf',''))

    # 创建临时目录存放文件和存储识别结果
    temp_dir = None
    pdf_path = None
    txt_path = None

    # 只有在上传新文件时，才执行 OCR 识别
    if uploaded_file:
        # 创建临时目录存放文件
        temp_dir = tempfile.mkdtemp()

        # 将上传的 PDF 文件保存到临时目录
        pdf_path = os.path.join(temp_dir, uploaded_file.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 显示上传的文件名和文件大小
        st.write(f"已上传文件: {uploaded_file.name}")
        st.write(f"文件大小: {uploaded_file.size} 字节")

    # 开始进行 OCR 识别按钮
    if uploaded_file and custom_filename:
        if st.button("开始 OCR 识别"):
            with st.spinner('正在转换文件并进行 OCR 识别，请稍候...'):
                try:
                    # 将 PDF 转换为图像并进行 OCR 识别
                    images = pdf_to_images(pdf_path)
                    extracted_text = images_to_text(images)

                    # 根据自定义文件名重命名输出 TXT 文件
                    txt_filename = custom_filename + ".txt"
                    txt_path = os.path.join(temp_dir, txt_filename)

                    # 保存 OCR 识别的文本为 TXT 文件
                    with open(txt_path, "w", encoding="utf-8") as txt_file:
                        txt_file.write(extracted_text)

                    # 将处理结果保存在 session_state 中
                    st.session_state[uploaded_file.name] = {
                        "txt_path": txt_path,
                        "custom_filename": txt_filename,
                        "temp_dir": temp_dir  # 保存临时目录路径
                    }

                    st.success("文件转换完成！")

                except Exception as e:
                    st.error(f"转换失败: {e}")

    # 显示下载按钮（如果转换完成）
    if uploaded_file and uploaded_file.name in st.session_state and st.session_state[uploaded_file.name] is not None:
        result = st.session_state[uploaded_file.name]
        txt_path = result["txt_path"]
        txt_filename = result["custom_filename"]

        # 提供 TXT 文件下载按钮
        with open(txt_path, "rb") as txt_file:
            st.download_button("下载转换后的 TXT 文件", txt_file, file_name=txt_filename)

        # 清理临时文件夹和文件
        if st.button('清理临时文件'):
            delete_temp_files(result["temp_dir"])
            st.write("临时文件夹已删除。")


main()
