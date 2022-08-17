class Forecast_Class:
    def __init__(self, time, temp, chance) -> None:
        self.time = time
        self.temp = temp
        self.chance = chance

    def info(self):
        return {
            "time": self.time,
            "temp": self.temp,
            "chance": self.chance
        }