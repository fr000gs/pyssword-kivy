from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.properties import VariableListProperty
from kivy.uix.checkbox import CheckBox
from hashlib import sha512

class main_screen(GridLayout):
    pswd = StringProperty(defaultvalue=18*'*')
    passwd = ''
    cols = 3
    master_passwd = StringProperty('foo')
    def show(self, show, active):
        print(show.text, active)
        show.password =  not active
    def complete(self):
        enc = sha512()
        enc.update(bytes(self.ids.m_pswd.text + self.ids.username.text + self.ids.site.text, 'utf-8'))
        self.passwd = str(enc.hexdigest()[::8] +'@A')
        self.pswd = self.passwd if self.ids.m_pswd_check.active else 18*'*'


class pysswordApp(App):
    def build(self):
        return main_screen()

if __name__ == '__main__':
    pysswordApp().run()

