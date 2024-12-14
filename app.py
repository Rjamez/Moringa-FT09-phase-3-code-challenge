from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine
from models.tag import Tag # type: ignore

# Create sample authors  
author1 = Author(id=1, name="Jane Doe")  

# Create sample magazines  
magazine1 = Magazine(id=1, name="Tech Times", category="Technology")  

# Create a sample article  
article1 = Article(author=author1, magazine=magazine1, title="The Future of Tech")  

# Now you can add print statements or logic to verify the created instances  
print(f"Author: {author1.name}, Magazine: {magazine1.name}, Article: {article1.title}")

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Create an author
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
        author_id = cursor.lastrowid 

        # Create a magazine
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
        magazine_id = cursor.lastrowid 

        # Create an article
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (article_title, article_content, author_id, magazine_id))

        conn.commit()

        # Query the database for inserted records. 
        # The following fetch functionality should probably be in their respective models

        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()

        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()

        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()

        # Display results
        print("\nMagazines:")
        for magazine in magazines:
            print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

        print("\nAuthors:")
        for author in authors:
            print(Author(author["id"], author["name"]))

        print("\nArticles:")
        for article in articles:
            print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()

    finally:
        conn.close()

if __name__ == "__main__":
    main()