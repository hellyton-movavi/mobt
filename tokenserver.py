# Copyright © Max Budko, Lev Kvasnikov, Sofie Litvin
# * Tokenserver is an autentification module, fast and portable.


import jwt
import inspect
import datetime
import time


class Token():
    @staticmethod
    def generate(issuedat, expires, issuer, algorithm, subject, key):

        header = {'alg': algorithm, "typ": 'JWT'}
        payload = {'iss': issuer, 'iat': issuedat,
                   'exp': expires, 'sub': subject}

        tokenkey = jwt.encode(payload, key, algorithm='RS256', headers=header)

        return tokenkey

    @staticmethod
    def validate(token):
        #  Проверить на корректность token
        #  Если token некорректный вернуть -1
        #  в противном случае вернуть user_id

        # processed_token = jwt.process_jwt(token)
        # kid = processed_token[0]['kid']
        # if kid not in certs:
        #     raise UnknownKID

        f = open("jwtpublic.pem", "rb")
        pub_key = f.read()
        f.close()

        try:
            decoded_claims = jwt.decode(token, pub_key, algorithms=["RS256"])
            return decoded_claims
        except Exception as e:
            print(e)
            if isinstance(e, jwt.exceptions.ExpiredSignatureError):
                return -1

            elif isinstance(e, jwt.exceptions.InvalidSignatureError):
                return -1

            elif isinstance(e, jwt.exceptions.InvalidIssuedAtError):
                return -1


jwttoken = Token.generate(issuedat=datetime.datetime.utcnow(), expires=datetime.datetime.utcnow() + datetime.timedelta(hours=12),
                                                  issuer = 'Mobile Tycoon Login API', algorithm = 'RS512', subject = user_id=1, key = jwtkey)