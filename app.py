from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, output_path, watermark_text, position, font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size=36):
    """
    添加水印到图片上
    :param image_path: 原始图片的路径
    :param output_path: 输出带水印图片的路径
    :param watermark_text: 水印的文本
    :param position: 水印的位置，格式为 (x, y)
    :param font_path: 水印的字体路径，默认为系统字体路径
    :param font_size: 水印的字体大小，默认为36
    """
    try:
        # 使用with语句确保图片文件在操作完成后正确关闭
        with Image.open(image_path) as image:
            draw = ImageDraw.Draw(image)
            # 尝试加载字体文件
            try:
                font = ImageFont.truetype(font_path, font_size)
            except IOError:
                # 如果指定字体加载失败，使用默认字体
                font = ImageFont.load_default()
            text_color = (255, 255, 255)  # 白色
            draw.text(position, watermark_text, font=font, fill=text_color)
            image.save(output_path)
    except Exception as e:
        print(f"An error occurred: {e}")

# 使用示例
add_watermark("image.png", "path_to_output_image.jpg", "Your Watermark", (100, 100))
