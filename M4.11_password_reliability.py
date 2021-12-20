
# ------------------------------------------------------------------
def is_valid_password(password):
# длинна пароля = 8?
    result = True
    if not len(password) == 8:
            result = False
    if result == True:
        # Содержит 1 хоть малую букву?
        LETTERS ="qwertyuiopasdfghjklzxcvbnm"
        result = False
        for i in password:
            if i in LETTERS:
                result = True
        if result == True:
            # Содержит 1 хоть большую букву?
            result = False
            for i in password:
                if i in LETTERS.upper():
                    result = True
            if result == True:
                # Содержит ли хоть 1 число?
                NUMBERS = "0123456789"
                result = False
                for i in password:
                    if i in NUMBERS:
                        result = True
    return result
    
print(is_valid_password("12345Ff2"))


