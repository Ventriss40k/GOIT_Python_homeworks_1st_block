def solve_riddle(riddle, word_length, start_letter, reverse=False):
    result =""
    if reverse == False:
        result = riddle[riddle.find(start_letter):riddle.find(start_letter)+word_length]
        return result
    elif reverse == True:
        result = riddle[riddle.find(start_letter)-(word_length-1):riddle.find(start_letter)+1]
        result = result[::-1]
        return result
    
# "mi1pow|per|et"
# riddle = "mi1powperet"
# word_length = 3
# start_letter = "r"



# print(solve_riddle(riddle, word_length, start_letter, reverse=True))