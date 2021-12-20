# ЗАДАЧА:
# 1. Создать словарь TRANS вне функции translate с помощью функции zip
# 2. Функция translate: принимает и возвращает строку; проводит транслитерацию символов на латиницу

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for c,i in zip(CYRILLIC_SYMBOLS,TRANSLATION):
    TRANS[ord(c)]=i
    TRANS[ord(c.upper())]=i.upper()

def translate(name):
    global TRANS
    return str(name).translate(TRANS).title()
print(translate("Иван Григориевич"))
