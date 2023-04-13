from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# Main Layout
class SeparateScreenAndButtons(GridLayout):
    def __init__(self, **kwargs):
        super(SeparateScreenAndButtons,self).__init__(**kwargs)
        self.rows = 4
        self.cols = 1
        self.add_widget(ScreenLayout())
        self.add_widget(ButtonLayout())
        self.add_widget(ButtonLayoutRow2())
        self.add_widget(ButtonLayoutRow3())

class ScreenLayout(GridLayout):
    def __init__(self, **kwargs):
        super(ScreenLayout,self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        # Textbox with Expression
        
        # Textbox with Answer

class ButtonLayout(GridLayout):
    def __init__(self, **kwargs):
        super(ButtonLayout,self).__init__(**kwargs)
        self.cols = 4
        self.rows = 5
        self.col_default_width = 75
        self.col_force_default = True
        self.row_default_height = 75
        self.row_force_default = True
        # 7, 8, 9, /
        button7 = Button(text='7')
        button8 = Button(text='8')
        button9 = Button(text='9')
        buttonDivide = Button(text='/')
        # 4 ,5, 6, *
        button4 = Button(text='4')
        button5 = Button(text='5')
        button6 = Button(text='6')
        buttonMulti = Button(text='X')
        # 1, 2, 3, -
        button1 = Button(text='1')
        button2 = Button(text='2')
        button3 = Button(text='3')
        buttonMinus = Button(text='-')

        self.add_widget(button7)
        self.add_widget(button8)
        self.add_widget(button9)
        self.add_widget(buttonDivide)
        self.add_widget(button4)
        self.add_widget(button5)
        self.add_widget(button6)
        self.add_widget(buttonMulti)
        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(button3)
        self.add_widget(buttonMinus)

class ButtonLayoutRow2(BoxLayout):
    def __init__(self, **kwargs):
        super(ButtonLayoutRow2,self).__init__(**kwargs)

        button0 = Button(text='0',size_hint=(None,None),size=(75,75))
        buttonPlus = Button(text='+',size_hint=(None,None),size=(75,75))
        buttonEquals = Button(text='=',size_hint=(None,None),size=(150,75))

        self.add_widget(button0)
        self.add_widget(buttonEquals)
        self.add_widget(buttonPlus)

class ButtonLayoutRow3(BoxLayout):
    def __init__(self, **kwargs):
        super(ButtonLayoutRow3,self).__init__(**kwargs) 

        buttonBackspace = Button(text='C',size_hint=(None,None),size=(150,75))  
        buttonAllClear = Button(text='AC',size_hint=(None,None),size=(150,75))

        self.add_widget(buttonBackspace)
        self.add_widget(buttonAllClear)
        



class MyApp(App):
    def build(self):
        return SeparateScreenAndButtons()


if __name__ == '__main__':
    MyApp().run()