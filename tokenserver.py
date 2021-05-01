# Copyright © Max Budko, Lev Kvasnikov, Sofie Litvin
# * Tokenserver is an autentification module, fast and portable.


from authlib.jose import jwt
import datetime
import time


class Token():
    @staticmethod
    def generate(issuedat, expires, issuer, algorithm, subject, key):

        header = {'alg': algorithm, "typ": 'JWT'}
        payload = {'iss': issuer, 'iat': issuedat,
                   'exp': expires, 'sub': subject}

        tokenkey = jwt.encode(header, payload, key)

        return tokenkey.decode()


user_id = '128755'

print(int(time.time()))

jwtkey = open('jwtkey.pem', 'r').read()
print(Token.generate(issuedat=int(time.time()), expires=int(time.time()) + 43200,
                     issuer='Mobile Tycoon Login API', algorithm='RS256', subject=user_id, key=jwtkey))
