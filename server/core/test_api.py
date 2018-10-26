import json

import pytest
from core import db
from core.models import Application, Version
from core.views import app


@pytest.fixture
def client(request):
    """ Create test Client """
    test_client = app.test_client()
    return test_client


def post_json(client, url, json_dict):
    """ Send dict to url as json """
    return client.post(
        url,
        data=json.dumps(json_dict),
        content_type='application/json'
        )


def json_response(response):
    """ Convert json response """
    return json.loads(response.data.decode('utf8'))


def test_get_apps(client):
    response = client.get('/apps')
    id = Application.query.first().id

    assert response.status_code == 200
    assert json_response(response)[0]['id'] == id


def test_get_app(client):
    id = Application.query.first().id
    response = client.get('/apps/{}'.format(id))
    assert json_response(response)['id'] == id


def test_get_app_version(client):
    id = Version.query.first().application
    version = Version.query.first().id
    response = client.get('/apps/{}/{}'.format(id, version))

    assert response.status_code == 200
    assert json_response(response)[0]['id'] == version


def test_post_app(client):
    name = 'Safari broser'
    response = client.post('/apps', data={'name': name})
    assert response.status_code == 201
    obj = db.session.query(Application).filter(Application.name == name).first()
    assert json_response(response)['id'] == obj.id
    db.session.delete(obj)
    db.session.commit()


def test_post_version(client):
    id = Application.query.first().id
    version_id = '12.0.112'
    response = client.post(
        '/apps/{}/{}'.format(id, version_id),
        data=json.dumps({'app_id': id, 'version_id': version_id})
    )
    obj = db.session.query(Version).filter(Version.id == version_id).first()
    assert json_response(response)['id'] == obj.id
    assert response.status_code == 201
    db.session.delete(obj)
    db.session.commit()
