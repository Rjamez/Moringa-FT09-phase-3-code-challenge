class Article:  
    def __init__(self, author: Author, magazine: Magazine, title: str):   # type: ignore
        self._author = author  # This should be an Author instance  
        self._magazine = magazine  # This should be a Magazine instance  
        self.title = title  # Use setter to validate and save title  

    @property  
    def title(self) -> str:  
        return self._title  

    @title.setter  
    def title(self, value: str):  
        if isinstance(value, str) and 5 <= len(value) <= 50:  
            self._title = value  
            # Add your database insert logic here to save to articles table  
        else:  
            raise ValueError("Title must be a string between 5 and 50 characters.")  

    @property  
    def author(self) -> author:   # type: ignore
        # SQL JOIN to get the author associated with this article  
        return self._author  

    @property  
    def magazine(self) -> Magazine:   # type: ignore
        # SQL JOIN to get the magazine associated with this article  
        return self._magazine