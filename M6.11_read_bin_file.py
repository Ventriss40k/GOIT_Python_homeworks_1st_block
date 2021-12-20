
path = "bin.txt"  
    
def get_credentials_users(path):
    result = []
    with open (path, "rb") as fh:
        lines = fh.readlines()
        for i in lines:
            result.append(i.decode().removesuffix("\n"))
        print(result)
        return(result)

print(get_credentials_users(path))  