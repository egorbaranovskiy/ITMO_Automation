# class Button:
#
#
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
# home = Button('Домой', '/home')
# catalog_msk = Button ('Каталог','/msk/catalog')
#
# print(home.text)
# print ('Кнопка' + home.text + 'имеет ссылку' + home.link)
#
# print('\n')
#
# print (catalog_msk.text)
# print('Кнопка' + catalog_msk.text + 'имеет ссылку' + catalog_msk.link)
from re import search


# class Input:
#     def __init__(self, loc):
#         self.loc = loc
#
# search = Input('input#search')
#
# print(search.loc)



class Page:
    def __init__(self, url):
        self.url = url

def get(self):
    print(self.url)

home = Page('https://demoqa.com/')
home.get()
