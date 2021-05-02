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

        # return 
        print(jwt.decode(token, pub_key))
        if jwt.verify(token, pub_key=pub_key, allowed_algs="RS256", checks_optional=True):
            claims = jwt.decode(token, pub_key)
            print(claims)
            return user_id
        else:
            return -1



token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.bYslY6aWlTNi6dHZU-WRUVJC_z_rDOZxry85Rw059kkJMFzpp2wrZzh5V7A7RCRPvYRYhPdBsPXLf3sYTmynl5KArKhS_2YqhiOzn0dUI5NU9to4F0YtR4R9gsR569SqGs1cf0z0ryyJ8xEWHWJiLji6vqBsprgNTfDUH84198tPvT_LzrzRCpEqjcDAFwMke7EkVuBi3Y0IEWUd4JMRZKjdCxOSvbzj-d8PtzDqxgLZFH55WvE61IH_6_cH-N5HsoQtr8yPk-mTcDetw0kVolm6WNMf9a73UMjgqqXYYtaXxmO5abcbBEkYB-CQgjTzVtzvIbAYDWcTXWeax7J03jmXuocASniXyl8OinmLTpq0bqaAENm93uPbMW8zfUz8mrSUoxvJyemnTqNapZmzfcm_ocyLAhqdCVif6qv8MZNvFd0GSkAQP9Dh7Z3rICstzzud_74uZB-JP8cuoyzVodJt7qbz5g3jNJkfClUTv-ypsEmS5AUsN9TH_jjA2bcjHs2XnTaYD4A1a3wgWA8Nd2nxln1e_vUNfG4tjCLlB7Hy7IwyhtQrligbHnd8fP5zs1NKgtfZ7pAdpKV87IdUupdfs-1V0cklDrEZF3wXu27uQlbala_f9O7nx7hd0YjfZFk5Lz7c5m8vVdW7Ns1YlO8zzSzojqMqDnlpjS06Gf7rn4DOV7J3nLs2xeIuqafHPEZ4hap9EzNJGTkCWj5k2nv20Qkm-EZ-F7CiE_yeZLBMpavVh-pKpBBSD934B7j4h4ZIkmUksZY8dH-tBQeqL7V0fMkvM3Rwvbtvc7nMWlHDt8Y1U5UzpruktJZ_LgCT2gc-13GKzAlS1INsw2WPFjcJohIZNO_zki_5sXd8M4N7cR9oOj_HPbWQwSXIHbe37uvMnZTDNI2e_fY6Ts8_hpn9kJMBoXagAXiGvxs8kFQBb97Dp1Kx3Nj7q67E1bxcYMFnGQ2kU5B6foHq1fHEoiwJgqhOllL02f_niP32ArZTn5IXTLnEDxnTGX0kfQ6cGgCvYS0jFqSanSmsIOzxPJr_RNB6DAm5Tn0GUq7Q68B0lrBlVgOtdAuoGjz4aSgX7Qjsdffw6c0VOQljTR5r-tvZD05N4YZ4y68TW6_pzUvWJoWElASkat37S_OR-XAKW9c8K6Y7TYbM4cQLBmW03wKvSm-as9BkouW4H6CLakDD0pWYBNdfw4qawFFRIysF0MqsWOdCU6w-dOsO1J0N-iTduORWNCeoXa4kYYAxH0GHpmhHfyWUycl5aknTgHbrkQ0u3ZsHwWhUsOy7TZCIbElgf3GLGeZS4AgG2sHFGHSvai6neTJ_khHB8-FPxcIs1kJg1uo0Ao1Qqq_PgsBHXl16dtoFXBzegextZ-BlqbYT2Eufh6FUoZLwKoJOiOb6Qbz6ZtR0Ibtdigmr1mCyptHoNkUZQ-Rf3Ms-lPf0LIpbSBE6RdRK4F9ugWz1py82Iney51Jp8q9BG4yAUciCQ7mGl3dm55VcFXgVlut2rnRuknFtyal4ptKo4E-t-mvVHsGzZfAToybZYuJp9Vb8kKKLnmr1PNAnegdXObWEbNG4DZStyOR4m9wONvmD2qcmCRA-iXjh9brymN4nEtIvPC5W9SrdDKfa7fF1MUOVTNzl5SYaCQaUG5Mrodc-AfvFnv-cjQ1UVOWpkMqTe9qN3zobKeSY-ZQT47gqkbuaz7DYtO3OsNY-n5trHJVm3EyzHx3O1kcu7DQo63Ik8s7_vk5lwT0lr6bPR_pxRkCpeqm6NyL8IkgSa2WME2P18yPo5QktPsBDM8cbmzlCtzKq0LJY9OettP9-l_Yu8diOYO_djRA7ja1kHVsxMY6xZDAAqYrQ7h0hbqGNwZo1dsyghjL5z6C-op99FHKlVABPbyYeg9otGpqkDBUiPLMsvMjTSUo5h2Ek5CMEUoaj3Lpozrde01IjvBU8Z9qZ-iDXKFUgoLd74tQrBEUe-5eczHktjXFu543vE96f-uXEl5w5pmoky7fxrIG2IehuaUsU0jtA2iK0kRQf3EkA1hwy9w3Ai-_A_AuFXjJ_PHO04lLoJvv2366JTvC3q5GVq2xLn2c2IOQ5pPjpr31SLXa7DVeA1nqEqy4AhbUXikuTsjI1OFMEoEw1RkaPs0RZ0FkRqHM_gUcMT0NCLTRfKPu-cQymupMeosEuAmFrvUPEPtpICRrlXHRiFLMWnFFKsZmOQsKotMGV8pT3egf0se76ysD7tXETFnnSIwU0qPf8IIkS8wRZO-KnEwPmvoXrQn-MGy4dI4JlToQSOCiLvQQPbuz7oMXDJ13AhAUUsjDGc9wLUZJy73_r8y2LcKhd31hvDmhr9R8fEqHCaXkwsOyKt_f4PfkhKYMma69VpcfEFrKRslCoRDUtwPnlgE-k7fQENQK5BuO9vNlIlvlqyWVBl2wXvIHxQ5V9Ag9I20rpz6GptusMmw4FgEdiF82_vhW4W82oVqT6iqIgXauuq9QccQcxu_wWP8KvXtgT0MxlJjMeda8XAHnAIfV4J83DpIPU4WCmWZqSswd20211YU3s6xHTy7MJddZnTaE52Z4XTEE_aBv4F6ZUUXKwvB5YeewbAkRgkvF41JvMYl7_M82jAmLjpkiGu2YEa4eOQNQnK0zw3_2NaPdlSZEPqCLlJvZodFPolrJevhNCA0NZFolXdGRCuYpoGPwgatopoemLTAZTEMRBoTfio5dFRv41jPcW_gI"

Token.validate(token)