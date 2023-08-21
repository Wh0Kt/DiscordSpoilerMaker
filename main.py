from pyperclip import copy

from kivy.clock import Clock

from kivy.core.image import Image

from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.config import Config

Config.set('graphics', 'full-screen', '0')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '600')  # (x coordinate)
Config.set('graphics', 'height', '200')  # (y coordinate)
Config.write()

n = ''


def btn_press(instance):  # code when button pressed
    print('pressed')

    def copied(dt):  # text change
        global n
        str(ti.text)

        for i in ti.text:
            n = n + f'||{i}||'

        instance.text = 'Copied!'
        copy(n)

    def notCopied(dt):  # undo text change
        instance.text = 'Copy'

    Clock.schedule_once(copied, 0)
    Clock.schedule_once(notCopied, 0.4)


class DiscordSpoilerMaker(App):
    def build(self):
        global ti
        global bt
        global w
        fl = FloatLayout()
        btn = FloatLayout()
        w = Image(source='Bg.png')
        btn.add_widget(w)

        ti = TextInput(  # text configuration
            pos=(10, 100),  # pos
            hint_text='Input your text',  # gray text
            size_hint_y=.18,  # size
            size_hint_x=.965,  # size
            font_name="RFont.ttf",  # font change
            font_size=19,
            padding=9,  # padding
            multiline=False,
            background_normal='TIBg.png',  # TextInput Bg
            background_active='TIBg.png',  # TextInput Bg
            border=(10, 10, 10, 10)
        )

        btn.add_widget(fl)
        fl.add_widget(ti)
        btn.add_widget(Button(  # button configuration
            text='Copy',  # button text
            on_release=btn_press,  # when pressed execute code
            size_hint=(.13, .19),  # button size
            pos=(505, 15),  # button position
            font_size=20,  # text size
            font_name="RFont.ttf",  # font change
            color=(255, 0, 0),  # text color
            background_normal='TIBg.png',
            background_down='TIBg.png'
        ))
        return btn


if __name__ == '__main__':
    DiscordSpoilerMaker().run()
