import os
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
import main

def push():
    clear()
    security_check()
    put_button("back",main.back, color='light', small=True)
    tittle = input("文章标题")
    content = textarea("文章内容")
    upload(tittle,content)

    #upload_res = file_upload("please upload what you want to upload:",accept="file/*")

    #with open(upload_res.get('filename'),mode='xb') as f:
    #    f.write(upload_res.get('content'))
    #clear()
    #print('what you uploaded is:',upload_res.get('filename'))

def upload(tittle,content):
    with open(f"{tittle}.txt",'w', encoding='utf-8') as af:
        af.write(content)


def security_check():
    passwd = input('输入密码')
    if passwd == '1318':
        pass
    else:
        push()