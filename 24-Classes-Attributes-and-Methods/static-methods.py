class WeatherForecast():
    def __init__(self, temp):
        self._temp = temp

    @staticmethod
    def convert_to_celsius(temp):
        return (temp - 32) * 5 / 9

    def in_celcius(self):
        return [round(self.convert_to_celsius(temp),2) for temp in self._temp]

wf = WeatherForecast([100,90,60])
print(wf.in_celcius())