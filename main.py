import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter


class myApp(App):
    def build(self):
        fl = FloatLayout(size=(200, 200), pos_hint={'center_y': .5, 'center_x': .5})
        fl.add_widget(Button(
            text="button 1",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1, 1, 0, 1],
            background_normal='',
            size_hint=(.4, .10),
            pos_hint={'center_y': .5, 'center_x': .5}));

        fl.add_widget(Button(
            text='button 2',
            font_size=20,
            on_press=self.btn2_press,
            background_color=[1, 0, 0, 1],
            background_normal='',
            size_hint=(.4, .10),
            pos_hint={'center_y': .7, 'center_x': .5}));
        return fl

    def btn_press(self, instance):
        instance.text = 'Clicked btn 1'

    def btn2_press(self, instance):
        instance.text = "Вторая кнопка нажата"


if __name__ == "__main__":
    myApp().run()

