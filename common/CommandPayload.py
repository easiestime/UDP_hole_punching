def from_str(string: str):
    split_strings = string.split('\n\n')
    command = split_strings[0]
    start_index = string.find('\n\n')
    if start_index < 0:
        return None
    payload = string[start_index + 2:]
    return CommandPayload(command, payload)


class CommandPayload:
    def __init__(self, command, payload):
        self.command = command
        self.payload = payload

    def toResponse(self):
        return f"{self.command}\n\n{self.payload}"

