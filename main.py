#  CoR [Chain of Responsibility] design pattern
"""
Definition:
The Chain of Responsibility pattern is a behavioral design pattern that allows an object to pass a request along a chain of handlers. Each handler in the chain decides either to process the request or to pass it along the chain to the next handler.

Example Scenario:
Let's consider a scenario where we have a chain of processors that handle different types of requests based on their priority. We will implement this using the CoR pattern.
"""

from abc import ABC, abstractmethod

# Request class
class Request:
    def __init__(self, content, priority):
        self.content = content
        self.priority = priority

# Abstract Handler class
class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

# Concrete Handlers
class Priority1Handler(Handler):
    def handle_request(self, request):
        if request.priority == 1:
            print(f"Priority 1 Handler: {request.content}")
        elif self.successor:
            self.successor.handle_request(request)

class Priority2Handler(Handler):
    def handle_request(self, request):
        if request.priority == 2:
            print(f"Priority 2 Handler: {request.content}")
        elif self.successor:
            self.successor.handle_request(request)

class Priority3Handler(Handler):
    def handle_request(self, request):
        if request.priority == 3:
            print(f"Priority 3 Handler: {request.content}")
        elif self.successor:
            self.successor.handle_request(request)

# Client
if __name__ == "__main__":
    # Create the chain of responsibility
    handler3 = Priority3Handler()
    handler2 = Priority2Handler(handler3)
    handler1 = Priority1Handler(handler2)

    # Create requests
    request1 = Request("Request 1", 1)
    request2 = Request("Request 2", 2)
    request3 = Request("Request 3", 3)
    request4 = Request("Request 4", 4)

    # Process requests
    handler1.handle_request(request1)
    handler1.handle_request(request2)
    handler1.handle_request(request3)
    handler1.handle_request(request4)
