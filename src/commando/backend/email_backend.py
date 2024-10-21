import ssl
from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.local_hostname = kwargs.get('local_hostname', None)
        self.debug_level = kwargs.get('debug_level', 0)

    def _get_ssl_context(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context

    def open(self):
        if self.connection:
            return False
        connection_class = self.connection_class
        if self.use_ssl:
            self.connection = connection_class(
                self.host, self.port, context=self._get_ssl_context()
            )
        else:
            self.connection = connection_class(self.host, self.port)
            if self.use_tls:
                self.connection.starttls(context=self._get_ssl_context())
        self.connection.set_debuglevel(self.debug_level)
        self.connection.login(self.username, self.password)
        return True
