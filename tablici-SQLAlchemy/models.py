from mongoengine import *
 
connect(
    db="web14",
    host="mongodb+srv://web14user:pythonCourse2023@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority",
)
 
 
class Task(Document):
    completed = BooleanField(default=False)
    consumer = StringField()
    meta = {"collection": 'tasks'}