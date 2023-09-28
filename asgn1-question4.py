class Penguin:
    def __init__(self, lenArms = 2, lenLegs = 2, numEyes = 2, tail = True, furry = True) -> None:
        self.lenArms = lenArms
        self.lenLegs = lenLegs
        self.numEyes = numEyes
        self.tail = tail
        self.furry = furry

    def describe(self):
        print("Length of arms:",  self.lenArms)
        print("\nLen of legs:", self.lenLegs)
        print("\nNumber of eyes:", self.numEyes)
        print("\nHas a tail:", self.tail)
        print("\nHas fur:", self.furry)

p = Penguin()
p.describe()
    