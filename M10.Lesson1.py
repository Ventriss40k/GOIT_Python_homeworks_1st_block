from collections import UserDict

class SmartDict(UserDict):
    def val_in_dict(self,value):
        if value in self.keys():
            print("in keys")
        if value in self.values():
            print("in values")
        else:
            print("no value in dict")

dict1 = {"a":1, "b":2}
dict1 =SmartDict()
print(dict1.val_in_dict("a"))
         