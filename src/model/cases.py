class Cases:
    def __init__(self):
        self.all_cases = 0
        self.deaths = 0
        self.recovered = 0

    def __str__(self):
        return "{all_cases: " + str(self.all_cases) + ", deaths: " \
        + str(self.deaths) + ", recovered: " + str(self.recovered) + "}"