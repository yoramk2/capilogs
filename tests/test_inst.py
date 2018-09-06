from inst import instrumenter


def handle_event_request(event, context):
    print("start "+str(event))


def main():
    handle_event_request({}, {})

if __name__ == '__main__':
    main()

