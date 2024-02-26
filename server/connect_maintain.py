
import datetime
class Connect_Maintain:

    connections = []
    def keep_alive(self, address):
        address_info = {
            "address": address[0],
            "port": address[1],
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        try:
            index = self.connections.index(address_info)
            self.connections.insert(index, address_info)
            for exitedAddress in self.connections:
                insert_time = datetime.datetime.strptime(exitedAddress.get("time"), "%Y-%m-%d %H:%M:%S")
                if datetime.datetime.now() + datetime.timedelta(minutes=1.0) < insert_time:
                    self.connections.remove(exitedAddress)
        except ValueError as e:
            self.connections.append(address_info)



