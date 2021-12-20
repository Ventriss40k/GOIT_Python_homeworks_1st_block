# Задача:
# сделать так что бы во воходящем тексте первые буквы в предложении были заглавными. Окончанием предложения считаеться . ? !
# Разделить на предложения текст
# Выделить первое слово в каждом предложении, сделать его с заглавной
# Приделать первое слово обратно к предолжению
# Собрать предложения обратно


def capital_text(s):
    # ----------------Разделить на предложения текст
    s = s + '.' # Добавить точку в конце, что бы последний кусок текста был предложением даже если там нет знака пирпенания в конце
    count_start =0
    count_end = 0
    sentences = []
    for i in s:
        count_end+=1
        if i in ".!?":
            sentence=str(s[count_start:count_end]).strip()
            sentences.append(sentence)
            count_start = count_end
    # ------------Выделить первую букву в предложении, сделать ее заглавной
    new_sentences = []
    for i in sentences:
        print(i)
        sentence1 = str(i[0:1]).upper()
        sentence2 = str(i[1:])
        sentence = sentence1+sentence2
        new_sentences.append(sentence)
        s = " ".join(new_sentences)
        s = str(s[0:len(s)-1]) # убираем последний символ (точку)
        # sentence = str(i[0:1]).upper + str(i[1:])
        # new_sentences.append(sentence)
    return s


s = 'alert. boss! oh'
capital_text(s)