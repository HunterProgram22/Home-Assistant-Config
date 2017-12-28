import appdaemon.appapi as appapi

class YellowAlert(appapi.AppDaemon):

    def initizalize(self):
        self.log("This is a Yellow Alert")
        self.log("All hands prepare for testing!")
