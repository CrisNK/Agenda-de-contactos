import os
import random

FOLDER = 'Contactos/'
EXTENSION = '.txt'

class Contact:
    def __init__(self, name, cellphone, category):
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
    print('|        Menu principal      |')
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
    print('*--------* Crear contacto *--------*')
    while True:
        contact_id = random.randint(1000, 9999)
        files = os.listdir(FOLDER) # Función para obtener un diccionario de los archivos contenidos en 'FOLDER'
        if not str(contact_id) + EXTENSION in files:
            break

    contact_name = input('Nombre: ')
    cellphone_number = input('Telefono: ')
    contact_category = input('Categoria: ')

    contact = Contact(contact_name, cellphone_number, contact_category)

    with open(FOLDER + '[' + str(contact_id)+ ']' + EXTENSION, 'w') as file:
        file.write('Nombre: ' + contact.name + '\n')
        file.write('Telefono: ' + contact.cellphone + '\n')
        file.write('Categoria: ' + contact.category + '\n')
    os.system('cls')
    print('¡Contacto creado exitosamente!')
    
def read_contact():
    print('Read contact')
def update_contact():
    print('Update contact')
def delete_contact():
    print('Delete contact')
def search_contact():
    print('Search contact')

main()