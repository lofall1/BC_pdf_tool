# import fitz  # PyMuPDF
# from PIL import Image
# from docx import Document
# from docx.shared import Inches
# import os
#
#
# def extract_images_from_pdf(pdf_path, output_folder):
#     """
#     从 PDF 文档中提取所有图像并保存到指定文件夹。
#     """
#     # 创建输出文件夹
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # 打开 PDF 文件
#     pdf_document = fitz.open(pdf_path)
#     image_paths = []  # 存储提取的图像路径
#
#     for page_number in range(len(pdf_document)):
#         page = pdf_document[page_number]
#         images = page.get_images(full=True)
#
#         for img_index, img in enumerate(images):
#             xref = img[0]
#             base_image = pdf_document.extract_image(xref)
#             image_bytes = base_image["image"]
#             image_ext = base_image["ext"]
#
#             # 保存图像到文件
#             image_path = os.path.join(output_folder, f"page{page_number + 1}_img{img_index + 1}.{image_ext}")
#             with open(image_path, "wb") as img_file:
#                 img_file.write(image_bytes)
#             image_paths.append(image_path)
#
#     pdf_document.close()
#     return image_paths
#
#
# def insert_images_to_word(image_paths, output_word_path):
#     """
#     将提取的图像插入到 Word 文档中。
#     """
#     doc = Document()
#     doc.add_heading("Extracted Images from PDF", level=1)
#
#     for image_path in image_paths:
#         doc.add_paragraph(f"Image: {os.path.basename(image_path)}")
#         doc.add_picture(image_path, width=Inches(5))  # 调整宽度
#
#     doc.save(output_word_path)
#     print(f"Word document saved at: {output_word_path}")
#
#
# def main():
#     # 输入 PDF 文件路径
#     pdf_path = "经典算法大全.pdf"  # 替换为你的 PDF 文件路径
#     output_folder = "extracted_images"  # 提取图像保存文件夹
#     output_word_path = "2.docx"  # 输出 Word 文件路径
#
#     # 提取图像
#     print("Extracting images from PDF...")
#     image_paths = extract_images_from_pdf(pdf_path, output_folder)
#     print(f"Extracted {len(image_paths)} images.")
#
#     # 插入图像到 Word
#     print("Inserting images into Word document...")
#     insert_images_to_word(image_paths, output_word_path)
#
#
# if __name__ == "__main__":
#     main()


from pdf2image import convert_from_path
from docx import Document
from docx.shared import Inches
import os
from PIL import ImageFile
from PIL import Image
import streamlit as st
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None




def insert_images_to_word(image_paths, output_word_path):
    """
    将图像插入到 Word 文档中，每页一个图像。
    """
    doc = Document()
    #doc.add_heading("PDF to Word with Images", level=1)

    for i, image_path in enumerate(image_paths):
        #doc.add_paragraph(f"Page {i+1}:")
        doc.add_picture(image_path, width=Inches(6))  # 可调整宽度
        doc.add_paragraph("\n")  # 添加空行

    doc.save(output_word_path)
    st.write(f"Word document saved at: {output_word_path}")

def main():
    st.title('png转word工具')
    images_paths=[]#存图像路径
    uploaded_files = st.file_uploader("请选择文件:", accept_multiple_files=True, type=["PNG","JPG"])
    if st.button('图像传输完毕,点我开始生成word文件'):
        if uploaded_files:
            for uploaded_file in uploaded_files:
                images_paths.append(uploaded_file.name)
            #if 'text_input_active' not in st.session_state:
            st.session_state['text_input_active'] = True
            st.session_state['output_word_path'] = None
            st.session_state['image_paths']=images_paths
        else:
            st.write("尚未传输图像")

    if st.session_state.get('text_input_active', False):
        output_word_path = st.text_input(label='重命名你要生成word文档的名字', value='None')
        # 处理用户输入
        if output_word_path and output_word_path != 'None':
            st.session_state['output_word_path'] = output_word_path
            st.session_state['text_input_active'] = False  # 禁用输入框，表示流程完成
            # 显示用户的最终输入结果
    if st.session_state.get('output_word_path'):
        st.write(f"生成的文件名是: {st.session_state['output_word_path']}")
        st.write('您的输入是', output_word_path)
        output_word_path += ".docx"  # 输出 Word 文件路径
        st.write("Inserting images into Word document...")
        insert_images_to_word(st.session_state['image_paths'], output_word_path)
        del st.session_state['output_word_path']

    # output_word_path = "output.docx"  # 输出 Word 文件路径
    #
    # st.write("Inserting images into Word document...")
    # insert_images_to_word(images_paths, output_word_path)

main()

# def pdf_to_images(pdf_path, output_folder):
#     """
#     将 PDF 的每一页转换为图像并保存到指定文件夹。
#     """
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # 转换 PDF 每一页为图像
#     images = convert_from_path(pdf_path, dpi=300)
#     image_paths = []
#
#     for i, image in enumerate(images):
#         image_path = os.path.join(output_folder, f"page_{i+1}.png")
#         image.save(image_path, "PNG")
#         image_paths.append(image_path)
#
#     return image_paths
#
# def insert_images_to_word(image_paths, output_word_path):
#     """
#     将图像插入到 Word 文档中，每页一个图像。
#     """
#     doc = Document()
#     #doc.add_heading("PDF to Word with Images", level=1)
#
#     for i, image_path in enumerate(image_paths):
#         #doc.add_paragraph(f"Page {i+1}:")
#         doc.add_picture(image_path, width=Inches(6))  # 可调整宽度
#         doc.add_paragraph("\n")  # 添加空行
#
#     doc.save(output_word_path)
#     print(f"Word document saved at: {output_word_path}")
#
# def main():
#     # 输入 PDF 文件路径
#     pdf_path = "林柏丞信息安全.pdf"  # 替换为你的 PDF 文件路径
#     output_folder = "pdf_images"  # 存放图像的文件夹
#     output_word_path = "1111.docx"  # 输出 Word 文件路径
#
#     # PDF 转图像
#     print("Converting PDF to images...")
#     image_paths = pdf_to_images(pdf_path, output_folder)
#     print(f"Converted {len(image_paths)} pages to images.")
#
#     # 图像插入 Word
#     print("Inserting images into Word document...")
#     insert_images_to_word(image_paths, output_word_path)
#
# if __name__ == "__main__":
#     main()
