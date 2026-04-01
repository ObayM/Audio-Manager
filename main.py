import os
from textual.app import App
from textual.widgets import Header, Footer, Input, RichLog

class AudioManager(App):
    def __init__(self):

        super().__init__()
        self.current_dir = os.path.abspath(os.getcwd())

        self.audio_exts = ('.mp3', '.wav')

    def compose(self):
        yield Header(show_clock=True)
        yield RichLog(id="main-log", markup=True, highlight=True)
        yield Input(placeholder="> Enter a command (type 'help' to get started)", id='cmd-input')
        yield Footer()

    def on_mount(self):
        self.log_view = self.query_one(RichLog)
        self.show_welcome()

    def show_welcome(self):
        banner = "Hi, welcome to audio manager, here you can manage all of your audio files :)"

        self.log_view.write(banner)

if __name__ == "__main__":
    AudioManager().run()