from urllib import request, parse, error
import json

class FacebookClient():
    def get_facebook_data(self, pageID):

        url = "https://graph.facebook.com/"+pageID+"/?access_token=767037023394997|oKftStqSDp8OcMQgd1IvDc02OA4"
        try:
            response = request.urlopen(url)
            json_response = json.loads(response.read().decode('utf-8'))

        except error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            return None
        except error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
            return None
        else:
            print(json_response)
            return json_response


# everything is fine
f =FacebookClient()

f.get_facebook_data("Midtown-Comics-Downtown-310715902311463")
