"""测试登录验证码的成功率"""

import requests
from PIL import Image
import pytesseract
from io import BytesIO

# 获取图片(拉勾网的注册图片)

img_response = requests.get('https://passport.lagou.com/vcode/create?from=register&refresh=1451121012510')

img_resource = img_response.content

# low 现将图片保存在文件中
with open('login.jpg', 'wb') as fout:
    fout.write(img_resource)

# low 读取图片
image = Image.open('login.jpg')

text = pytesseract.image_to_string(image)

print(text)
