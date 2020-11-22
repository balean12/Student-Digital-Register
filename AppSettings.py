import javaproperties
class AppSettings():
    def __init__(self):
        self._filename = "settings.properties"
        f = open(self._filename, 'r')
        self._datalist = javaproperties.load(f)

    @property
    def Data(self):
        return self._datalist


