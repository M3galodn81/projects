from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class SeparateScreenAndButtons(GridLayout):
    def __init__(self, **kwargs):
        super(SeparateScreenAndButtons,self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1

class ScreenLayout(GridLayout):
    def __init__(self, **kwargs):
        super(ScreenLayout,self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2

class ButtonLayout(GridLayout):
    def __init__(self, **kwargs):
        super(ButtonLayout,self).__init__(**kwargs)
        self.cols = 4
        self.cols = 5
        

class MyApp(App):
    def build(self):
        return SeparateScreenAndButtons


if __name__ == '__main__':
    MyApp().run()