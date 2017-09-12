import serial

class LGTVResponse(object):
    def __init__(self, command, setid, rescode, value, res):
        self.command = command
        self.setid = setid
        self.rescode = rescode
        self.value = value
        self.res = res

class LGTV(object):
    def __init__(self, port='COM1', setid : bytes = b'01'):
        self.port = port
        if type(setid) is bytes:
            self.setid = setid
        elif type(setid) is str:
            self.setid = bytes(setid, 'utf-8')

    def powermode(self):
        return self.write(b'ka', b'FF')

    def poweron(self):
        return self.write(b'ka', b'01')

    def poweroff(self):
        return self.write(b'ka', b'00')

    def write(self, command : bytes, argument : bytes):
        retval = None

        with serial.Serial(port=self.port, timeout=5) as ser:
            ser.write(command + b' ' + self.setid + b' ' + argument + b'\n')
            retval = self.decode(ser.readline())

        return retval

    def decode(self, res: bytes):
        command = res[0]
        setid = ((res[2] - 48) * 16) + (res[3] - 48)
        rescode = res[5:7].decode('utf-8')
        value = ((res[7] - 48) * 16) + (res[8] - 48)
        return LGTVResponse(command, setid, rescode, value, res)