import random
import string


REGEX_EMAIL = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
REGEX_ONLY_LETTERS = '[A-Za-z]'


def first_name_generator():
    first_name_list = [
        'Emma', 'Jack', 'Mary', 'Jacob', 'Jennifer', 'Thomas', 'Elizabeth', 'Robert', 'Amelia', 'Charlie', 'Lily',
        'James']
    return ''.join([random.choice(first_name_list)])


def last_name_generator():
    last_name_list = [
        'Smith', 'Jones', 'Johnson', 'Wilson', 'Miller', 'Williams', 'Brown', 'Wang', 'Walsh']
    return ''.join([random.choice(last_name_list)])


def email_generator(length=8, digits=False):
    symbols = string.ascii_lowercase + string.digits if digits is True else string.ascii_lowercase
    email = ''.join([random.choice(symbols) for _ in range(length)]) + '@reqres.com'
    return email


def avatar_link_generator(length=5, digits=False):
    symbols = string.ascii_lowercase + string.digits if digits is True else string.ascii_lowercase
    avatar_link = 'https://reqres.in/img/faces/' + ''.join([random.choice(symbols) for _ in range(length)]) + '.jpg'
    return avatar_link

