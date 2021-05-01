from RadiusApp import RadiusAuthen
from dotenv import load_dotenv
from nameko.rpc import rpc

import os

load_dotenv()

server = os.getenv('RADIUS_SERVER')
secret = os.getenv('RADIUS_SECRET')

r = RadiusAuthen(server, secret)

class RadiusAuthentication:
    name = 'radius'

    @rpc
    def authentication(self, username, password):
        return r.authentication(username, password)