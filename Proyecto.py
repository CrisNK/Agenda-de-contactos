import os
import random

FOLDER = 'Contactos/'
EXTENSION = '.txt'

class Contact:
    def __init__(self, id, name, cellphone, category):
        self.id = id
        self.name = name
        self.cellphone = cellphone
        self.category = category   

def main():
    create_directory()
    options = {
        1: create_contact,
        2: read_contact,
        3: update_contact,
        4: delete_contact,
        5: search_contact
    }
    while True:
        display_menu()
        option = int(input(' Seleccione una opción: '))
        if option in options:
            os.system('cls')
            options[option]()
        elif option == 6:
            break
        else:
            os.system('cls')
            print("Error: La opción ingresada no es válida")

def display_menu():
    print('*----------------------------*')
    print('|       Menu principal       |')
    print('*----------------------------*')
    print('| 1) Crear contacto          |')
    print('| 2) Mostrar contacto        |')
    print('| 3) Actualizar contacto     |')
    print('| 4) Eliminar contacto       |')
    print('| 5) Buscar contacto         |')
    print('| 6) Finalizar programa      |')
    print('*----------------------------*')
def create_directory():
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)
# CRUD
def create_contact():
    print('*--------------------------------------*') 
    print('|            Crear contacto            |') 
    print('*--------------------------------------*') 
    while True:
        contact_id = random.randint(1000, 9999)
        files = os.listdir(FOLDER) # Función para obtener un diccionario de los archivos contenidos en 'FOLDER'
        if not str(contact_id) + EXTENSION in files:
            break

    contact_name = input('Nombre: ')
    cellphone_number = input('Telefono: ')
    contact_category = input('Categoria: ')

    contact = Contact(contact_id, contact_name, cellphone_number, contact_category)

    with open(FOLDER + '[' + str(contact_id)+ ']' + EXTENSION, 'w') as file:
        file.write('ID: ' + str(contact.id) + '\n')
        file.write('Nombre: ' + contact.name + '\n')
        file.write('Telefono: ' + contact.cellphone + '\n')
        file.write('Categoria: ' + contact.category + '\n')
    os.system('cls')
    print('¡Contacto creado exitosamente!')
def read_contact():
    print('*---------------------------------------*')
    print('|           Mostrar contactos           |')
    print('*---------------------------------------*')
    files = os.listdir(FOLDER)

    for i, directory in enumerate(files):
        file = open(FOLDER + directory, 'r')
        print(file.read())
        file.close()
    print('*-------------- FIN LISTA -------------*')
    os.system('pause')
def update_contact():
    read_contact()
    files = os.listdir(FOLDER)
    print('*--------------------------------------*') 
    print('|         Actualizar contacto          |') 
    print('*--------------------------------------*') 
    contact_id = input('Ingrese el ID del contacto: ')
    id_exists = os.path.isfile(FOLDER + '[' + contact_id + ']' + EXTENSION)
    if not id_exists:
        os.system('cls')
        print('Sin resultados.')
    else:
        file = open(FOLDER + '[' + contact_id + ']' + EXTENSION, 'w')
        os.system('cls')
        print('Ingreso de nuevos datos a modificar:')
        contact_name = input('Nombre: ')
        cellphone_number = input('Telefono: ')
        contact_category = input('Categoria: ')

        # Instanciar
        contact = Contact(contact_id, contact_name, cellphone_number, contact_category)

        file.write('ID: ' + contact_id + '\n')
        file.write('Nombre: ' + contact.name + '\n')
        file.write('Telefono: ' + contact.cellphone + '\n')
        file.write('Categoria: ' + contact.category + '\n')
        file.close()
        print('¡Contacto actualizado exitosamente!')
def delete_contact():
    read_contact()
    print('*--------------------------------------*') 
    print('|          Eliminar contacto           |') 
    print('*--------------------------------------*') 
    contact_id = input('Ingrese el ID del contacto: ')
    id_exists = os.path.isfile(FOLDER + '[' + contact_id + ']' + EXTENSION)
    if id_exists:
        os.remove(FOLDER + '[' + contact_id + ']' + EXTENSION)
        print('¡Contacto eliminado exitosamente!')
    else:
        os.system('cls')
        print('Sin resultados.')
def search_contact():
    print('*--------------------------------------*') 
    print('|           Buscar contacto            |') 
    print('*--------------------------------------*') 
    contact_name = input('Nombre del contacto a buscar: ').lower()
    files = os.listdir(FOLDER)
    nameFounded = False
    os.system('cls')
    print(f'Listado con la/s persona/s con el nombre: {contact_name}')
    # Acceder a cada archivo de la list creada
    for i, directory in enumerate(files):
        file = open(FOLDER + directory, 'r')
        file.readline() # Utilizado para omitir la lectura del ID, y vaya directo al nombre
        contact_name_in_file = file.readline().lower().split(' ')[1].strip()
        # Verificar que el nombre ingresado sea igual al del archivo
        if contact_name == contact_name_in_file:
            nameFounded = True
            file.seek(0)
            print(file.read())
        file.close()
    if nameFounded:
        os.system('pause')
        os.system('cls')
    else:
        os.system('cls')
        print('Sin resultados')
os.system('cls')
print('         ¡Bienvenido!')
main()