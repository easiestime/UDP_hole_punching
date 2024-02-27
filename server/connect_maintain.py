
import datetime
class Connect_Maintain:

    connections = {}
    def keep_alive(self, address, payload):
        address_info = {
            "address": address[0],
            "port": address[1],
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.connections[payload] = address_info
        for key, exitedAddress in self.connections.items():
            insert_time = datetime.datetime.strptime(exitedAddress.get("time"), "%Y-%m-%d %H:%M:%S")
            if datetime.datetime.now() + datetime.timedelta(minutes=1.0) < insert_time:
                self.connections.pop(key)



