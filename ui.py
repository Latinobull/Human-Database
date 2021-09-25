from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Opening(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    #     b1 = Button(text='A')
    pass


class MainWidget(Widget):
    pass


class HumanGameApp(App):
    intro = 'Welcome to the Simulation'

    def build(self):
        return Opening()


if __name__ == '__main__':
    HumanGameApp().run()
