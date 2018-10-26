import os
import werkzeug

from flask_restful import Resource, Api, fields, marshal_with, reqparse
from flask import send_file

from core import app, db
from .models import Application, Version

api = Api(app)

version_resource_fields = {
    'id': fields.String,
    'file': fields.String,
}
application_resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'versions': fields.List(fields.Nested(version_resource_fields))
}

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument(
    'file',
    type=werkzeug.datastructures.FileStorage,
    location='files'
)
parser.add_argument('app_id')
parser.add_argument('version_id')


class Applications(Resource):
    @marshal_with(application_resource_fields)
    def get(self):
        """Return the list of all applications."""
        return Application.query.all()

    @marshal_with(application_resource_fields)
    def post(self):
        """Create and return new application."""
        args = parser.parse_args()
        if Application.query.get(
            '-'.join([word.lower() for word in args.get('name').split(' ')])
        ) is None:
            application = Application(name=args.get('name'))
            db.session.add(application)
            db.session.commit()
            return application, 201

        return None


class App(Resource):
    @marshal_with(application_resource_fields)
    def get(self, app_id):
        """Return application by id."""
        return Application.query.get(app_id)


class Files(Resource):
    def get(self, file):
        """Return saved file."""
        file_url = os.path.join(app.config['UPLOAD_FOLDER'], file)
        version = Version.query.filter_by(file=file_url).first()
        if version:
            return send_file(
                os.path.realpath(
                    os.path.join(app.config['UPLOAD_FOLDER'], file)
                ),
                as_attachment=True
            )
        return 404


class Versions(Resource):
    @marshal_with(version_resource_fields)
    def get(self, app_id, version_id):
        """Return all versions of application."""
        return Version.query.filter(
            Version.application == app_id, Version.id == version_id).all()

    @marshal_with(version_resource_fields)
    def post(self, app_id, version_id):
        """Create new version of application, upload file."""
        args = parser.parse_args()
        file = args.get('file', None)
        version = Version.query.filter_by(
            id=version_id, application=app_id).first()
        if version:
            if file:
                version.file = version.upload_file(file)
                db.session.commit()
            return version, 201
        else:
            version = Version(
                id=version_id,
                app_id=app_id,
                file=file
            )
            db.session.add(version)
            db.session.commit()
            return version, 201


api.add_resource(Files, '/files/<file>')
api.add_resource(Applications, '/apps')
api.add_resource(App, '/apps/<app_id>')
api.add_resource(Versions, '/apps/<app_id>/<version_id>')

if __name__ == '__main__':
    app.run()
