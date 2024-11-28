
import os
import tempfile
import shutil
import comtypes.client
import pythoncom  # 引入 pythoncom 库
import streamlit as st


# 将 PPT 转换为 PDF
def ppt_to_pdf(ppt_path, pdf_path):
    """使用 PowerPoint COM 接口将 PPTX 转换为 PDF"""
    try:
        # 显式初始化 COM 库
        pythoncom.CoInitialize()

        # 初始化 PowerPoint 应用程序
        powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
        powerpoint.Visible = 1  # 设置 PowerPoint 可见（可设置为 0 在后台运行）

        # 打开 PowerPoint 文件
        presentation = powerpoint.Presentations.Open(ppt_path)
        print(f"成功打开 PPT 文件: {ppt_path}")

        # 保存为 PDF 格式
        presentation.SaveAs(pdf_path, 32)  # 32 对应 PDF 格式
        print(f"成功保存 PDF 文件: {pdf_path}")

        # 关闭 PowerPoint 文件
        presentation.Close()
        powerpoint.Quit()

        return True
    except Exception as e:
        print(f"转换失败: {e}")
        return False
    finally:
        # 取消初始化 COM 库
        pythoncom.CoUninitialize()  # 确保 COM 库正确释放


# 删除临时文件夹及其中内容的函数
def delete_temp_files(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


# Streamlit 界面
def main():
    st.title("PPT 转换为 PDF 工具")
    st.write("上传一个 PPT 文件，将其转换为 PDF 文件。")

    # 上传 PPT 文件
    uploaded_file = st.file_uploader("选择一个 PPT 文件", type=["pptx"])

    # 创建临时目录存放文件和存储转换结果
    temp_dir = None
    ppt_path = None
    pdf_path = None

    # 只有在上传新文件时，才执行转换
    if uploaded_file:
        # 创建临时目录存放文件
        temp_dir = tempfile.mkdtemp()

        # 将上传的 PPT 文件保存到临时目录
        ppt_path = os.path.join(temp_dir, uploaded_file.name)
        with open(ppt_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 显示上传的文件名和文件大小
        st.write(f"已上传文件: {uploaded_file.name}")
        st.write(f"文件大小: {uploaded_file.size} 字节")
        st.write('在点击转换为pdf后会自动打开用于转换的ppt文件，属于正常现象')
    # 开始进行 PPT 转换为 PDF 按钮
    if uploaded_file:
        if st.button("开始转换为 PDF"):
            with st.spinner('正在转换文件，请稍候...'):
                try:
                    # 生成 PDF 文件路径
                    pdf_filename = os.path.splitext(uploaded_file.name)[0] + ".pdf"
                    pdf_path = os.path.join(temp_dir, pdf_filename)

                    # 执行转换
                    success = ppt_to_pdf(ppt_path, pdf_path)

                    if success:
                        # 将处理结果保存在 session_state 中
                        st.session_state[uploaded_file.name] = {
                            "pdf_path": pdf_path,
                            "pdf_filename": pdf_filename,
                            "temp_dir": temp_dir  # 保存临时目录路径
                        }

                        st.success("转换完成！")
                    else:
                        st.error("转换失败，请检查文件是否为有效的 PPTX 文件。")

                except Exception as e:
                    st.error(f"转换失败: {e}")

    # 显示下载按钮（如果转换完成）
    if uploaded_file and uploaded_file.name in st.session_state and st.session_state[uploaded_file.name] is not None:
        result = st.session_state[uploaded_file.name]
        pdf_path = result["pdf_path"]
        pdf_filename = result["pdf_filename"]

        # 提供 PDF 文件下载按钮
        with open(pdf_path, "rb") as pdf_file:
            st.download_button("下载转换后的 PDF 文件", pdf_file, file_name=pdf_filename)

        # 清理临时文件夹和文件
        if st.button('点击后清理临时文件，请勿多次点击'):
            delete_temp_files(result["temp_dir"])
            st.write("临时文件夹已删除。")


main()


