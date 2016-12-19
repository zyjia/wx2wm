# -*- coding:utf-8 -*-

import qrcode
import web
import time
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding('utf8')

urls = (
    '/', 'Index'

)
render = web.template.render('templates')

def code(info):
    qr = qrcode.QRCode(
        version = 1,    #二维码的大小12*12
        error_correction = qrcode.constants.ERROR_CORRECT_H, #二维码容错率，容错率越高，越容易被识别，中间的图片可以设置越大，二维码越密集；容错率最小，中间不能内嵌图片，二维码稀疏
        box_size = 10,
        border = 4,
    )
    qr.add_data(
        '''
        BEGIN:VCARD\n
        VERSION:3.0\n
        FN:%s\n             #名字
        ORG:%s\n            #公司
        TITLE:%s\n          #职位
        ADR;WORK:%s\n       #地址
        TEL;WORK:%s\n       #联系电话
        EMAIL;WORK:%s\n     #邮箱
        URL:%s\n            #个人主页
        NOTE:%s\n           #备注
        END:VCARD
        ''' % (info['name'], info['company'], info['title'], info['address'], info['mobile'], info['email'], info['url'],info['desc'])
    )   #添加数据
    img = qr.make_image()   #创建二维码
    img = img.convert("RGBA")   #转换为黑白格式
    icon = Image.open("static/images/logo1.png")    #打开图片
    img_w, img_h = img.size #二维码宽高
    n = 4
    size_w = int(img_w/n)   #size是Logo图片的宽和高
    size_h = int(img_w/n)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_w
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int(img_w-icon_w)/2
    h = int(img_h-icon_h)/2
    img.paste(icon, (w,h), icon)
    path = "static/CardImg/%s.png" % time.time()
    img.save(path)
    return path

class Index(object):
    def GET(self):
        return render.index()
    def POST(self):
        print web.input()
        return code(web.input()) #返回图片地址

if __name__ == '__main__':
    web.application(urls, globals()).run()