# Nie wybrano żadnego
#
# Przejdź do treści
# Korzystanie z usługi Gmail z czytnikami ekranu
# python
# Wątki
# python zalandoserwis@alektumgroup.pl. Aby wstawić tę sugestię, naciśnij klawisz Tab.
# This is a sample Python script.

from pymongo import MongoClient
import pprint
import certifi
import pymongo
from pymongo.errors import BulkWriteError,CollectionInvalid
ca = certifi.where()
class BAZA_DANYCH:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://ArturO:1234@cluster0.cwnxf.mongodb.net/Kino?retryWrites=true&w=majority",tlsCAFile=ca)
        self.db = self.client['Kino']

    def GUI(self):
        for nazwa_tabeli in ['Film', 'Bilet', 'Miejsca', 'Produkt', 'Sala', 'Seans', 'Zamowienie']:
            operator = False
            print('Nazwa tabeli na ktorej sie operuje:',nazwa_tabeli)
            self.collection = self.db[nazwa_tabeli]
            print('Lista kolekcji:',self.db.list_collection_names())
            while(operator == False):
                print('1.Wyszukiwanie wszystkich obiektów.')
                print('2.Wyszukiwanie obiektu po ID.')
                print('3.Dodawanie obiektu.')
                print('4.Usuwanie obiektu.')
                print('5.Update obiektu.')
                print('6.Stworz nowa kolekcje ze zdefiniowana schema.')
                print('7.Wyjscie.')
                opcja = int(input('Wpisz liczbe od 1 do 7 aby wykonac operacje. Jesli wpiszesz inna liczbe program przejdzie do kolejnej tabeli.'))
                if opcja == 1:
                    for post in self.collection.find():
                        pprint.pprint(post)
                elif opcja == 2:
                    post_id = int(input('Podaj ID obiektu którego poszukujesz.'))
                    pprint.pprint(self.collection.find_one({"_id": post_id}))
                elif opcja == 3:
                    post = {'_id': int(input('Podaj nr. ID.')),
                            str(input('Podaj Wlasciwosc obiektu.')): input('Podaj ceche obiektu.'),
                            str(input('Podaj Wlasciwosc obiektu.')): input('Podaj ceche obiektu.'),
                            str(input('Podaj Wlasciwosc obiektu.')): input('Podaj ceche obiektu.'),
                            str(input('Podaj Wlasciwosc obiektu.')): input('Podaj ceche obiektu.'),
                            str(input('Podaj Wlasciwosc obiektu.')): input('Podaj ceche obiektu.'),}
                    self.collection.insert_one(post)
                elif opcja == 4:
                    requests = [pymongo.DeleteOne({'_id':int(input('Podaj ID obiektu który chcesz usunac.'))})]
                    try:
                        self.collection.bulk_write(requests)
                    except BulkWriteError:
                        pprint.pprint(BulkWriteError.details)
                elif opcja == 5:
                    self.collection.find_one_and_update({'_id':int(input('Podaj ID obiektu ktory chcesz aktualizowac.'))},
                    {"$set": {str(input('Podaj nazwe wlasciwosci ktora updatetujesz.')):input('Podaj wartosc wlasciwosci ktora udatetujesz.')}})
                elif opcja == 6:
                    user_schema = {
                        '_id': {
                            'type': 'integer',
                            'minlength': 1,
                            'required': True,
                        },
                        'imie': {
                            'type': 'string',
                            'minlength': 1,
                            'required': True,
                        },
                        'nazwisko': {
                            'type': 'string',
                            'minlength': 1,
                            'required': False,
                        },
                        'stanowisko': {
                            'type': 'string',
                            'minlength': 1,
                            'required': True,
                        },
                        'obowiazki': {
                            'type': 'string',
                            'minlength': 1,
                            'required': True,
                        },
                        'kontakt': {
                            'type': 'integer',
                            'required': True,
                        },
                    }

                    collection = 'Personel'

                    validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
                    required = []

                    for field_key in user_schema:
                        field = user_schema[field_key]
                        properties = {'bsonType': field['type']}
                        minimum = field.get('minlength')

                        if type(minimum) == int:
                            properties['minimum'] = minimum

                        if field.get('required') is True: required.append(field_key)

                        validator['$jsonSchema']['properties'][field_key] = properties

                    if len(required) > 0:
                        validator['$jsonSchema']['required'] = required

                    try:
                        self.db.create_collection(collection)
                    except CollectionInvalid:
                        pass
                    collection = self.db['Personel']
                    post1 = {'_id': int(input('Podaj nr. ID.')),
                            'imie': str(input('Podaj ceche obiektu imie.')),
                            'nazwisko': str(input('Podaj ceche obiektu nazwisko.')),
                            'stanowisko': str(input('Podaj ceche obiektu stanowisko.')),
                            'obowiazki': str(input('Podaj ceche obiektu obowiazki.')),
                            'kontakt': int(input('Podaj ceche obiektu kontakt.')), }
                    try:
                        collection.insert_one(post1)
                    except AttributeError:
                        print('Nieprawidlowa wartosc schemy.')
                    #output: AttributeError: 'str' object has no attribute 'insert_one'
                elif opcja == 7:
                    exit(1)
                else:
                    operator = True

            # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = BAZA_DANYCH()
x.GUI()
