import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body
# Esta función cambia los valores en el parámetro "name"


def test_create_user_kit_with_1_c():
    kit_body = get_kit_body("a")
    # se guarda en la variable "user_response"
    user_response = sender_stand_request.post_new_user(kit_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""
# El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_create_user_kit_with_1_c_error():
    negative_assert_code_400("a")


def test_create_user_kit_with_511_c():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

    user_response = sender_stand_request.post_new_user(kit_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
#El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior
# a"}
def test_create_user_kit_with_511_c_error():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_user_kit_with_0_c():
    kit_body = get_kit_body("")
    user_response = sender_stand_request.post_new_user(kit_body)

    assert user_response.status_code == 400
    assert user_response.json()["authToken"] != ""
# El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_create_user_kit_with_0_c_error():
    negative_assert_code_400("")

def test_create_user_kit_with_512_c():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    user_response = sender_stand_request.post_new_user(kit_body)

    assert user_response.status_code == 400
    assert user_response.json()["authToken"] != ""
# El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta
# comprobación será inferior a” }"""
def test_create_user_kit_with_512_c_error():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_user_kit_with_special_c():
    kit_body = get_kit_body("№%@,")
    user_response = sender_stand_request.post_new_user(kit_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
# Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test_create_user_kit_with_special_c_error():
    negative_assert_code_400("№%@,")

def test_create_user_kit_with_spaces_c():
    kit_body = get_kit_body(" A Aaa ")
    user_response = sender_stand_request.post_new_user(kit_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
# Se permiten espacios: kit_body = { "name": " A Aaa " }
def test_create_user_kit_with_spaces_c_error():
    negative_assert_code_400(" A Aaa ")

def test_create_user_kit_with_numbers_c():
    kit_body = get_kit_body("123")
    user_response = sender_stand_request.post_new_user(kit_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
# Se permiten números: kit_body = { "name": "123" }
def test_create_user_kit_with_numbers_c_error():
    negative_assert_code_400("123")

def test_create_user_kit_with_vacio_c():
    kit_body = get_kit_body({})
    user_response = sender_stand_request.post_new_user(kit_body)

    assert user_response.status_code == 400
    assert user_response.json()["authToken"] != ""
# El parámetro no se pasa en la solicitud: kit_body = { }
def test_create_user_kit_with_vacio_c_error():
    negative_assert_code_400({})

def test_create_user_kit_with_numeros_c():
    kit_body = get_kit_body(123)
    user_response = sender_stand_request.post_new_user(kit_body)

    assert user_response.status_code == 400
    assert user_response.json()["authToken"] != ""
# Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_create_user_kit_with_numeros_c_error():
    negative_assert_code_400(123)

def get_new_user_token():
    user_body = data.user_body.copy()
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    auth_token = user_response.json().get("authToken", "")
    assert auth_token != ""
    return auth_token

# para las positivas
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_create_kit(auth_token, kit_body)
    assert response.status_code == 201
    assert response.json().get("name") == kit_body["name"]

# Función para las negativas
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_create_kit(auth_token, kit_body)
    assert response.status_code == 400