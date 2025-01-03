# In models/article.py
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id  # Use author_id (foreign key) here
        self.magazine_id = magazine_id  # Use magazine_id (foreign key) here

    def __repr__(self):
        return f"Article(id={self.id}, title='{self.title}', content='{self.content}', author_id={self.author_id}, magazine_id={self.magazine_id})"
