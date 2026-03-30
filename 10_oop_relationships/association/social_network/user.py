from message import Message

class User:

    def __init__(self, name):
        self.name = name
        self.followers = []
        self.following = []
        self.messages = []

    def follow(self, user):
        self.following.append(user)
        user.followers.append(self)
        return self.following
    
    def send_message(self, content, timestamp):
        message = Message(self, content, timestamp)
        return self.messages.append(message)
