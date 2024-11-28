
import streamlit as st


import os
import shutil

from PIL import Image


# 删除临时文件夹及其中内容的函数
def delete_temp_files(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


# Streamlit 文件上传界面
def main1():
    st.title("批量 PNG/JPG 转 PDF 工具")
    st.write("上传一个或多个 PNG 或 JPG 图像文件，它们将被转换成一个 PDF 文件。")

    # 上传多个文件
    uploaded_files = st.file_uploader("选择 PNG 或 JPG 文件", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

    # 输入自定义文件名
    custom_filename = st.text_input("自定义输出 PDF 文件名（不包含扩展名）", "output")

    if st.button('点击开始转换'):
        if uploaded_files:
            # 获取上传文件的临时路径
            temp_dir = "temp_files"
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)

            img_paths = []  # 用来存储图像的路径

            # 将上传的每个文件保存到本地临时目录
            for uploaded_file in uploaded_files:
                img_path = os.path.join(temp_dir, uploaded_file.name)
                with open(img_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                img_paths.append(img_path)

            # 设置 PDF 文件保存路径
            pdf_path = os.path.join(temp_dir, custom_filename + ".pdf")

            # 使用 spinner 显示加载动画
            with st.spinner('正在转换文件，请稍候...'):
                try:
                    # 打开所有图片并调整质量（例如，调整为 RGB 模式，压缩质量）
                    images = []
                    max_width = 800  # 设置最大宽度，用于缩放图片
                    for img_path in img_paths:
                        image = Image.open(img_path)
                        image = image.convert("RGB")  # 转换为 RGB 模式，避免透明背景问题

                        # 调整图片大小，保持比例，最大宽度为 800px
                        image.thumbnail((max_width, max_width))
                        images.append(image)

                    # 保存为一个 PDF 文件
                    images[0].save(pdf_path, save_all=True, append_images=images[1:], resolution=100.0, quality=95)

                    st.success("文件转换完成！")
                except Exception as e:
                    st.error(f"转换失败: {e}")

            # 只有在 PDF 转换成功后，才显示下载按钮
            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button("下载 PDF 文件", pdf_file, file_name=custom_filename + ".pdf")

            # 清理临时文件夹和文件
            delete_temp_files(temp_dir)



main1()
