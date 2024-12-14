class Magazine:  
    def __init__(self, id: int, name: str, category: str):  
        self._id = id  
        self._name = None  # To store the name from the database  
        self._category = None  # To store the category from the database  
        self.name = name  
        self.category = category  

    @property  
    def id(self) -> int:  
        return self._id  

    @property  
    def name(self) -> str:  
        return self._name  

    @name.setter  
    def name(self, value: str):  
        if isinstance(value, str) and 2 <= len(value) <= 16:  
            self._name = value  
            # Add your database insert logic here to save to magazines table  
        else:  
            raise ValueError("Name must be a string between 2 and 16 characters.")  

    @property  
    def category(self) -> str:  
        return self._category  

    @category.setter  
    def category(self, value: str):  
        if isinstance(value, str) and len(value) > 0:  
            self._category = value  
            # Add your database update logic here to save to magazines table  
        else:  
            raise ValueError("Category must be a non-empty string.")  

    def articles(self):  
        # SQL JOIN to get all articles associated with this magazine  
        pass  

    def contributors(self):  
        # SQL JOIN to get all authors associated with this magazine  
        pass  

    def article_titles(self):  
        # Return a list of article titles  
        pass  

    def contributing_authors(self):  
        # Return a list of authors with more than 2 articles  
        pass