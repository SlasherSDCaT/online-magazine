#10
class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = "A"

    def pull(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "F"
            return 3
        if self.state == "D":
            self.state = "E"
            return 5
        if self.state == "E":
            self.state = "F"
            return 7
        if self.state == "F":
            self.state = "D"
            return 9
        if self.state == "G":
            self.state = "H"
            return 10
        if self.state == "H":
            self.state = "D"
            return 11
        raise MealyError("pull")

    def glare(self):
        if self.state == "A":
            self.state = "F"
            return 1
        if self.state == "B":
            self.state = "C"
            return 2
        if self.state == "C":
            self.state = "D"
            return 4
        if self.state == "D":
            self.state = "D"
            return 6
        if self.state == "F":
            self.state = "G"
            return 8
        raise MealyError("glare")


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.glare() == 1
    assert o.glare() == 8
    raises(lambda: o.glare(), MealyError)
    assert o.pull() == 10
    assert o.pull() == 11
    assert o.glare() == 6
    assert o.pull() == 5
    assert o.pull() == 7
    assert o.pull() == 9

    o = main()
    assert o.pull() == 0
    assert o.glare() == 2
    raises(lambda: o.pull(), MealyError)
    assert o.glare() == 4

    o = main()
    assert o.pull() == 0
    assert o.pull() == 3

#8
def main(s):
    s = s[6:-7]
    s = (s.replace('store', '')
         .replace('array', '')
         .replace('(', '')
         .replace(')', '')
         .replace('\n', ' '))
    s = s.split('.')
    for i in range(len(s)):
        s[i] = s[i].split(':=')
    s = s[:-1]
    ans = dict()
    for i in range(len(s)):
        ans[s[i][0].replace(' ', '')] = s[i][1].split()
    return ans

#7
def main(x):
    x = bin(x)[2:]
    if len(x) < 38:
        x = "0" * (38 - len(x)) + x
    j5 = x[0:3]
    j4 = x[3:13]
    j3 = x[13:23]
    j12 = x[23:]
    x = j5 + j3 + j4 + j12
    return str(int(x, 2))

#6
def main(d):
    d = list(str(i) for i in d)
    x = {
        "2007": {
            "NINJA": {"1967": 0, "2007": {"1962": 1, "1974": 2, "2001": 3}},
            "POD": {"1967": 4, "2007": {"NU": 5, "RAGEL": 6, "R": 7}},
        },
        "2006": {
            "RAGEL": 11,
            "R": 12,
            "NU": {"POD": 10, "NINJA": {"1967": 8, "2007": 9}},
        },
    }

    while not type(x) is int:
        x = x[list(set(d) & set(x.keys()))[0]]

    return x

#5
import math


def main(y, z, x):
    ans = 0
    n = len(y)
    for i in range(1, n + 1):
        ans += math.exp(z[n + 1 - math.ceil(i / 4) - 1] / 46
                        - y[math.ceil(i / 4) - 1] ** 3 / 12 - 72
                        * x[math.ceil(i / 2) - 1] ** 2) ** 4 / 9
    return ans
