documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
    for numbers in documents:
        if doc_number in numbers['number']:
            return numbers['name']
    return "Документ не найден"
        
def get_directory(doc_number):
    for shelf, directory in directories.items():
        if doc_number in directory:
            return shelf
    return 'Полки с таким документом не найдено'
        

def add(document_type, number, name, shelf_number):
    documents.append({'type': document_type, 'number': number,'name': name})
    directories[str(shelf_number)].append(number)



if __name__ == '__main__':
    get_directory()
    get_name()
    add()


# Аристарх Павлов
# 1
# Документ не найден
# 3
# Александр Пушкин
# Полки с таким документом не найдено