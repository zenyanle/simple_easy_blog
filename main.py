import os
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
import push_article

class article():
    def __init__(self,tittle,content,number):
        self.tittle = tittle.split('.',1)[0]
        self.content = content
        self.n = number
    def show(self):
        clear()
        put_button("back",back, color='light', small=True)
        put_markdown(f"# {self.tittle}")
        put_markdown(self.content)


def create_article():
    g = os.walk(r"e:\test")
    n = 0
    alist = []
    for path,dir_list,file_list in g:  
        for file_name in file_list:
            with open(r'e:\test\\'+file_name,"r", encoding='utf-8') as af:
                alist.append(article(file_name, af.read(),n+1) )
        n += 1
    return alist

def index_page():
    put_button("upload",push_article.push, color='light', small=True)
    put_markdown("# welcome to my blog")
    put_table(create_list())


def create_list():
    print_list = []
    n = 1
    alist = create_article()
    for target in alist:
        list_in = []
        list_in.append(n)
        list_in.append(span(put_button(target.tittle, alist[n-1].show, color='light', link_style=True)))
        print_list.append(list_in)
        n += 1
    return print_list


def back():
    clear()
    index_page()

def run_blog():
    start_server(index_page, port=8000)


if __name__ == "__main__":
    run_blog()