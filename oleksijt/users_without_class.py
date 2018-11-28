""" This module contents functions, that serve users:

`access_control` - decorator function which controls user access
    to functions;
`get_user_info` - returns user's name. This function
     decorated by access_control function;
`check_perms` - checks permission for user. This function
     decorated by access_control function.
"""

admins_list = ['pivanchy', 'oleksijt']
moderators_list = ['Yuriy', 'oleksijt']


# Decorator function which controls user access to functions
def allowed_users(user_list):
    def access_control(func):
        def wrapper(*args, **kwargs):
            if args[0] not in user_list:
                raise PermissionError('Permission denied.')
            return func(*args, **kwargs)
        return wrapper
    return access_control


@allowed_users(admins_list)
def get_user_info(name):
    # Returns  user's name.
    return name


@allowed_users(moderators_list)
def check_perms(name):
    # Function checks permission for user.
    return 'Allowed access'


if __name__ == '__main__':
    print(get_user_info('oleksijt'))  # Prints `Oleksiy`
    print(get_user_info('Yuriy'))  # Prints `Permission denied.`

    print(check_perms('pivanchy'))  # Prints `Allowed access`
    print(check_perms('Yuriy'))  # Prints `Permission denied.`
