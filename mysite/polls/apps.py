from django.apps import AppConfig


class PollsConfig(AppConfig):
  name = 'polls'
  verbose_name = 'Polls'

  def ready(self):
    from  polls.signals.handlers import my_custom_handler
    from  polls.signals.senders import custom_signal
    # custom_signal.connect(my_custom_handler)