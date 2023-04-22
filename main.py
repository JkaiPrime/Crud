from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Tela1(Screen):
    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        grid = GridLayout(cols=2, rows=2)
        layout.add_widget(grid)

        grid.add_widget(Label(text='Número 1'))
        self.number1 = TextInput(multiline=False)
        grid.add_widget(self.number1)
        grid.add_widget(Label(text='Número 2'))
        self.number2 = TextInput(multiline=False)
        grid.add_widget(self.number2)

        layout.add_widget(Button(text='Próxima', on_press=self.on_next_screen, size_hint=(1, 0.2)))

    def on_next_screen(self, instance):
        self.manager.current = 'tela2'


class Tela2(Screen):
    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        layout.add_widget(Label(text='Tela 2'))
        layout.add_widget(Button(text='Voltar', on_press=self.on_previous_screen, size_hint=(1, 0.2)))

    def on_previous_screen(self, instance):
        self.manager.current = 'tela1'


class MeuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Tela1(name='tela1'))
        sm.add_widget(Tela2(name='tela2'))
        return sm


if __name__ == '__main__':
    MeuApp().run()
