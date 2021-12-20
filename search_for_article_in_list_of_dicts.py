articles_dict = [
    {
        "title": "Minim voluptate eu aliqua duis pariatur cupidatat voluptate.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Dolore Lorem aliquip est labore elit labore ex consequat ad occaecat duis.",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "Aliqua minim amet ut pariatur et occaecat esse qui commodo ut duis sunt elit.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "Irure reprehenderit aliquip officia quis occaecat aute mollit laborum ullamco laboris Lorem commodo.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result = []
    if letter_case == True:
        for i in articles_dict:
            if key in i["author"] or key in i["title"]:
                result.append(i)
               
    elif letter_case == False:
        for i in articles_dict:
            if key.lower() in i["author"].lower() or key.lower() in i["title"].lower():
                result.append(i)       
    return result
print(find_articles("Q",False))

    
