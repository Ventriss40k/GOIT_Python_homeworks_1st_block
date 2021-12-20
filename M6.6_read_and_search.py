path="recipes.txt"
search_id="60b90c3b13067a15887e1ae4"
def get_recipe(path, search_id):
    with open(path,"r") as fh:
        while True:
            line =fh.readline()
            if search_id in line:
                line = line.split(",")
                line[4] = line[4][0:int(len(line[4])-1)]
                # print(f"Line found: {line}")
                result = {"id":line[0],"name":line[1],"ingredients":line[2:]}
                print(result)
                return result
            if not line:
                return None

{'id': '60b90c3b13067a15887e1ae4', 'name': 'Watermelon Cucumber Salad', 'ingredients': ['1 large seedless watermelon', '12 leaves fresh mint', '1 cup crumbled feta cheese']}
{'id': '60b90c3b13067a15887e1ae4', 'name': 'Watermelon Cucumber Salad', 'ingredients': ['1 large seedless watermelon', '12 leaves fresh mint', '1 cup crumbled feta chees']}





get_recipe(path,search_id)
# 1. сделать словарь 
# id: line[0] name: line[1] ingredients: (line [2:len(line)-1]+line[4][0:int(len(line[4])-2)])
        
        