from kivy.uix.screenmanager import Screen

class EditProjectScreen(Screen):
    def add_audio(self, filepath):
        print(f"Adding audio: {filepath}")

    def apply_effect(self, effect_name):
        print(f"Applying effect: {effect_name}")
