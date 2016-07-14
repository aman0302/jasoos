from karamchand.logic.config.EntityInfoEnum import EntityInfoEnum
from urllib import request, parse, error
import json


class GoogleSearchClient():
    def get_google_search_data(self, query_term, domain):

        query = (query_term + "+website:" + domain.lower()+".com").replace(" ", "+")
        print(query)
        url = "https://www.googleapis.com/customsearch/v1/?key=AIzaSyC7zSddHHJ_scz9RZ2J5gY8HjZINGeeL-g&cx=008788000725238317546:f4uuwzmhcbq&q=" + query

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

    def get_links_from_google_search(self, entity_info, domain):

        entity = ''
        address1 = ''
        city = ''
        if EntityInfoEnum.entity.name in entity_info:
            entity = entity_info.get(EntityInfoEnum.entity.name)
        if EntityInfoEnum.address1.name in entity_info:
            address1 = entity_info.get(EntityInfoEnum.address1.name)
        if EntityInfoEnum.city.name in entity_info:
            city = entity_info.get(EntityInfoEnum.city.name)

        query = entity + " " + address1 + " " + city

        dump = self.get_google_search_data(query, domain)

        links = self.extract_links_from_dump(dump)
        print(links)

        return links

    def extract_links_from_dump(self, dump):

        if 'items' in dump:
            items = dump['items']
            links = []

            for item in items:

                if 'link' in item:
                    links.append(item['link'])

        return links


# everything is fine

# get_google_search_data(queryTerm="reliance", website="facebook.com")
'''
a = GoogleSearchClient()
a.get_links_from_google_search({'entity': 'Reliance', 'city': 'mumbai'}, 'facebook.com')
'''