import appdaemon.appapi as appapi

class YellowAlert(appapi.AppDaemon):

    def initialize(self):
        self.handle = self.listen_state(self.set_lights, "light.desk_lamp")


    def set_lights(self, **kwargs):
        self.turn_on("light.tall_office_lamp")
        self.turn_on("light.top_track_bulb", color_name="blue")
        self.say_it_loud()

    def say_it_loud(self):
        self.call_service("tts/google_say",
            message="Yellow Alert, prepare for testing!",
            entity_id="media_player.office_speaker")
