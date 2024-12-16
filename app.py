from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Create the author and magazine objects
    author = Author(author_name)  # Author object is created but not inserted yet
    magazine = Magazine(magazine_name, magazine_category)  # Magazine object is created but not inserted yet

    # Insert the author and magazine into the database (this will assign their IDs)
    author_id = insert_author_into_db(author)  # Insert author and return the generated ID
    magazine_id = insert_magazine_into_db(magazine)  # Insert magazine and return the generated ID

    # Now create the article with the IDs
    article = Article(None, article_title, article_content, author_id, magazine_id)  # Pass the IDs to Article

    # Display results
    print("\nAuthor Details:")
    print(f"ID: {author_id}, Name: {author.name}")

    print("\nMagazine Details:")
    print(f"ID: {magazine_id}, Name: {magazine.name}, Category: {magazine.category}")

    print("\nArticle Details:")
    print(f"ID: {article.id}, Title: {article.title}, Author ID: {article.author_id}, Magazine ID: {article.magazine_id}")


def insert_author_into_db(author):
    # Insert the author into the database and return the generated ID
    # For example, if you're using SQLAlchemy, this could be:
    # session.add(author)
    # session.commit()
    # return author.id
    pass

def insert_magazine_into_db(magazine):
    # Insert the magazine into the database and return the generated ID
    # Similar logic to insert_author_into_db
    pass

if __name__ == "__main__":
    main()
