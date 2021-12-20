# ЗАДАЧА
# Функия принимает строку text, проверяет ее на содержание запрещенных слов из списка spam_words, а так же имеет параметр space_around.
# space_around отвечает за то, будет ли искать функция отдельное слово или нет
# Возвращает True если в строке есть хоть одно запрещенноу слово или False, если нет
# Слова должны искаться независимо от их регистра




def is_spam_words(text, spam_words, space_around=False):
    if space_around == True: # Если ищем только отдельные слова
        for word in spam_words:
            test_spam_center = " "+ word + " "
            test_spam_end = " " + word + "."
            # 1.
            if word == text[0: len(word)] and text[len(word):len(word)+1] == " ": # 1. первым словом с пробелом справа,
                return True
            # 2.
            elif test_spam_center in text: # 2. словом по центру, с пробелом справа и слева,
                return True
            # 3. 
            elif test_spam_end in text:    # 3. последним словом, с пробелом слева и точкой справа.
                return True
    elif space_around == False: # Если ищем слово независимо, пишеться ли оно вместе либо отдельно от других слов
        for word in spam_words:
            text = str(text)
            word = str(text)
            if word.lower()in text.lower():
                return True
    return False
            

    





print(is_spam_words("Вот тылох.", ["лох", "сука","нахуй","блять"],True))


