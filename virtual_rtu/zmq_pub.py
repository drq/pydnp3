import zmq
import time


def main():
    context = zmq.Context()

    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:55555")

    while True:
        time.sleep(10)
        print("Publishing...")
        socket.send_string("point {\"foo\" : \"bar\"}")


if __name__ == '__main__':
    main()