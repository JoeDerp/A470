import random
import simpy

RANDOM_SEED = 42
NEW_CUSTOMER = 0  # Event for a new customer arriving
ORDER_COMPLETE = 1  # Event for an order being completed

class FastFoodRestaurant(object):
    def __init__(self, env, num_servers, service_time_range):
        self.env = env
        self.queue = simpy.Resource(env, capacity=10)  # Queue with a maximum capacity of 10
        self.servers = simpy.Resource(env, capacity=num_servers)
        self.service_time_range = service_time_range
        self.customer_arrivals = env.process(self.generate_customers())
        self.orders_served = 0
        self.total_wait_time = 0

    def generate_customers(self):
        while True:
            # Generate a new customer with an interarrival time sampled from an exponential distribution
            interarrival_time = random.expovariate(1.0 / 3.0)  # 3 customers per minute on average
            yield self.env.timeout(interarrival_time)
            self.env.process(self.handle_customer())

    def handle_customer(self):
        # Request a spot in the queue
        with self.queue.request() as request:
            yield request
            service_time = random.uniform(*self.service_time_range)
            with self.servers.request() as server_request:
                start_time = self.env.now
                yield server_request
                yield self.env.timeout(service_time)
                wait_time = self.env.now - start_time
                self.total_wait_time += wait_time
                self.orders_served += 1

def main():
    random.seed(RANDOM_SEED)
    num_servers = 3
    service_time_range = (1, 3)  # Service time range in minutes
    env = simpy.Environment()
    restaurant = FastFoodRestaurant(env, num_servers, service_time_range)
    env.run(until=30)  # Run the simulation for 30 minutes

    print(f"Orders served: {restaurant.orders_served}")
    print(f"Average wait time: {restaurant.total_wait_time / restaurant.orders_served:.2f} minutes")

if __name__ == "__main__":
    main()