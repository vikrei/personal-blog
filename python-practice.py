# Module 2 Python practice for the personal blog project

post_title = "A Cozy Corner of the Internet"

post_content = "A short personal post about creativity and everyday thoughts."

tags = ["personal", "thoughts", "creativity"]

comments = [
    "I liked this post!",
    "This was interesting to read."
]

author = "Viktoria"
year = 2026

full_title = post_title + " — by " + author

tag_count = len(tags)
comment_count = len(comments)

print(full_title)
print(post_content)
print("Tags:", tags)
print("Number of tags:", tag_count)
print("Number of comments:", comment_count)
print("Published in:", year)