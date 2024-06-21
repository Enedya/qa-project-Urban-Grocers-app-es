# Proyecto Urban Grocers 

# Este proyecto contiene pruebas para la API de Urban Grocers

## Estudiaremos la creacion de un kit para el usuario (Main.kits)

# Instrucciones:

# 1. Se clonó el repositorio
# 2. Se hizo uso de pycharme para llevar a cabo este proyecto
# 3. se pasó las pruebas por pytest haciendo uso correcto de la funcion separada con el prefijo test.
# 4. La fuente de la documentacion fue apiDoc
# 5. Archivos utilizados: 

# a. configuration.py: contiene las configuraciones basicas como URL y rutas.
# b. create_kit_name_kit_test.py: contiene las pruebas para la creacion de kits de usuario.
# c. data.py: contiene los cuerpos de solicitud utilizados en las pruebas.
# d. sender_stand_request.py: contiene las funciones que envia las solicitudes a la API.
# e.README.md: breve explicacion del proceso
# f. .gitignore: archivos que no se deben mostrar.

## get_kit_body(name): Esta función toma un nombre y lo inserta en el cuerpo de solicitud del kit. Con esta funcion permite reutilizar el mismo cuerpo de solicitud con diferentes nombres en las pruebas.
# get_new_user_token(): Esta función crea un nuevo usuario y devuelve su token de autenticación. Este token es necesario para autorizar las solicitudes. 
# assert user_response.json()["authToken"]: Esta función envía una solicitud de creación de kit con el token de autenticación y el cuerpo del kit proporcionado. Verifica que la respuesta tenga un código de estado 201 (creado) y que el nombre del kit en la respuesta coincida con el del cuerpo de la solicitud.
# negative_assert_code_400(kit_body): Similar a positive_assert, pero verifica que la respuesta tenga un código de estado 400 (solicitud incorrecta).
# test_create_user_kit_with_1_c: inserta en el cuerpo de solicitud y verifica si es correcto el caracter agragado por el usuario