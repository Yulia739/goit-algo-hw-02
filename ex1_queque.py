import queue
import random
import time

# Creating a queue for storing requests
request_queue = queue.Queue()

# Function for generating new requests
def generate_request():
    # Create a new request with a random number
    request_id = random.randint(1000, 9999)
    print(f"A new request with the number {request_id} has been received.")
    # Add the request to the queue
    request_queue.put(request_id)

# Function for processing requests
def process_request():
    if not request_queue.empty():
        # Pulling the first request from the queue
        request_id = request_queue.get()
        print(f"We are processing the request with the number {request_id}.")
    else:
        print("The queue is empty, there are no requests to process.")


def main():
    while True:
        # We generate new requests every 2 seconds
        generate_request()
        time.sleep(2)
        
        # We are processing the request
        process_request()
        
        # Check if the user wants to exit the program
        exit_program = input("Press 'q' to exit or any key to continue: ")
        if exit_program.lower() == 'q':
            print("Exit the program...")
            break


if __name__ == "__main__":
    main()
