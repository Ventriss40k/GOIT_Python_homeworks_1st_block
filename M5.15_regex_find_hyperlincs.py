# начало гиперссылки может быть http:// или https://
# доменное имя это набор латинских букв, цифр, символов подчеркивания _ и точек .
# символы точек . не могут встречаться рядом
import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"(http:\/\/|https:\/\/)[a-z]+.[a-z]+(.[a-z]+)", text)
    for match in iterator:
        result.append(match.group())
    return result