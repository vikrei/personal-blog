# Classes for representing blog posts and comments

class BlogPost:
    def __init__(self, title, content, tags):
        self.title = title
        self.content = content
        self.tags = tags

    def display_post(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Tags: {', '.join(self.tags)}")

class Comment:
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def display_comment(self):
        print(f"Author: {self.author}")
        print(f"Text: {self.text}")

        