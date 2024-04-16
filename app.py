from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text, font_path, output_path):
    # 打开图片
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # 设置字体和大小
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)

    # 设置水印位置和颜色
    width, height = image.size
    # 使用 textbbox 获取文本边界框
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) / 2
    y = height - text_height - 20
    
    # 添加水印
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # 白色半透明

    # 保存图片
    image.save(output_path)

# 使用示例
add_watermark('image.png', '生活他妈太苦了', 'NotoSansSC-VariableFont_wght.ttf', 'output_image.jpg')
