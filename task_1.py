from queue import Queue
import random

class Order:
    def __init__(self, data):
        self.data = data

    def process(self):
        print(f"Processing Order #{self.data}")

container = Queue()

def generate_request():
    order = Order(random.randint(0, 1000))
    container.put(order)
    
def process_request():
    if container.empty():
        print(f"Queue is empty")
    else:
        order: Order = container.get()
        order.process()

def main():
    while True :
        userinput = input("write 'stop' to exit programm or enter to continue: ")
        generate_request()
        process_request()
        if userinput == 'stop':
            break

    
if __name__ == "__main__":
    main()