from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager


class Entry_Chart (Screen):
    def __init__(self, **kw):
        super(Entry_Chart,self).__init__(**kw)



class Manager (ScreenManager):
    def __init__(self, **kwargs):
        super(Manager,self).__init__(**kwargs)

        self.add_widget(Entry_Chart(name="entrychart"))



class Engine(App):
    def build(self):
        return Manager ()



if __name__ == "__main__":
    Engine().run()