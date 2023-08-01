import requests

class Petfriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru"

    def get_api_key(self, email, password):
        headers = {
            "email": email,
            "password": password
        }
        res = requests.get(self.base_url + "/api/key", headers=headers)
        status = res.status_code
        result = res.json() if status == 200 else res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {"auth_key": auth_key["key"]}
        filter = {"filter": filter}
        res = requests.get(self.base_url + "/api/pets", headers=headers, params=filter)
        status = res.status_code
        result = res.json() if status == 200 else res.text
        return status, result

    def add_new_pet(self, auth_key, name, animal_type, age, pet_photo):
        headers = {"auth_key": auth_key["key"]}
        data = {
            "name": name,
            "animal_type": animal_type,
            "age": age
        }
        files = {"pet_photo": pet_photo}
        res = requests.post(self.base_url + "/api/pets", headers=headers, data=data, files=files)
        status = res.status_code
        result = res.json() if status == 200 else res.text
        return status, result

    def delete_pet(self, auth_key, pet_id):
        headers = {"auth_key": auth_key["key"]}
        res = requests.delete(self.base_url + f"/api/pets/{pet_id}", headers=headers)
        status = res.status_code
        result = res.json() if status == 200 else res.text
        return status, result

    def update_pet_info(self, auth_key, pet_id, name=None, animal_type=None, age=None):
        headers = {"auth_key": auth_key["key"]}
        data = {}
        if name is not None:
            data["name"] = name
        if animal_type is not None:
            data["animal_type"] = animal_type
        if age is not None:
            data["age"] = age
        res = requests.put(self.base_url + f"/api/pets/{pet_id}", headers=headers, data=data)
        status = res.status_code
        result = res.json() if status == 200 else res.text
        return status, result

    def add_photo_to_pet(self, auth_key, pet_id, pet_photo):
        headers = {"auth_key": auth_key["key"]}
        files = {"pet_photo": pet_photo}
        res = requests.post(self.base_url + f"/api/pets/set_photo/{pet_id}", headers=headers, files=files)
        status = res.status_code
        result = res.json() if status == 200 else res.text
        return status, result
