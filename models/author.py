# In models/author.py
class Author:  
    def __init__(self, name):  
        self.name = name  

def main():  
    author_name = input("Enter author's name: ")  
    magazine_name = input("Enter magazine name: ")  
    magazine_category = input("Enter magazine category: ")  
    article_title = input("Enter article title: ")  
    article_content = input("Enter article content: ")  

    author = Author(author_name)  # Create an Author instance  
    # Additional code to create the Magazine and Article instances...  

if __name__ == "__main__":  
    main()