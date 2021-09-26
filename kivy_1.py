from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView #прокрутка экрана

class ScrButton(Button):
    def __init__(self, screen, direction = 'right', goal = 'main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction #текущий экран и сохраняет его в current
        self.screen.manager.current = self.goal #переходит в нужный экран, который хр. в goal
    
class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        h = BoxLayout()
        v = BoxLayout(orientation = 'vertical', spacing = 8, padding = 8)
        txt = Label(text = 'Выбери экран')
        v.add_widget(ScrButton(self, direction='down', goal = 'first', text = '1'))
        v.add_widget(ScrButton(self, direction='left', goal = 'second', text = '2'))
        v.add_widget(ScrButton(self, direction='up', goal = 'third', text = '3'))
        v.add_widget(ScrButton(self, direction='right', goal = 'fourth', text = '4'))
        h.add_widget(txt)
        h.add_widget(v)
        self.add_widget(h)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name = 'main'))
        return sm

MyApp().run()



