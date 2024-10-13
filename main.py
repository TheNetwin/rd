from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.project_screen import ProjectScreen
from screens.edit_project_screen import EditProjectScreen

class PhotoStopApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ProjectScreen(name='project_screen'))
        sm.add_widget(EditProjectScreen(name='edit_project_screen'))
        return sm

if __name__ == '__main__':
    PhotoStopApp().run()
