""" This module contents functions, that serve users:

`access_control` - decorator function which controls user access
    to functions;
`get_user_info` - returns user's name. This function
     decorated by access_control function;
`check_perms` - checks permission for user. This function
     decorated by access_control function.
"""

admin_name = 'Oleksiy'


def access_control(func):
    # Decorator function which controls user access to functions
    def wrapper(name):
        try:
            if name == admin_name:
                return func(name)
            else:
                raise PermissionError
        except PermissionError:
            print('Permission denied')
    return wrapper


@access_control
def get_user_info(name):
    # Returns  user's name.
    return name


@access_control
def check_perms(name):
    # Function checks permission for user.
    return 'Allowed access'


print(get_user_info('Oleksiy')) #  Prints `Oleksiy`
print(get_user_info('Yuriy')) #  Prints `Permission denied.`

print(check_perms('Oleksiy')) #  Prints `Allowed access`
print(check_perms('Yuriy')) #  Prints `Permission denied.`

