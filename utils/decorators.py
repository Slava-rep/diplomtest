# utils/decorators.py
from django.core.exceptions import PermissionDenied

def measurement_type_required(*measurement_types):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.employee.measurement_types.filter(name__in=measurement_types).exists():
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator