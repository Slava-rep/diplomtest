# utils/decorators.py
from django.core.exceptions import PermissionDenied

# def measurement_type_required(*measurement_types):
#     def decorator(view_func):
#         def wrapper(request, *args, **kwargs):
#             user = request.user
#             if not user.employee.measurement_types.filter(name__in=measurement_types).exists():
#                 raise PermissionDenied
#             return view_func(request, *args, **kwargs)
#         return wrapper
#     return decorator


# diplomtest/utils/decorators.py
from django.core.exceptions import PermissionDenied
from functools import wraps

def measurement_type_required(measurement_type_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied
            if not hasattr(request.user, 'employee'):
                raise PermissionDenied
            if not request.user.employee.measurement_types.filter(name=measurement_type_name).exists():
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator