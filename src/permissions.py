from functools import wraps


class Checks:
    def enforce_logged_in(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.logged_in:
                raise PermissionError("User is not logged in")
            return func(self, *args, **kwargs)
        return wrapper
