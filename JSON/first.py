import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.button import Button



class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3
        self.size_hint = (0.2, 0.2)
        self.pos_hint = {"center_x":0.5, "center_y":0.5}

        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False, padding_y = (20, 20), size_hint = (1, 0.3))
        self.add_widget(self.username)
        
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False, padding_y = (10, 10), size_hint = (1, 1))
        self.add_widget(self.password)


        self.button = Button(text="Submit")
        self.button.bind(on_press = self.handle(self.password))
        self.add_widget(self.button)

        def handle(self, password):
            LoginScreen.add_widget(Label(text="Your password was" + password))

        self.dropdown = DropDown()
        options = ["add", "create", "view"]
        for index in range(len(options)):
            self.btn = Button(text = options[index], size_hint_y = None, height = 20)
            self.btn.bind(on_release = lambda btn: self.dropdown.select(self.btn.text)) #lambda btn:
            self.dropdown.add_widget(self.btn)

        self.mainbutton = Button(text = 'options', size_hint =(None, None), pos =(350, 300))
        self.mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))
        print(self.x)

        #runTouchApp(self.mainbutton)

class MyApp(App):
    def build(self):

        self.window = GridLayout()
        self.window.cols = 2
        self.window.rows = 3
        self.window.size_hint = (0.2, 0.2)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}

        self.window.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False, padding_y = (10, 10), size_hint = (1, 0.3))
        self.window.add_widget(self.username)
        
        self.window.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False, padding_y = (10, 10), size_hint = (1, 1))
        self.window.add_widget(self.password)


        self.button = Button(text="Submit")
        self.button.bind(on_press = self.handle)
        self.window.add_widget(self.button)

        self.dropdown = DropDown()
        options = ["add", "create", "view"]
        for index in range(len(options)):
            self.btn = Button(text = options[index], size_hint_y = None, height = 20)
            print(self.btn.text)
            self.btn.bind(on_release = self.show_menu) #lambda btn:
            self.dropdown.add_widget(self.btn)

        self.mainbutton = Button(text = 'options', size_hint =(None, None), pos =(350, 300))
        self.mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, options: setattr(self.mainbutton, 'text', options[index]))
        print(self.dropdown.x)

        runTouchApp(self.mainbutton)
        
        return self.window
    
    def handle(self, instance):
            self.window.add_widget(Label(text="Your password was " + self.password.text))
    
    def show_menu(self, instance):
        self.dropdown.select(self.btn.text)



if __name__ == '__main__':
    MyApp().run()