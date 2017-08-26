from views import db
from models import Task
from datetime import date

db.create_all()

db.session.add(Task("Finish this tutorial", date(2017, 8, 28), 10, 1))
db.session.add(Task("Finish scuba course", date(2017, 8, 28), 10, 1))
db.session.add(Task("Begin arduino robotics", date(2017, 8, 28), 10, 1))

db.session.commit()