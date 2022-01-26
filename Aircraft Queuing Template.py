class Aircraft():

    def __init__(self, id, weight, passengers):
        self.id = id
        self.weight = weight
        self.passengers = passengers


class Runway():

    def __init__(self, id, runway_type):
        self.runway_type = runway_type
        self.id = id
        self.aircraft_list = []

        if self.runway_type == "small":
            self.cap = 200000
        elif self.runway_type == "medium":
            self.cap = 500000
        elif self.runway_type == "large":
            self.cap = float('inf')

    def add(self, aircraft):
        self.aircraft_list.append(aircraft)


def sort_aircrafts(aircrafts, runways):
    # Implement sorting

    for aircraft in aircrafts:
        runways[0].add(aircraft)

    return runways


def print_output(runways):
    for runway in runways:
        print(f"Runway {runway.id}: {runway.runway_type}")
        for aircraft in runway.aircraft_list:
            print(f"\t Aircraft {aircraft.id}: {aircraft.weight} lbs, {aircraft.passengers} passenegers")


def main():
    aircrafts = [
        Aircraft(1, 400000, 212),
        Aircraft(2, 100000, 55),
        Aircraft(3, 100000, 25),
        Aircraft(4, 100000, 95),
        Aircraft(5, 100000, 115),
        Aircraft(6, 250000, 121),
        Aircraft(7, 600000, 15),
        Aircraft(8, 300000, 155),
        Aircraft(9, 600000, 225),
        Aircraft(10, 100000, 95),
        Aircraft(11, 100000, 116),
        Aircraft(12, 800000, 3),
        Aircraft(13, 5555, 3),
        Aircraft(14, 250000, 3),
        Aircraft(15, 100000, 116),
    ]

    runways = [Runway(1, "small"),
               Runway(2, "small"),
               Runway(3, "medium"),
               Runway(4, "medium"),
               Runway(5, "medium"),
               Runway(6, "large")]

    sorted_runways = sort_aircrafts(aircrafts, runways)
    print_output(sorted_runways)


if __name__ == "__main__":
    main()
