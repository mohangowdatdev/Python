class Parrot:
    def fly(self):
        print("Can Fly!!")

    def swim(self):
        print("Cant swim!!")


class Penguin:
    def fly(self):
        print("Cant Fly!!")

    def swim(self):
        print("Can swim!!")


def flying_test(bird):
    bird.fly()

