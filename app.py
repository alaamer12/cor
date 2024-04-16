class SupportHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        pass


class LevelOneSupport(SupportHandler):
    def handle_request(self, request):
        if request.level == 1:
            print("Level One Support: Request handled")
        elif self.successor:
            self.successor.handle_request(request)


class LevelTwoSupport(SupportHandler):
    def handle_request(self, request):
        if request.level == 2:
            print("Level Two Support: Request handled")
        elif self.successor:
            self.successor.handle_request(request)


class LevelThreeSupport(SupportHandler):
    def handle_request(self, request):
        if request.level == 3:
            print("Level Three Support: Request handled")
        elif self.successor:
            self.successor.handle_request(request)


class Request:
    def __init__(self, level):
        self.level = level


def main():
    # Creating the chain of responsibility
    level_three_support = LevelThreeSupport()
    level_two_support = LevelTwoSupport(level_three_support)
    level_one_support = LevelOneSupport(level_two_support)

    # Test cases
    request1 = Request(2)  # Request at level 2
    request2 = Request(3)  # Request at level 3
    request3 = Request(1)  # Request at level 1

    # Handling requests
    level_one_support.handle_request(request1)
    level_one_support.handle_request(request2)
    level_one_support.handle_request(request3)


if __name__ == "__main__":
    main()
