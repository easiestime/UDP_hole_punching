
class CommandPayload:
    def __init__(self, command, payload):
        self.command = command
        self.payload = payload

    def toResponse(self):
        return f"{self.command}\n\n{self.payload}"

