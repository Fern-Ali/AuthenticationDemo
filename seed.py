from models import User, db
from app import app
import datetime
# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add Base Pets
whiskey = User(username='Whiskey', password='$2b$12$Rv7Dyl5iybUfxXf2mMIhdu7KJ3u6YGJJ7ZgISwdafjCvzANmui8Vi', first_name='Alicia', last_name='Jones', email="test@example.net")
bowser = User(username='Bowser', password='$2b$12$Rv7Dyl5iybUfxXf2mMIhdu7KJ3u6YGJJ7ZgISwdafjCvzANmui8Vi', first_name='Johny', last_name='Walker', email="test@example.net" )
spike = User(username='Spike', password='$2b$12$Rv7Dyl5iybUfxXf2mMIhdu7KJ3u6YGJJ7ZgISwdafjCvzANmui8Vi', first_name='Pritti', last_name='Prashad', email="test@example.net" )

## Add Base Dummy Post

#dummy_post = Post(title="It's a Dummy", content="I'm a post, and I'm a dummy!", user_id=1)
#dummy_post2 = Post(title="It's a Dummy", content="I'm a post, and I'm a dummy!", user_id=2)
#dummy_post3 = Post(title="It's a Dummy", content="I'm a post, and I'm a dummy!", user_id=3)

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# Commit--otherwise, this never gets saved!
db.session.commit()

## create / commit post after users are created so that the user_id of 1 is valid upon post creation
#db.session.add(dummy_post)
#db.session.add(dummy_post2)
#db.session.add(dummy_post3)
#db.session.commit()

