class Robot:
    """一个标示机器人的类"""
    #机器人的数量
    population = 0

    def __init__(self, name):
        """初始化"""
        self.name = name
        print("(初始化 {})".format(self.name))
        #初始化一个机器人后
        #机器人的数量增加一
        Robot.population += 1

    def die(self):
        """I am dying."""
        if Robot.population > 0:
            print("{} is being destroyed!".format(self.name))
            #机器人数量减一
            Robot.population -=  1
            print("There are still {:d} robots working.".format(Robot.population))
        else:
            print("Sorry there is no robot any more.")

    def say_hi(self):
        """Greeeting by the robot.
        Yeah, they can do that.
        """
        print("Hello, my master call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-02")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print("Robots are working...")
print("Work have done.")
droid1.die()
Robot.how_many()
droid2.die()
Robot.how_many()
