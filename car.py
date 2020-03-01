import simpy

class Car(object):
    def __init__(self, env):
        self.env = env
        # Start run() every time a Car is created
        self.action = env.process(self.run())

    def run(self):
        while True:
            yield env.timeout(driving_time)
            print("%s arrving to %d" % (name, self.env))
            with bcs.request as req:
                yield req

                charge_duration = 5
                print("%s starting to charge at %d" % (name, self.env))
                yield env.timeout(charge_duration)
                print("%s leaving the battery charging station at %d" % (name, self.env))

    def charge(self, env):
        yield self.env.timeout(duration)


def car(env, name, bcs, driving_time, charge_duration):
    while True:
        yield env.timeout(driving_time)
        print("%s arrving to %d" % (name, env.now))
        with bcs.request() as req:
            yield req

            print("%s starting to charge at %d" % (name, env.now))
            yield env.timeout(charge_duration)
            print("%s leaving the battery charging station at %d" % (name, env.now))


env = simpy.Environment()
bcs = simpy.Resource(env, capacity=2)

for i in range(4):
    env.process(car(env, 'Car %d' % i, bcs, i * 2, 5))

env.run()
