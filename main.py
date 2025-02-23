from kivy.app import App  
from kivy.uix.boxlayout import BoxLayout  
from kivy.uix.textinput import TextInput  
from kivy.uix.button import Button  
import subprocess  

class DownloaderGUI(BoxLayout):  
    def __init__(self, **kwargs):  
        super().__init__(orientation='vertical', **kwargs)  

        self.url_input = TextInput(hint_text="Enter URL", size_hint=(1, 0.2))  
        self.add_widget(self.url_input)  

        self.download_button = Button(text="Download", size_hint=(1, 0.2))  
        self.download_button.bind(on_press=self.start_download)  
        self.add_widget(self.download_button)  

    def start_download(self, instance):  
        url = self.url_input.text.strip()  
        if not url:  
            return  
        command = f"python main.py --url {url}"  
        subprocess.Popen(command, shell=True)  

class DownloaderApp(App):  
    def build(self):  
        return DownloaderGUI()  

if __name__ == "__main__":  
    DownloaderApp().run()
