from api import Petfriends
from settings import valid_email, valid_password, invalid_email, invalid_password, \
    valid_pet_photo_path, invalid_pet_photo_path, valid_photo_path

pf = Petfriends()

# Позитивный тест для проверки получения API-ключа с действительными данными пользователя
def test_get_api_key_for_valid_user():
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert 'key' in result

# Позитивный тест для проверки получения списка питомцев с действительным ключом
def test_get_all_pets_with_valid_key():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter="all")
    assert status == 200
    assert len(result['pets']) > 0

# Позитивный тест для добавления нового питомца с действительными данными
def test_add_new_pet_with_valid_data():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_name = "Fluffy"
    pet_animal_type = "Cat"
    pet_age = 2
    pet_photo = valid_pet_photo_path
    status, result = pf.add_new_pet(auth_key, pet_name, pet_animal_type, pet_age, pet_photo)
    assert status == 200
    assert 'id' in result

# Позитивный тест для удаления питомца с действительными данными
def test_delete_pet_with_valid_data():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter="my_pets")
    assert status == 200
    assert len(result['pets']) > 0

    pet_id = result['pets'][0]['id']

    status, result = pf.delete_pet(auth_key, pet_id)
    assert status == 200

# Позитивный тест для обновления информации о питомце с действительными данными
def test_update_pet_info_with_valid_data():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter="my_pets")
    assert status == 200
    assert len(result['pets']) > 0

    pet_id = result['pets'][0]['id']
    new_name = "Updated Pet Name"
    new_animal_type = "Updated Animal Type"
    new_age = 3

    status, result = pf.update_pet_info(auth_key, pet_id, name=new_name, animal_type=new_animal_type, age=new_age)
    assert status == 200

# Позитивный тест для добавления фотографии к питомцу с действительными данными
def test_add_photo_to_pet_with_valid_data():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_name = "Fluffy"
    pet_animal_type = "Cat"
    pet_age = 2
    pet_photo = valid_pet_photo_path

    # Добавление нового питомца и получение его ID
    status, result = pf.add_new_pet(auth_key, pet_name, pet_animal_type, pet_age, pet_photo)
    assert status == 200
    assert 'id' in result
    pet_id = result['id']

    # Добавление фотографии к питомцу с полученным ID
    status, result = pf.add_photo_to_pet(auth_key, pet_id, valid_photo_path)
    assert status == 200
    assert 'id' in result

# Негативный тест для проверки получения API-ключа с недействительными данными пользователя
def test_get_api_key_with_invalid_credentials():
    status, result = pf.get_api_key(invalid_email, invalid_password)
    assert status == 403
    assert 'key' not in result

# Негативный тест для получения списка питомцев с недействительным ключом
def test_get_list_of_pets_with_invalid_key():
    invalid_key = "invalid_key"

    status, result = pf.get_list_of_pets({"key": invalid_key}, filter="my_pets")
    assert status == 403
    assert 'pets' not in result

# Негативный тест для добавления нового питомца с недействительными данными
def test_add_new_pet_with_invalid_data():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    invalid_pet_name = ""
    invalid_pet_animal_type = "Invalid Type"
    invalid_pet_age = -1
    invalid_pet_photo = invalid_pet_photo_path

    status, result = pf.add_new_pet(auth_key, invalid_pet_name, invalid_pet_animal_type, invalid_pet_age, invalid_pet_photo)
    assert status == 400
    assert 'id' not in result

# Негативный тест для удаления питомца с недействительными данными
def test_delete_pet_with_invalid_data():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    invalid_pet_id = "invalid_pet_id_here"

    status, result = pf.delete_pet(auth_key, invalid_pet_id)
    assert status == 400

# Негативный тест для обновления информации о питомце с недействительными данными
def test_update_pet_info_with_invalid_data():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    invalid_pet_id = "invalid_pet_id_here"

    status, result = pf.update_pet_info(auth_key, invalid_pet_id, name="Invalid Name")
    assert status == 400
