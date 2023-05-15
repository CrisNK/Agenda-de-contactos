import os
import random

CARPETA = 'Proyecto/Contactos/'

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

# Funciones principales
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
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
# Funciones secundarias
def create_contact():
    print('*--------* Crear contacto *--------*')
    contact_id = random.randint(1000, 9999)
    print(contact_id)
    name = input('Ingrese el nombre del contacto: ')
    
def read_contact():
    print('Read contact')
def update_contact():
    print('Update contact')
def delete_contact():
    print('Delete contact')
def search_contact():
    print('Search contact')

main()