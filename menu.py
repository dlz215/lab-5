from peewee import *

"""
A menu - you need to add the database and fill in the functions. 
"""

from peewee import *

db = SqliteDatabase('jugglers.sqlite')

# to create table, classes must be subclass of peewee model class
class Juggler(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.country}, {self.catches}'

db.connect()
db.create_tables([Juggler])    
Juggler.delete().execute()

# create / insert
juggler1 = Juggler(name = 'JANE MUSTONEN', country = 'FINLAND', catches = 98)
juggler1.save()

juggler2 = Juggler(name = 'IAN STEWART', country = 'CANADA', catches = 94)
juggler2.save()

juggler3 = Juggler(name = 'AARON GREGG', country = 'CANADA', catches = 88)
juggler3.save()

juggler4 = Juggler(name = 'CHAD TAYLOR', country = 'USA', catches = 78)
juggler4.save()


def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    for juggler in Juggler.select():
        print(juggler)

def search_by_name():
    juggler_name = input('Enter juggler name: ')
    matching_jugglers = []

    for juggler in Juggler.select():
        if juggler_name.upper() == juggler.name:
            matching_jugglers.append(juggler)

    if matching_jugglers:
        for juggler in matching_jugglers:
            print(juggler)
    else:
        print("no matches found")

def add_new_record():
    name = input('Enter name: ')
    country = input('Enter country: ')
    catches = input('Enter number of catches: ')

    already_in_database = Juggler.select().where(Juggler.name == name.upper() 
        and Juggler.country == country.upper() and Juggler.catches == catches)

    if already_in_database:
        print("Juggler already in database")
    else:
        new_juggler = Juggler(name= name.upper(), country = country.upper(), catches = catches)
        new_juggler.save()

def edit_existing_record():
    id = input("Enter ID of juggler you with to update: ")
    name = input('Enter name: ')
    country = input('Enter country: ')
    catches = input('Enter number of catches: ')
    
    rows_modified = Juggler.update(name = name.upper(), country = country.upper(), catches = catches).where(Juggler.id == id).execute() 

    if rows_modified:
        print('Juggler updated successfully')
    else: 
        print('No juggler found with that ID')

def delete_record():
    id = input("Enter ID of juggler you with to delete: ")

    rows_modified = Juggler.delete().where(Juggler.id == id).execute() 


if __name__ == '__main__':
    main()