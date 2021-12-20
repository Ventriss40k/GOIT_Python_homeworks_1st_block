path = "bin.txt"
users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
# def save_credentials_users(path, users_info):
#     to_write = ""
#     with open (path,"wb") as fh:
#         for i,j in users_info.items():
#             to_write = i+":"+j+"\n"
#             to_write = 
#         print(to_write.encode())




def save_credentials_users(path, users_info):
    username_password = ""
    result = ""
    with open(path, 'wb') as fh:
        for key, val in users_info.items():
            username_password = f"{key}:{val}"
            result = fh.write((username_password + "\n").encode())
    return result
save_credentials_users(path, users_info)