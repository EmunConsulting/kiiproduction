from django.contrib import messages
from functools import wraps
from django.shortcuts import redirect, render


def create_record(model, form_class, template_name, redirect_url, redirect_id=None, post_save_callback=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.method == "POST":
                form = form_class(request.POST)
                if form.is_valid():
                    record = form.save()
                    messages.success(request, 'Record created.')

                    if post_save_callback:
                        post_save_callback(record)

                    if redirect_id and 'redirect_id' in kwargs:
                        return redirect(redirect_url, pk=kwargs['redirect_id'])
                    return redirect(redirect_url)
            else:
                form = form_class()
            return render(request, template_name, {'form': form})
        return _wrapped_view
    return decorator


def update_record(model, form_class, template_name, redirect_url, redirect_id=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, pk, *args, **kwargs):
            instance = model.objects.get(pk=pk)
            if request.method == "POST":
                form = form_class(request.POST, instance=instance)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Record updated.')
                    if redirect_id and 'redirect_id' in kwargs:
                        return redirect(redirect_url, pk=kwargs['redirect_id'])
                    return redirect(redirect_url)
            else:
                form = form_class(instance=instance)
            return render(request, template_name, {'form': form, 'instance': instance})
        return _wrapped_view
    return decorator


def delete_record(model, redirect_url, redirect_id=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, pk, *args, **kwargs):
            instance = model.objects.get(pk=pk)
            instance.delete()
            messages.success(request, 'Record deleted.')
            if redirect_id and 'redirect_id' in kwargs:
                return redirect(redirect_url, pk=kwargs['redirect_id'])
            return redirect(redirect_url)
        return _wrapped_view
    return decorator

