"""
This module contains functions, that serve users:
`check_access` - decorator function which controls user access to functions;
`get_user_info` - returns user's username depending on their name; decorated by check_access;
`check_perms` - checks permission for user; decorated by check_access.
"""


class CustomError(Exception):
    pass


class AccessDenied(CustomError):
    pass


users = {'olya': 'olya_petryshyn', 'ryan': 'ryan_gosling', 'pavlo': 'pivanchy', 'oleksiy': 'oleksijt'}


def check_access(f):
    def wrapper(*args, **kwargs):
        if args[0] not in users.keys():
            raise AccessDenied('Access denied. User with that name does not exist.')
        return f(*args, **kwargs)
    return wrapper


@check_access
def get_user_info(name):
    return users[name]


@check_access
def check_perms(name):
    return 'Allowed access.'


def main():
    print(get_user_info('olya'))  # prints 'olya_petryshyn'
    try:
        print(get_user_info('sofiia'))  # prints 'Access denied. User with that name does not exist.'
    except AccessDenied:
        print('Access denied. User with that name does not exist.')

    print(check_perms('olya'))  # prints 'Allowed access'
    print(check_perms('ryan'))  # prints 'Allowed access'


main()
