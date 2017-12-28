import appdaemon.appapi as appapi

class YellowAlert(appapi.AppDaemon):

    def initizalize(self):
        self.log("This is a Yellow Alert")
        self.log("All hands prepare for testing!")
        self.set_lights()

    def set_lights(self):
        self.turn_on("light.tall_office_lamp")
        self.turn_on("light.top_track_bulb")
