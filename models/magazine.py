class Magazine:  
    def __init__(self, name, category=None, id=None):  
        self.id = id
        self.name = name  
        self.category = category  

    def __repr__(self):  
        return f'<Magazine {self.name}>'
