#!/usr/bin/env python3
#-*-coding:utf-8-*-

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


#Загружаю разметку
Builder.load_string('''
<MainScreen>:
    orientation:'vertical'
    BoxLayout:
        canvas:
            Color:
                rgba:(0.5,0.5,0.5,1)
            Rectangle:
                pos:self.pos
                size:self.size
        ScrollView:
            size_hint_y:None
            size_hint:(1,1)
            BoxLayout:
                id:another_box
                size_hint_y:None
                height:self.minimum_height
                orientation:'vertical'
                spacing:5
    BoxLayout:
        canvas:
            Color:
                rgba:(1,1,1,1)
            Rectangle:
                pos:self.pos
                size:self.size
        size_hint:(1,0.1)
        padding:5
        spacing:3
        Button:
            text:'create'
        Button:
            text:'recreate'
        Button:
            text:'update'
        Button:
            text:'clear'
        Button:
            text:'new screen'
            on_release: root.add_new_screen()


<MyNewScreen>:
    orientation:'vertical'
    size_hint:(1,0.1)
    padding:5
    spacing:3
    Button:
        text:'update'
    Button:
        text:'clear'
    Button:
        text:'new screen'

''')


class MyNewScreen(BoxLayout):
    #Это мой новый экран
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class MainScreen(BoxLayout):
    #Главный экран, на котором все будет происходить

    def add_new_screen(self):
        #удаляет все виджеты принадлежащие классу MainScreen и создает сделанный мной виджет MyNewScreen
        self.clear_widgets()
        self.add_widget(MyNewScreen())


class TestApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    TestApp().run()