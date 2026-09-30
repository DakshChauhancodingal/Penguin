class bird:
    def __init__(self):
        print("Bird is ready")
    def who_is_this(self):
        print("Blu")
    def swim(self):
        print("It swim faster")
class penguin(bird):
    def __init__(self):
        super(). __init__()
        print("Penguin  is ready")
    def who_is_this(self):
        print("Penguin ")
    def run(self):
        print("It run faster")
peggy=penguin()
peggy.who_is_this()
peggy.run()
peggy.swim()
