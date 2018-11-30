"""Script defines custom exceptions."""


class CustomError(Exception):
    pass


class PermissionDenied(CustomError):
    pass
