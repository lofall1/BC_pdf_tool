
# import fitz  # PyMuPDF库
# from docx import Document
# import docx
# from docx.shared import Cm
#
# # 打开PDF文件
# pdf_path = '1.pdf'
# pdf_document = fitz.open(pdf_path)
# doc=Document()
# # 初始化文本和图像列表
# texts = []
# images = []
#
# # 遍历PDF的每一页
# for page_num in range(len(pdf_document)):
#     page = pdf_document.load_page(page_num)
#     text = page.get_text()  # 获取页面文本
#     images.extend(page.get_images())  # 获取页面图像
#     texts.append(text)
#
# # # 关闭PDF文档
# # pdf_document.close()
#
# # 打印结果
# print("Texts:")
# doc.add_paragraph(texts)
# for t in texts:
#     print(t)
# print("\nImages:")
# i=1
# for img in images:
#     pix=fitz.Pixmap(pdf_document,img[0])
#     if pix.n >= 5:  # CMYK: convert to RGB first
#         pix = fitz.Pixmap(fitz.csRGB, pix)
#     img_path=f"{pdf_path}{i}.png"
#     pix._writeIMG(img_path,1,None)
#     doc.add_picture(img_path,width=Cm(20),height=Cm(23))
#     print(img)
# doc.save("林柏丞信息安全.docx")

from PIL import Image
import pytesseract
import fitz
import cv2

pdf_file_path = "1.pdf"

pdf_document = fitz.open(pdf_file_path)

scale_factor = 2

ocr_language = 'chi_sim'

for page_number in range(pdf_document.page_count):
    page = pdf_document.load_page(page_number)

    pix = page.get_pixmap(dpi=300)

    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    image_file_name = f"page_{page_number + 1}.png"

    img.save(image_file_name)

    img1 = cv2.imread(f"page_{page_number + 1}.png", 0)

    text = pytesseract.image_to_string(img1, lang=ocr_language, config='--psm 4')

    text_file_name = f"page_{page_number + 1}.txt"

    with open(text_file_name, "w", encoding="utf-8") as text_file:
        text_file.write(text)

pdf_document.close()