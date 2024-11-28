# import os
# import shutil
# import streamlit as st
# from pdf2image import convert_from_path
# from PIL import Image
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
#     st.title("PDF 转 图像 工具")
#     st.write("上传一个 PDF 文件，它将被转换成多个图像文件，每页一个图像。")
#
#     # 上传 PDF 文件
#     uploaded_file = st.file_uploader("选择一个 PDF 文件", type=["pdf"])
#
#     # 输入自定义文件名前缀
#     custom_filename = st.text_input("自定义输出文件名前缀（不包含扩展名）", "page")
#
#     if uploaded_file:
#         # 获取上传文件的临时路径
#         temp_dir = "temp_files"
#         if not os.path.exists(temp_dir):
#             os.makedirs(temp_dir)
#
#         pdf_path = os.path.join(temp_dir, uploaded_file.name)
#
#         # 将上传的 PDF 文件保存到本地临时目录
#         with open(pdf_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
#
#         # 创建存储图像的路径列表
#         img_paths = []
#
#         # 使用 spinner 显示加载动画
#         with st.spinner('正在转换文件，请稍候...'):
#             try:
#                 # 将 PDF 转换为图像
#                 images = convert_from_path(pdf_path, dpi=200)  # 200 DPI 提供较好的图像质量
#
#                 # 设置最大宽度，用于缩放图片
#                 max_width = 800
#                 for i, image in enumerate(images):
#                     # 调整图片大小，保持比例，最大宽度为 800px
#                     image.thumbnail((max_width, max_width))
#
#                     # 保存图像到文件
#                     img_filename = os.path.join(temp_dir, f"{custom_filename}_page_{i + 1}.png")
#                     image.save(img_filename, "PNG")
#                     img_paths.append(img_filename)
#
#                 st.success(f"文件转换完成！生成了 {len(images)} 页图像文件。")
#             except Exception as e:
#                 st.error(f"转换失败: {e}")
#
#         # 只在图像转换成功后显示下载按钮
#         for img_path in img_paths:
#             with open(img_path, "rb") as img_file:
#                 st.download_button(f"下载 {os.path.basename(img_path)}", img_file, file_name=os.path.basename(img_path))
#
#         # 清理临时文件夹和文件
#         #delete_temp_files(temp_dir)
#         #st.write("临时文件夹已删除。")
#
#
# if __name__ == "__main__":
#     main()


# import os
# import shutil
# import streamlit as st
# from pdf2image import convert_from_path
# from PIL import Image
#
# # 删除临时文件夹及其中内容的函数
# def delete_temp_files(temp_dir):
#     if os.path.exists(temp_dir):
#         shutil.rmtree(temp_dir)
#
# # Streamlit 文件上传界面
# def main():
#     st.title("PDF 转 图像 工具")
#     st.write("上传一个 PDF 文件，它将被转换成多个图像文件，每页一个图像。")
#
#     # 上传 PDF 文件
#     uploaded_file = st.file_uploader("选择一个 PDF 文件", type=["pdf"])
#
#     # 输入自定义文件名前缀
#     custom_filename = st.text_input("自定义输出文件名前缀（不包含扩展名）", uploaded_file.name)
#
#     if uploaded_file:
#         # 如果 PDF 转换后的结果已经缓存，直接加载
#         if "img_paths" not in st.session_state:
#             st.session_state.img_paths = []  # 用于存储每页图像的路径
#
#         # 获取上传文件的临时路径
#         temp_dir = "temp_files"
#         if not os.path.exists(temp_dir):
#             os.makedirs(temp_dir)
#
#         pdf_path = os.path.join(temp_dir, uploaded_file.name)
#
#         # 将上传的 PDF 文件保存到本地临时目录
#         with open(pdf_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
#
#         # 使用 spinner 显示加载动画
#         with st.spinner('正在转换文件，请稍候...'):
#             try:
#                 # 将 PDF 转换为图像
#                 images = convert_from_path(pdf_path, dpi=200)  # 200 DPI 提供较好的图像质量
#
#                 # 设置最大宽度，用于缩放图片
#                 max_width = 800
#                 img_paths = []  # 存储每页图像的路径
#
#                 for i, image in enumerate(images):
#                     # 调整图片大小，保持比例，最大宽度为 800px
#                     image.thumbnail((max_width, max_width))
#
#                     # 保存图像到文件
#                     img_filename = os.path.join(temp_dir, f"{custom_filename}_page_{i+1}.png")
#                     image.save(img_filename, "PNG")
#                     img_paths.append(img_filename)
#
#                 # 将生成的图像路径存储到 session_state 中
#                 st.session_state.img_paths = img_paths
#                 st.success(f"文件转换完成！生成了 {len(images)} 页图像文件。")
#             except Exception as e:
#                 st.error(f"转换失败: {e}")
#
#         # 只在图像转换成功后显示下载按钮
#         if st.session_state.img_paths:
#             for img_path in st.session_state.img_paths:
#                 with open(img_path, "rb") as img_file:
#                     st.download_button(f"下载 {os.path.basename(img_path)}", img_file, file_name=os.path.basename(img_path))
#
#         # 清理临时文件夹和文件
#         delete_temp_files(temp_dir)
#         st.write("临时文件夹已删除。")
#
# if __name__ == "__main__":
#     main()


import os
import shutil
import zipfile
import streamlit as st
from pdf2image import convert_from_path
from PIL import Image

# 删除临时文件夹及其中内容的函数
def delete_temp_files(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

# 压缩文件为 zip 文件
def create_zip_from_files(file_paths, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in file_paths:
            zipf.write(file, os.path.basename(file))
def reset_page():
    # 通过清空 session_state 来重置页面的所有控件
    for key in st.session_state.keys():
        del st.session_state[key]
# Streamlit 文件上传界面
def main():
    st.title("PDF 转 图像 工具")
    st.write("上传一个 PDF 文件，它将被转换成多个图像文件，每页一个图像。")

    # 上传 PDF 文件
    uploaded_file = st.file_uploader("选择一个 PDF 文件", type=["pdf"])

    # 输入自定义文件名前缀
    if uploaded_file:
        custom_filename = st.text_input("重命名文件（不包含扩展名）", uploaded_file.name.replace('.pdf',''))

    # 只有当文件上传且转换未完成时才执行转换
    if uploaded_file and ("img_paths" not in st.session_state or not st.session_state.img_paths):
        # 获取上传文件的临时路径
        temp_dir = "temp_files"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        else:
            delete_temp_files(temp_dir)
            os.makedirs(temp_dir)
        pdf_path = os.path.join(temp_dir, uploaded_file.name)

        # 将上传的 PDF 文件保存到本地临时目录
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 使用 spinner 显示加载动画
        with st.spinner('正在转换文件，请稍候...'):
            try:
                # 将 PDF 转换为图像
                images = convert_from_path(pdf_path, dpi=200)  # 200 DPI 提供较好的图像质量

                # 设置最大宽度，用于缩放图片
                max_width = 800
                img_paths = []  # 存储每页图像的路径

                for i, image in enumerate(images):
                    # 调整图片大小，保持比例，最大宽度为 800px
                    image.thumbnail((max_width, max_width))

                    # 保存图像到文件
                    img_filename = os.path.join(temp_dir, f"{custom_filename}_page_{i+1}.png")
                    image.save(img_filename, "PNG")
                    img_paths.append(img_filename)

                # 将生成的图像路径存储到 session_state 中
                st.session_state.img_paths = img_paths
                st.session_state.pdf_converted = True  # 标记 PDF 转换完成
                st.success(f"文件转换完成！生成了 {len(images)} 页图像文件。")
            except Exception as e:
                st.error(f"转换失败: {e}")


    # 提供“一键下载”按钮（下载所有图像）
    if "img_paths" in st.session_state and st.session_state.img_paths:
        # 确保 temp_dir 存在
        temp_dir = "temp_files"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        # 创建一个 ZIP 文件
        zip_path = os.path.join(temp_dir, "output_images.zip")
        with open(zip_path, "wb") as zipf:
            create_zip_from_files(st.session_state.img_paths, zip_path)

        # 显示一键下载按钮
        with open(zip_path, "rb") as zip_file:
            st.download_button("一键下载所有图像", zip_file, file_name="output_images.zip")

        # 显示单个图像下载按钮
        for img_path in st.session_state.img_paths:
            with open(img_path, "rb") as img_file:
                st.download_button(f"下载 {os.path.basename(img_path)}", img_file, file_name=os.path.basename(img_path))

        if st.button('重命名文件/重新生成文件'):
            delete_temp_files(temp_dir)
            reset_page()
            st.rerun()
main()




# import os
# import shutil
# import zipfile
# import streamlit as st
# from pdf2image import convert_from_path
# from PIL import Image
#
# # 删除临时文件夹及其中内容的函数
# def delete_temp_files(temp_dir):
#     if os.path.exists(temp_dir):
#         shutil.rmtree(temp_dir)
#
# # 压缩文件为 zip 文件
# def create_zip_from_files(file_paths, zip_path):
#     with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         for file in file_paths:
#             zipf.write(file, os.path.basename(file))
# def reset_page():
#     # 通过清空 session_state 来重置页面的所有控件
#     for key in st.session_state.keys():
#         del st.session_state[key]
# # Streamlit 文件上传界面
# def main():
#     st.title("PDF 转 图像 工具")
#     st.write("上传一个 PDF 文件，它将被转换成多个图像文件，每页一个图像。")
#
#     # 上传 PDF 文件
#     uploaded_file = st.file_uploader("选择一个 PDF 文件", type=["pdf"])
#
#     # 输入自定义文件名前缀
#     if uploaded_file:
#         custom_filename = st.text_input("自定义输出文件名前缀（不包含扩展名）", uploaded_file.name.replace('.pdf',''))
#
#     # 只有当文件上传且转换未完成时才执行转换
#     if uploaded_file and ("img_paths" not in st.session_state or not st.session_state.img_paths):
#         # 获取上传文件的临时路径
#         temp_dir = "temp_files"
#         if not os.path.exists(temp_dir):
#             os.makedirs(temp_dir)
#
#         pdf_path = os.path.join(temp_dir, uploaded_file.name)
#
#         # 将上传的 PDF 文件保存到本地临时目录
#         with open(pdf_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
#
#         # 使用 spinner 显示加载动画
#         with st.spinner('正在转换文件，请稍候...'):
#             try:
#                 # 将 PDF 转换为图像
#                 images = convert_from_path(pdf_path, dpi=200)  # 200 DPI 提供较好的图像质量
#
#                 # 设置最大宽度，用于缩放图片
#                 max_width = 800
#                 img_paths = []  # 存储每页图像的路径
#
#                 for i, image in enumerate(images):
#                     # 调整图片大小，保持比例，最大宽度为 800px
#                     image.thumbnail((max_width, max_width))
#
#                     # 保存图像到文件
#                     img_filename = os.path.join(temp_dir, f"{custom_filename}_page_{i+1}.png")
#                     image.save(img_filename, "PNG")
#                     img_paths.append(img_filename)
#
#                 # 将生成的图像路径存储到 session_state 中
#                 st.session_state.img_paths = img_paths
#                 st.session_state.pdf_converted = True  # 标记 PDF 转换完成
#                 st.success(f"文件转换完成！生成了 {len(images)} 页图像文件。")
#             except Exception as e:
#                 st.error(f"转换失败: {e}")
#
#
#     # 提供“一键下载”按钮（下载所有图像）
#     if "img_paths" in st.session_state and st.session_state.img_paths:
#         # 确保 temp_dir 存在
#         temp_dir = "temp_files"
#         if not os.path.exists(temp_dir):
#             os.makedirs(temp_dir)
#
#         # 创建一个 ZIP 文件
#         zip_path = os.path.join(temp_dir, "output_images.zip")
#         with open(zip_path, "wb") as zipf:
#             create_zip_from_files(st.session_state.img_paths, zip_path)
#
#         # 显示一键下载按钮
#         with open(zip_path, "rb") as zip_file:
#             st.download_button("一键下载所有图像", zip_file, file_name="output_images.zip")
#
#         # 显示单个图像下载按钮
#         for img_path in st.session_state.img_paths:
#             with open(img_path, "rb") as img_file:
#                 st.download_button(f"下载 {os.path.basename(img_path)}", img_file, file_name=os.path.basename(img_path))
#         if st.button('不需要下载时点击此按钮清除临时文件'):
#             delete_temp_files(temp_dir)
#             reset_page()
#             st.rerun()
# if __name__ == "__main__":
#     main()
#
#
