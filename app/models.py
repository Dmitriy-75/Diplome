from app import db

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)

    firstname = db.Column(db.String(40), index=True)
    lastname = db.Column(db.String(40), index=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    age = db.Column(db.Integer(), nullable=False)
    job = db.Column(db.String(100), nullable=True)
    task = db.relationship('Task',  back_populates='user' )

    def __repr__(self):
        return f'<User {self.username}>'

class Task(db.Model):

    __tablename__ = 'tasks'
    id = db.Column(db.Integer(), primary_key=True)

    title = db.Column(db.String(128))
    content = db.Column(db.String(250))
    priority = db.Column(db.Integer())
    completed = db.Column(db.Boolean())
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    slug = db.Column(db.String(128))
    user = db.relationship('User',  back_populates='task')

    def save(self, *args, **kwargs):
        ''' получение slug из title'''
        if not self.id:
            self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)

    def __repr__(self):
        return f'<Task {self.title}>'