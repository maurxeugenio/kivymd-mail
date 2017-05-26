from kivy.app import App
from kivymd.theming import ThemeManager
from .sender import mail

class SendMailApp(App):
    theme_cls = ThemeManager()

    # chama a função que envia os emails
    def send_mail(*args):
        mail(args)

    def build(self):
        self.theme_cls.theme_style = 'Light'
