from http import HTTPStatus

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# @mark.anyio
def test_ping():
    response = client.get('/api/ping')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'success': True, 'message': ''}


def test_create_shorten_url():
    # TODO этот тест и аналогичные падают с ошибкой, полное описание приложил в файле error.txt
    # TODO помогите пожалуйста раобраться
    full_url = 'https://yandex.ru'
    response = client.post(
        '/api/',
        json={
            'full_url': full_url,
        }
    )
    response_data = response.json()
    assert response.status_code == HTTPStatus.CREATED, f'Invalid status code: {response.status_code}'
    assert response_data['full_url'] == full_url


# @mark.anyio
def test_invalid_data_when_create_shorten_url():
    full_url = 'abc123qwerty'
    response = client.post(
        '/api/',
        json={
            'full_url': full_url,
        }
    )
    response_data = response.json()
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, f'{response.status_code}, {response_data}'
    assert len(response_data['detail']) == 1, f'Error detail: {response_data["detail"]}'


def test_empty_batch_upload():
    response = client.post(
        '/api/batch_upload',
        json=[]
    )
    response_data = response.json()
    assert response.status_code == HTTPStatus.CREATED, f'Invalid status code: {response.status_code}'
    assert response_data == {'shorten_url_models': [], 'errors': []}, f'Invalid response: {response_data}'


def test_try_getting_not_valid_url_status():
    response = client.get(
        '/api/abc123/status',

    )
    target_response_data = {
        'detail': [
            {
                'input': 'abc123',
                'loc': [
                    'path', 'shorten_url_id'
                ],
                'msg': 'Input should be a valid integer, unable to parse string as an integer',
                'type': 'int_parsing'
            }
        ]
    }
    response_data = response.json()
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, f'Invalid status code: {response.status_code}'
    assert response_data == target_response_data, f'Invalid response: {response_data}'
