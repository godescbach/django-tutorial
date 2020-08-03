import django.dispatch


custom_signal = django.dispatch.Signal(providing_args=['arg1_', 'arg2_'])
