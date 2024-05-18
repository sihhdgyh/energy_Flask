class result:
    code = 200
    data = None
    msg = ''
    def __init__(self,code,data,msg):
        self.code=code
        self.data=data
        self.msg=msg

    def jsonformat(self):
        return {
            "code": self.code,
            "data": self.data,
            "msg": self.msg
        }

