# multi-level inheritance: each level adds specific behaviour on top of the parent
#
# Content
#     └── Post          (adds likes, publish flow)
#             ├── VideoPost   (adds duration, resolution)
#             └── Article     (adds word count, reading time)


class Content:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.tags = []

    def tag(self, *tags):
        self.tags.extend(tags)
        return self     # allows chaining: post.tag("python", "oop").tag("tutorial")

    def info(self):
        return f'"{self.title}" by {self.author}'


class Post(Content):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.likes = 0
        self.published = False

    def like(self):
        self.likes += 1
        return self

    def publish(self):
        self.published = True
        return self

    def info(self):
        status = "published" if self.published else "draft"
        return f"{super().info()} | {self.likes} likes | {status}"


class VideoPost(Post):
    def __init__(self, title, author, duration_sec, resolution="1080p"):
        super().__init__(title, author)
        self.duration_sec = duration_sec
        self.resolution = resolution

    def info(self):
        minutes = self.duration_sec // 60
        seconds = self.duration_sec % 60
        return f"{super().info()} | {minutes}m{seconds}s | {self.resolution}"


class Article(Post):
    def __init__(self, title, author, word_count):
        super().__init__(title, author)
        self.word_count = word_count

    def reading_time(self):
        return max(1, self.word_count // 200)   # ~200 words per minute

    def info(self):
        return f"{super().info()} | {self.word_count} words (~{self.reading_time()} min read)"


video = VideoPost("Python OOP explained", "john", duration_sec=732)
video.tag("python", "oop").tag("tutorial")
video.like().like().like().publish()
print(video.info())
print(video.tags)

print("--------------------")

article = Article("Why composition beats inheritance", "jane", word_count=1450)
article.tag("architecture").publish().like()
print(article.info())

print("--------------------")

feed = [video, article]
for item in feed:
    print(isinstance(item, Content), isinstance(item, Post), type(item).__name__)
