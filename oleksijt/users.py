""" This module contents functions and classes, that serve Users:

`access_control` - decorator function which controls user access
    to functions;

`User` - base class for users;
    `set_role` - sets roles for access handling.
    `get_name` - returns user's name. This function
         decorated by access_control function;
    `get_username` - returns user's login. This function
         decorated by access_control function;
    `get_user_info` - returns user object's parameters. This function
         decorated by access_control function;
    `check_perms` - checks permission for given user. This function
         decorated by access_control function.
"""


def access_control(func):
    # Decorator function to control user access to functions
    def wrapper(*args, **kwargs):
        try:
            if args[0].role == 'admin':
                return func(*args, **kwargs)
            else:
                raise PermissionError
        except PermissionError:
            print('Access denied. You can not perform this operation.')
    return wrapper


class User:
    """Base class for users."""
    def __init__(self, name, username, role='guest'):
        self.name = name
        self.username = username
        self.role = role

    def set_role(self, role):
        # Sets roles for access handling.
        self.role = role

    @access_control
    def get_name(self):
        # Returns user's name.
        return self.name

    @access_control
    def get_username(self):
        # Returns user 's login.
        return self.username

    @access_control
    def get_user_info(self):
        # Returns  user object's parameters.
        user_info = vars(self)
        return user_info

    @access_control
    def check_perms(self, user):
        # Function checks permission for given user.
        permission = 'Denied access'
        if user.role == 'admin':
            permission = 'Allowed access'
        return permission


if __name__ == '__main__':

    print(__doc__)
    print(User.__doc__)

    # Create user oleksiy.
    oleksiy = User('Oleksiy', 'oleksijt')
    print(oleksiy, vars(oleksiy))

    print(oleksiy.get_name())  # Raises PermissionError.
    print(oleksiy.get_username())  # Raises PermissionError.
    print(oleksiy.get_user_info())  # Raises PermissionError.

    # Create user yuriy.
    yuriy = User('Yuriy', 'yurchykt')
    print(yuriy, vars(yuriy))

    print(yuriy.get_name())  # Raises PermissionError.
    print(yuriy.get_username())  # Raises PermissionError.
    print(yuriy.get_user_info())  # Raises PermissionError.

    # Set oleksiy as admin.
    oleksiy.set_role('admin')
    print(oleksiy, vars(oleksiy))
    print(oleksiy.get_name())  # Doesn't raise PermissionError.
    print(oleksiy.get_username())  # Doesn't raise PermissionError.
    print(oleksiy.get_user_info())  # Doesn't raise PermissionError.

    # Check permission
    print(oleksiy.check_perms(oleksiy))  # Returns `Allowed access`
    print(oleksiy.check_perms(yuriy))  # Returns `Denied access`
    print(yuriy.check_perms(oleksiy))  # Raises PermissionError.
