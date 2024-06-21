import configuration
import requests
import data

def post_new_user(body):  #devuelve el token #Crear un nuevo usuario #(con el primer print muestra el estado de la solicitud y con el segundo se convierte en diccionario)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def post_create_kit(auth_token, kit_body):
    headers = data.headers.copy()
    headers["Authorization"]: f"Bearer {authToken}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         hearders=headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH)

response = get_users_table()
print(response.status_code)