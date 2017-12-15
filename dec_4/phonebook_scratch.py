import re
import pickle
try:
    f = open('phonebook.pkl','rb')
    phonebook = pickle.load(f)
except:
    phonebook = {}

print(phonebook)

def create_entry(entry_name):
    first_name = input('What is {}\'s first name? '.format(entry_name))
    last_name = input('What is {}\'s last name? '.format(entry_name))
    phone_number = input('What is {}\'s phone number? '.format(entry_name))
    nickname = input('What is {}\'s nickname? '.format(entry_name))
    phonebook[entry_name] = {}
    phonebook[entry_name]['first_name'] = first_name
    phonebook[entry_name]['last_name'] = last_name
    phonebook[entry_name]['phone_number'] = phone_number
    phonebook[entry_name]['nickname'] = nickname

def search_phonebook():
    return_list = []
    search_by = input('What would you like to search by? Enter key, first name, last name, phone number, or nickname. ').lower()
    if search_by in 'key':
        key = input('Please type in the key exactly. This is case sensitive. ')
        try:
            return_list.append('{} {}\'s phone number is {}. Their nickname is {}.'.format(phonebook[key]['first_name'],phonebook[key]['last_name'],phonebook[key]['phone_number'],phonebook[key]['nickname']))
        except KeyError:
            return 'Entry not found.'
    elif search_by in 'first name':
        query = input('What is the first name of the person you are looking for? ').lower()
        for key in phonebook:
            if phonebook[key]['first_name'].lower() == query:
                return_list.append('{} {}\'s phone number is {}. Their nickname is {}.'.format(phonebook[key]['first_name'],phonebook[key]['last_name'],phonebook[key]['phone_number'],phonebook[key]['nickname']))
    elif search_by in 'last name':
        query = input('What is the last name of the person you are looking for? ').lower()
        for key in phonebook:
            if phonebook[key]['last_name'].lower() == query:
                return_list.append('{} {}\'s phone number is {}. Their nickname is {}.'.format(phonebook[key]['first_name'],phonebook[key]['last_name'],phonebook[key]['phone_number'],phonebook[key]['nickname']))
    elif search_by in 'phone number #':
        query = re.sub('[^0123456789\.]','',input('What is the phone number of the person you are looking for? '))
        for key in phonebook:
            if phonebook[key]['phone_number'] == query:
                return_list.append('{} {}\'s phone number is {}. Their nickname is {}.'.format(phonebook[key]['first_name'],phonebook[key]['last_name'],phonebook[key]['phone_number'],phonebook[key]['nickname']))
    elif search_by in 'nickname':
        query = input('What is the nickname of the person you are looking for? ')
        for key in phonebook:
            if phonebook[key]['nickname'] == query:
                return_list.append('{} {}\'s phone number is {}. Their nickname is {}.'.format(phonebook[key]['first_name'],phonebook[key]['last_name'],phonebook[key]['phone_number'],phonebook[key]['nickname']))

    if return_list:
        return '\n'.join(return_list)
    else:
        return 'Entry not found'

def update_entry(entry_name):
    update_what = input('What would you like to update? Respond first name, last name, phone number, or nickname. ').lower()
    if update_what in 'first name':
        old = phonebook[entry_name]['first_name'][:]
        phonebook[entry_name]['first_name']=input('Enter the new first name: ')
        print('{}\'s first name has been changed from {} to {}.'.format(entry_name,old,phonebook[entry_name]['first_name']))
    elif update_what in 'last name':
        old = phonebook[entry_name]['last_name'][:]
        phonebook[entry_name]['last_name']=input('Enter the new last name: ')
        print('{}\'s last name has been changed from {} to {}.'.format(entry_name,old,phonebook[entry_name]['last_name']))
    elif update_what in 'phone number':
        old = phonebook[entry_name]['phone_number'][:]
        phonebook[entry_name]['phone_number']=input('Enter the new phone number: ')
        print('{}\'s phone number has been changed from {} to {}.'.format(entry_name,old,phonebook[entry_name]['phone_number']))
    elif update_what in 'nickname':
        old = phonebook[entry_name]['nickname'][:]
        phonebook[entry_name]['nickname']=input('Enter the new nickname: ')
        print('{}\'s nickname has been changed from {} to {}.'.format(entry_name,old,phonebook[entry_name]['nickname']))
    else:
        print('I didn\'t understand that, sorry.')
        return update_entry(entry_name)
    return phonebook[entry_name]

def delete_entry(entry_name):
    del phonebook[entry_name]

def command_line_interface(crud):
    if crud in 'retrievesearch':
        print(search_phonebook())
    elif crud in 'create entry':
        entry_name = input('What entry would you like to create? The key is case sensitive. ')
        create_entry(entry_name)
        print('{} has been added to this phonebook.'.format(entry_name))
        return phonebook[entry_name]
    elif crud in 'update entry':
        entry_name = input('What entry would you like to update? Type in the case sensitive key exactly. ')
        return update_entry(entry_name)
    elif crud in 'delete entry':
        entry_name = input('What entry would you like to delete? Type in the case sensitive key exactly. ')
        print('{} has been deleted from this phonebook.'.format(entry_name))
        return delete_entry(entry_name)
    else:
        print('I haven\'t built that functionality yet.')

def phonebook_loop():
    crud = input('What would you like to do? Respond create, retrieve, update, delete, or exit: ').lower()
    while crud not in 'exit':
        command_line_interface(crud)
        crud = input('What would you like to do? Respond create, retrieve, update, delete, or exit: ').lower()
    print('You have exited the program.')

phonebook_loop()
print(phonebook)
output = open('phonebook.pkl', 'wb')
pickle.dump(phonebook, output)
output.close()
