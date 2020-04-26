from kivy.app import App
from kivy.loader import Loader
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.clock import Clock
from kivy.properties import *
from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button

Builder.load_string('''
<MyWidget>:
    carousel: carousel
    cols: 1
    Button:
        pos_hint: {"center_x":0.5, "center_y":0.1}
        size_hint: .3,.1
        font_size: 35
        text: str(root.on_off)
        on_release: root.start_slide()
    Carousel:
        pos_hint: {"center_x":0.5, "center_y":0.9}
        id: carousel
        direction: 'right'
        loop: True
        index: 0
''')

class MyWidget(GridLayout):
    on_off = StringProperty('Start')
    slide_count = NumericProperty(11)
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__()
        self.carousel = Carousel(direction='right')
        self.add_widget(self.carousel)
        for i in range(self.slide_count):
            src = "%d&.jpg" % i
            image = AsyncImage(source=src, allow_stretch=True)
            self.carousel.add_widget(image)
        #self.start_slide()### Uncomment this to start slideshow when the app starts

    def start_slide(self, *args):
        if self.on_off == 'Start':
            self.on_off = 'Stop'
            self.clock = Clock.schedule_interval(self.slide_next, 3) ##move right every 3 seconds
            return
        if self.on_off == 'Stop':
            self.on_off = 'Start'
            Clock.unschedule(self.clock)
            self.carousel.index = 0

    def slide_next(self, *args):
        if self.carousel.index == (self.slide_count - 1):
            self.carousel.index = 0### This keeps the loops intact
            #### if you want to end the slideshow at the last image, use 'Clock.unschedule(self.clock)' instead
            return
        self.carousel.load_next()

class SlideShowApp(App):

    def build(self):
        mywidget = MyWidget()
        return mywidget

if __name__ == '__main__':

    SlideShowApp().run()