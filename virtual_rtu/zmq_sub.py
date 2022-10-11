import zmq
import json


def main():
    context = zmq.Context()

    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:55556")
    socket.setsockopt_string(zmq.SUBSCRIBE, "control")

    while True:
        print ("waiting....")
        message = socket.recv_string()
        print(message)
        try:
            json_object = json.loads(message)
            print(json_object["payload"])
        except:
            print("")

if __name__ == '__main__':
    main()
