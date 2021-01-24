import re
import sys


def validate_phone_number(phone_number):
    num_regex = '((([0](55|77|99|98|91))|(55|77|99|98|91))([0-9]{6}|[\ ][0-9]{6}|[\ ][0-9]{3}[\ ][0-9]{3}|[\ ][0-9]{2}[\ ][0-9]{2}[\ ][0-9]{2}|[\ ][0-9]{3}[\-][0-9]{3}|[\ ][0-9]{2}[\-][0-9]{2}[\-][0-9]{2}))'
    if re.search(num_regex, phone_number):
        print('True')
    else:
        print('False')


def validate_email(email):
    email_regex = '([a-z0-9\.+]+[@][a-z]*[\.][a-z]*[\.]?[a-z]*)'
    if re.search(email_regex, email):
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    commands = {
        'phone_number': validate_phone_number,
        'email': validate_email
    }

    func = commands.get(sys.argv[1])

    if func:
        func(sys.argv[1], sys.argv[2])
    else:
        print('No such method.')
