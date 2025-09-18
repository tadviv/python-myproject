import random
import string
import base64
import webbrowser

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup


def get_random_str(length=3):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def process_message(message, coding):
    try:
        if not coding:
            message = base64.b64decode(message).decode('utf-8')
    except Exception:
        return "❌ Invalid encoded message!"

    words = message.split(" ")
    nwords = []
    if coding:
        for word in words:
            if len(word) >= 3:
                r1 = get_random_str()
                r2 = get_random_str()
                stnew = r1 + word[1:] + word[0] + r2
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
    else:
        for word in words:
            if len(word) >= 3:
                stnew = word[3:-3]
                stnew = stnew[-1] + stnew[:-1]
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])

    result = "  ".join(nwords)
    if coding:
        result = base64.b64encode(result.encode('utf-8')).decode('utf-8')
    return result


class EncoderApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.label = Label(text="Enter your message:", font_size=20, size_hint=(1, 0.1))
        self.add_widget(self.label)

        self.text_input = TextInput(multiline=True, font_size=18, size_hint=(1, 0.4))
        self.add_widget(self.text_input)

        self.encode_button = ToggleButton(text="Encode", group="mode", state='down', size_hint=(0.5, 0.1))
        self.decode_button = ToggleButton(text="Decode", group="mode", size_hint=(0.5, 0.1))

        toggle_layout = BoxLayout(size_hint=(1, 0.1))
        toggle_layout.add_widget(self.encode_button)
        toggle_layout.add_widget(self.decode_button)
        self.add_widget(toggle_layout)

        self.process_button = Button(text="Process", size_hint=(1, 0.1), background_color=(0.2, 0.6, 1, 1))
        self.process_button.bind(on_press=self.process_text)
        self.add_widget(self.process_button)

        self.result = TextInput(text="", multiline=True, readonly=True, font_size=18, size_hint=(1, 0.4))
        self.add_widget(self.result)

        self.whatsapp_button = Button(text="Send to WhatsApp", size_hint=(1, 0.1), background_color=(0, 0.8, 0, 1))
        self.whatsapp_button.bind(on_press=self.send_to_whatsapp)
        self.add_widget(self.whatsapp_button)

    def process_text(self, instance):
        text = self.text_input.text.strip()
        coding = self.encode_button.state == 'down'
        if not text:
            self.show_popup("Error", "Please enter a message.")
            return
        result = process_message(text, coding)
        self.result.text = result

    def send_to_whatsapp(self, instance):
        message = self.result.text.strip()
        if not message:
            self.show_popup("Error", "No message to send.")
            return
        url = f"https://wa.me/?text={message}"
        webbrowser.open(url)

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text="Close", size_hint=(1, 0.25))
        popup_layout.add_widget(close_button)
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()


class EncoderAppMain(App):
    def build(self):
        return EncoderApp()


if __name__ == "__main__":
    EncoderAppMain().run()
