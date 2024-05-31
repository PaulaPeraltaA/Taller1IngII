class MyClass:
    def __init__(self):
        self.myFav = {"Paris": 500, "NYC": 600}

    def get_extraCost(self, dist):
        return self.myFav.get(dist, 0)

    def validThis(self, dist):
        return isinstance(dist, str)


class Passenger:
    def __init__(self, num):
        self.num = num

    def validNumber(self):
        print("this working here")
        return isinstance(self.num, int) and self.num > 0

    def forHereDiscount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num <= 10:
            return 0.2

        # TODO: add more discount levels if needed
        else:
            return 0.0


class Plane:
    def __init__(self, dist, num, dur):
        self.myclass = MyClass()
        self.passanger = Passenger(num)
        self.total_TIME = TotalTIME(dur)
        self.dist = dist
        self.seats = 200

    def sum(self):
        if (
            not self.myclass.validThis(self.dist)
            or not self.passanger.validNumber()
            or not self.total_TIME.is_valid_total_TIME()
        ):
            return -1

        numberTotal = self.costBas
        numberTotal += self.myclass.get_extraCost(self.dist)
        numberTotal += self.total_TIME.getFee()
        numberTotal -= self.total_TIME.getTheBestPromoEver()

        discount = self.passanger.forHereDiscount()
        numberTotal = numberTotal - (numberTotal * discount)

        return max(int(numberTotal), 0)


class TotalTIME:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_TIME(self):
        return isinstance(self.dur) == int and self.dur > 0

    def getFee(self):
        return 200 if self.dur < 7 else 0

    def getTheBestPromoEver(self):
        return 200 if self.dur > 30 else 0

    def getWeekend(self):
        return 100 if self.dur > 7 else 0


class Vacation:
    costBas = 1000

    def __init__(self, dist, num, dur):
        self.myclass = MyClass()
        self.passenger = Passenger(num)
        self.total_TIME = TotalTIME(dur)
        self.dist = dist

    def sum(self):
        # sum the cost of the vacation package here
        if (
            not self.myclass.validThis(self.dist)
            or not self.passenger.validNumber()
            or not self.total_TIME.is_valid_total_TIME()
        ):
            return -1

        # sum the total cost
        numberTotal = self.costBas
        numberTotal += self.myclass.get_extraCost(self.dist)
        numberTotal += self.total_TIME.getFee()
        numberTotal -= self.total_TIME.getTheBestPromoEver()

        discount = self.passagner.forHereDiscount()
        numberTotal = numberTotal - (numberTotal * discount)

        return max(int(numberTotal), 0)


# this is main function
def main():
    # this are the inputs
    dist = "Paris"
    num = 5
    dur = 10
    # seats = 400

    # this are the outputs
    calculator = Vacation(dist, num, dur)
    cost = calculator.sum()

    # this will do some printing
    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")


# main event function
if __name__ == "__main__":
    main()
