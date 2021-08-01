import requests


base_url = 'https://petstore.swagger.io/v2/pet'
pet_id = 86401
headers = {
    'Content-type': 'application/json',
    'accept': 'application/json'
}
delete_headers = {
    'Content-type': 'application/json',
    'api_key': 'special-key'
}
pet_data = {
    "id": pet_id,
    "category": {
        "id": 1,
        "name": "small"
    },
    "name": "Chirag's doggie",
    "photoUrls": [
        "https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/04/12185602/Lagotto-Romangolo-Tongue-Out.jpg"
    ],
    "tags": [
        {
            "id": 11,
            "name": "brown"
        }
    ],
    "status": "available"
}


def test_add_pet():
    response = requests.post(base_url, json=pet_data, headers=headers)
    assert response.status_code == 200


def test_find_pet():
    response = requests.get(f"{base_url}/{pet_id}")
    assert response.status_code == 200
    assert response.json().get('id') == pet_id
    assert response.json().get('name') == "Chirag's doggie"
    assert response.json().get('status') == "available"


def test_update_pet_name():
    new_data = pet_data.copy()
    new_data['name'] = "Chirag's doge"
    response = requests.put(base_url, json=new_data, headers=headers)
    assert response.status_code == 200
    assert response.json().get('id') == pet_id
    assert response.json().get('name') == "Chirag's doge"


def test_delete_pet():
    response = requests.delete(f"{base_url}/{pet_id}", headers=delete_headers)
    assert response.status_code == 200
    assert response.json().get('message') == str(pet_id)

