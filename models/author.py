class Author:  
    def __init__(self, id: int, name: str):  
        self._id = id  
        self._name = None  # To store the name from the database  
        self.name = name  # Use the setter to save it to the database  

    @property  
    def id(self) -> int:  
        return self._id  

    @property  
    def name(self) -> str:  
        return self._name  

    @name.setter  
    def name(self, value: str):  
        if isinstance(value, str) and len(value) > 0:  
            self._name = value  
            # Add your database insert logic here to save to authors table  
        else:  
            raise ValueError("Name must be a non-empty string.")  

    def articles(self):  
        # SQL JOIN to get all articles associated with this author  
        pass  

    def magazines(self):  
        # SQL JOIN to get all magazines associated with this author  
        pass