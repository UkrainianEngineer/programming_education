"""
This module contents functions that serve Users:

`get_name` - returns user's name;
`get_username` - returns user's login;
`get_user_info` - returns user object's parameters;
`get_user_info` - returns user object's parameters. This function
 decorated by perm_control function;

`get_user_info` - returns user object's parameters;
`get_user_info` - returns user object's parameters;
`get_user_info` - returns user object's parameters;



15. This task contains a few parts:
Write a custom function which returns your name or username.
Write a decorator which allows access for your user and prints “Permission denied” for other users.

Tips:
Create `get_user_info` function which returns your name or username.
Create decorator which raises Exception if `get_user_info` returns not your name or username
Create `check_perms` function decorated by decorator. This function returns `Allowed access` if user validation is successful.


"""


def access_control(func):
    def wrapper(*args, **kwargs):
        # print('get:{}'.format(*args, **kwargs))
        # print(args[0])

        if args[0].role == 'admin':
            func(*args, **kwargs)
        else:
            raise PermissionError
    return wrapper


class User:

    def __init__(self, name, username, role='guest'):
        self.name = name
        self.username = username
        self.role = role

    def set_role(self, role):
        self.role = role

    @access_control
    def get_name(self):
        return self.name

    @access_control
    def get_username(self):
        return self.username

    @access_control
    def get_user_info(self):
        user_info = self.__dict__
        print('infunc', user_info)
        return user_info

    def check_perms(self):
        permission = 'Denied access'
        if self.role == 'admin':
            permission = 'Allowed access'
        return permission


if __name__ == '__main__':

    # Create user oleksiy.
    oleksiy = User('Oleksiy', 'oleksijt')
    print(oleksiy, oleksiy.__dict__)

    # print(oleksiy.get_name()) # Raises PermissionError.
    # print(oleksiy.get_username()) # Raises PermissionError.
    # print(oleksiy.get_user_info()) # Raises PermissionError.

    # Create user yuriy.
    yuriy = User('Yuriy', 'Yurchykt')
    print(yuriy, yuriy.__dict__)

    # print(yuriy.get_name()) # Raises PermissionError.
    # print(yuriy.get_username()) # Raises PermissionError.
    # print(yuriy.get_user_info()) # Raises PermissionError.

    # Set oleksiy as admin.
    oleksiy.set_role('admin')
    print(oleksiy, oleksiy.__dict__)
    print(oleksiy.get_name())
    print(oleksiy.get_username())
    print(oleksiy.get_user_info()) # Raises PermissionError.



    print(oleksiy.get_user_info())

    # Check permission
    print(oleksiy.check_perms())
    print(yuriy.check_perms())
