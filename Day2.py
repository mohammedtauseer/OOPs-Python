# Class and object

class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []   # list of strings

    def display_title(self):
        print("The title of the reel is:", self.title)

    def display_description(self):
        print("The description of the reel is:", self.description)

    def display_creator(self):
        print("The creator of the reel is:", self.creator_name)

    def display_location(self):
        print("The location of the reel is:", self.location)

    def display_likes(self):
        print("The likes of the reel is:", self.likes)

    def display_comments(self):
        print("Comments on the reel:")
        if not self.comments:
            print("No comments yet")
        else:
            for comment in self.comments:
                print("-", comment)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)
    def remove_comment(self):
        temp=self.comments.pop()
        print("Removed comment:", temp)



# Object creation
reel1 = Instagram(
    "dancing",
    "dancing with friends",
    "Alice",
    "Mumbai"
)

reel1.disliked()   # 0
reel1.liked()      # 1
reel1.add_comment("Amazing dance!")
reel1.add_comment("Loved the vibe")


reel2 = Instagram(
    "finance minister conference",
    "finance minister conference with friends",
    "Bob",
    "Delhi"
)

reel1.liked()      # 2
reel2.liked()      # 1
reel1.disliked() 


reel1.display_likes()
reel2.display_likes()

reel1.display_creator()
reel1.display_location()
reel1.display_comments()
reel1.remove_comment()
reel1.display_comments()

print(id(reel1))
print(id(reel2))
