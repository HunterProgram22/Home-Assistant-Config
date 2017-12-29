import appdaemon.appapi as appapi

class YellowAlert(appapi.AppDaemon):

    def initialize(self):
        self.log("This is a Yellow Alert")
        self.log("All hands prepare for testing!")
        self.set_lights()
        self.say_it_loud()

    def set_lights(self):
        self.turn_on("light.tall_office_lamp")
        self.turn_on("light.top_track_bulb", color_name="blue")

    def say_it_loud(self):
        self.call_service("tts/google_say",
            message="Yellow Alert, prepare for testing!",
            entity_id="media_player.office_speaker")
