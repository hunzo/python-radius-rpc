import radius

class RadiusAuthen:
    def __init__(self, server, secret):
        self.sever = server
        self.secret = secret
    
    def authentication(self, username, password):
        r = radius.Radius(self.secret, host=self.sever, port=1812)
        return 'Access-Accept' if r.authenticate(username, password) else 'Access-Reject'
