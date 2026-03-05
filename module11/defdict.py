


class DefaultDict:
    def __init__(self, default_type):
        self.collection = {}
        self.default_type=default_type
    
    def __getitem__(self, key):
        if key in self.collection:
            return self.collection[key]
        
        value = self.default_type()
        self.collection[key] = value
        return value
        

    def __setitem__(self, key, value):
        pass
    

        

d = DefaultDict(list)
print(d["asd"])