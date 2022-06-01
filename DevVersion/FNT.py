# Sensor: Sensor ID, Status, Location.
class Sensor(object):
    def __init__(self, sid, status, location):
        self.sid = sid
        self.status = status
        self.location = location


# Dataset: Data Type, Data.
class Dataset(object):
    def __init__(self, datatype, data):
        self.datatype = datatype
        self.data = data


# Packet: Packet ID, Timestamp, Auditee, Auditor, Sensor Info, Dataset.
class Packet(Sensor, Dataset):

    def __init__(self, pid, timestamp, auditee1, auditee2, sid, status, location, datatype, data):

        Sensor.__init__(self, sid, status, location)
        Dataset.__init__(self, datatype, data)

        self.pid = pid
        self.timestamp = timestamp
        self.auditee1 = auditee1
        self.auditee2 = auditee2
        self.auditor = []
        self.disable = False

    def get_pid(self):
        return self.pid

    def get_timestamp(self):
        return self.timestamp

    def get_auditee(self):
        a1 = self.auditee1
        a2 = self.auditee2

        if a1 is None and a2 is None:
            return [None, None]
        elif a1 is not None and a2 is None:
            return [a1.get_pid(), None]
        elif a2 is not None and a1 is None:
            return [None, a2.get_pid()]
        else:
            return [a1.get_pid(), a2.get_pid()]

    def get_sid(self):
        return self.sid

    def get_status(self):
        return self.status

    def get_location(self):
        return self.location

    def get_datatype(self):
        return self.datatype

    def get_data(self):
        return self.data

    def print_sensor(self):
        print("Sensor ID: {0}, Status: {1}, Location: {2}".format(self.sid, self.status, self.location))

    def print_dataset(self):
        print("Data: {0} = {1}".format(self.datatype, self.data))

    def print_packet(self):
        print("Packet ID: {0}, Timestamp: {1}, Auditee: [{2}, {3}]"
              .format(self.pid, self.timestamp, self.auditee1, self.auditee2))
