# "Hello, World!" - str to be writen
# "4433555555666110966677755531111 - buttons to be pressed for this
def sequence_buttons(string):
    # dial = (1,11,111,1111,11111,2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999,0)
    dial = ("1","11","111","1111","11111","2","22","222","3","33","333","4","44","444","5","55","555","6","66","666","7","77","777","7777","8","88","888","9","99","999","9999","0")
    symbol = (".",",","?","!",":","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","w","X","Y","Z"," ")
    translate_dict = {}
    for d,s in zip(dial,symbol):
        translate_dict[ord(s)]=d
    # print(translate_dict)
    return (string.upper()).translate(translate_dict)
    
print(sequence_buttons("a"))
