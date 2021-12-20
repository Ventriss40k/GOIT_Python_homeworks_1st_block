# Задача:
# 1. Функция принимает аргументы text и  spam_word -  текст в который будут вносится правки и список слов, которыее подлежат заменению
# 2. если слово из списка spam_words есть в строке, оно должно быть заменено звездочками * (столько звездочек, сколько букв в слове)
# 3. Нечувствительность к регистру spam_words

import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        word = str(word).upper
    for i in spam_words:
        spam_stars = len(i)*"*"
        text = re.sub(i,spam_stars,text,flags=re.IGNORECASE)
    return text

print(replace_spam_words("Попался, коршун ебучий, сука!", ["ебучий", "сука"]))


