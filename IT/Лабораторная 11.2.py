class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        return f'Время: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'
    def __repr__(self):
        return f'hours: {self.hours} minutes: {self.minutes} seconds: {self.seconds}'
    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    def __eq__(self, other):
        return self.total_seconds() == other.total_seconds()
    def __ne__(self, other):
        return self.total_seconds() != other.total_seconds()
    def __lt__(self, other):
        return self.total_seconds() < other.total_seconds()
    def __gt__(self, other):
        return self.total_seconds() > other.total_seconds()
    def __le__(self, other):
        return self.total_seconds() <= other.total_seconds()
    def __ge__(self, other):
        return self.total_seconds() >= other.total_seconds()
    def __add__(self, other):
        addition = self.total_seconds() + other.total_seconds()
        hours = addition // 3600
        minutes = (addition % 3600) // 60
        seconds = addition % 60
        return Time(hours, minutes, seconds)
    def __sub__(self, other):
        addition = self.total_seconds() - other.total_seconds()
        if addition < 0:
            addition = other.total_seconds() - self.total_seconds()
        hours = addition // 3600
        minutes = (addition % 3600) // 60
        seconds = addition % 60
        return Time(hours, minutes, seconds)
    def __mul__(self, other):
        addition = self.total_seconds() * other.total_seconds()
        hours = addition // 3600
        minutes = (addition % 3600) // 60
        seconds = addition % 60
        return Time(hours, minutes, seconds)
    def __floordiv__(self, other):
        addition = self.total_seconds() // other.total_seconds()
        hours = addition // 3600
        minutes = (addition % 3600) // 60
        seconds = addition % 60
        return Time(hours, minutes, seconds)
clock_1 = Time(1,23,30)
clock_2 = Time(1,23,13)
clock_3 = Time(23,40,12)

print(clock_1)
print(clock_2)
print(clock_3)
print('-'*100)
print( clock_2,'==', clock_3, clock_2 == clock_3)
print( clock_2,'!=', clock_3, clock_2 != clock_3)
print( clock_2,'>', clock_3, clock_2 > clock_3)
print( clock_2,'<', clock_3, clock_2 < clock_3)
print(clock_2 + clock_3)
print(clock_2 - clock_3)
print(clock_2 * clock_3)
print(clock_3 // clock_2)


