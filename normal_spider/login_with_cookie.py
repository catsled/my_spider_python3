"""使用cookie进行登录"""

import requests
import re

cookies = {
     '_ga':'GA1.2.831014041.1509238038;',
     'anonymid':'j9jxkhl0-r519h1;',
     '_r01_':'1;',
     'depovince':'GW;',
     'jebe_key':'19e7dda5-b70c-4ef5-9295-e73e1a8f9402%7Ccfcd208495d565ef66e7dff9f98764da%7C1509715401976%7C0%7C1510214419112;',
     'jebecookies':'4c60cce9-c620-4e58-b8c2-bd956a05c24b|||||;',
     'ick_login':'e0870f02-9a86-4db2-85a6-82448eea7e4a;',
     '_de':'4F1FF60C280AA48B2CD1201DB4C6DF4A;',
     'p':'f7ec74cb8b208e0213567ac5a5f738ff5;',
     'first_login_flag':'1;',
     'ln_uact':'17173805860;',
     'ln_hurl':'http://head.xiaonei.com/photos/0/0/men_main.gif;',
     't':'8abd5bf35d8585790de8bf40fd406a575;',
     'societyguester':'8abd5bf35d8585790de8bf40fd406a575;',
     'id':'923768535;',
     'xnsid':'5f07f701;',
     'loginfrom':'syshome;',
     'ch_id':'10016;',
     'JSESSIONID':'abc1Zw30nxigqeXCb_G_v',
}

response = requests.get('http://www.renren.com/top', cookies=cookies)
a = re.search(r'迷途', response.content.decode())
print(a.group())