import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import Functions as fun
import DataBase as db

class Introduction(Screen):
    pass


class InputWin(Screen):
    distance = 0

    def press(self):
        try:
            long_1 = float(self.ids.long_1.text)
            lat_1 = float(self.ids.lat_1.text)
            long_2 = float(self.ids.long_2.text)
            lat_2 = float(self.ids.lat_2.text)
            a = fun.havfor(lat_1, long_1, lat_2, long_2)
            d = fun.havinv(a) * 6378.1
            self.ids.lat_1.text = ''
            self.ids.long_1.text = ''
            self.ids.lat_2.text = ''
            self.ids.long_2.text = ''
            self.ids.dist.text = str(d)

            if 0 < d <= 52.074:
                self.ids.condition.text = 'Choice'
            elif 52.074 < d <= 8000:
                self.ids.condition.text = 'MissileOut'
            else:
                self.ids.condition.text = 'Error'


        except:
            self.ids.lat_1.text = ''
            self.ids.long_1.text = ''
            self.ids.lat_2.text = ''
            self.ids.long_2.text = ''
            self.ids.condition.text = 'Error'


class Choice(Screen):
    pass


class MissileOut(Screen):
    def display(self):
        dist = float(self.manager.screens[1].ids.dist.text)
        direc = fun.missile_filter(db.missile_directory, dist)
        missile = fun.missile_out(direc, dist)
        self.ids.missileout.text = missile


class ArtilleryOut(Screen):
    def display_a(self):
        dist = float(self.manager.screens[1].ids.dist.text)
        direc = fun.artillery_filter(db.artillery_directory, dist)
        artillery = fun.artillery_out(direc, dist)
        self.ids.artilleryout.text = artillery


class Error(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('Frontend.kv')



class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()
