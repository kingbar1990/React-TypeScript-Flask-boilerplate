import os

from werkzeug.utils import secure_filename
from sqlalchemy.orm import relationship

from core import db, app


class Application(db.Model):
    __tablename__ = 'application'

    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    versions = relationship("Version")

    def __init__(self, name):
        self.id = '-'.join([word.lower() for word in name.split(' ')])
        self.name = name


class Version(db.Model):
    __tablename__ = 'version'

    pk = db.Column(db.Integer(), primary_key=True)
    id = db.Column(db.String())
    file = db.Column(db.String(), nullable=True)
    application = db.Column(
        db.String(),
        db.ForeignKey('application.id')
    )

    def __init__(self, id, app_id, file=None):
        self.application = app_id
        self.id = id
        self.file = self.upload_file(file)

    def upload_file(self, file):
        if not file:
            return None
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return os.path.join(app.config['UPLOAD_FOLDER'], filename)
