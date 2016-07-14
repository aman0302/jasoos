from karamchand.logic.sources.DataSource import DataSource
from karamchand.logic.config.EntityInfoEnum import EntityInfoEnum
from karamchand.logic.clients.FacebookClient import FacebookClient
from karamchand.logic.clients.GoogleSearchClient import GoogleSearchClient
from urllib.parse import urlsplit
import re


class Facebook(DataSource):
    def __init__(self, entity_info):
        super(Facebook, self).__init__()
        self.entity_info = entity_info

    def get_source_name(self):
        return ('Facebook')

    def get_source_data(self):
        facebook_links = self.entity_info.get(EntityInfoEnum.facebook_links.name)

        if not facebook_links:
            GS = GoogleSearchClient()
            facebook_links = GS.get_links_from_google_search(entity_info=self.entity_info, domain=self.get_source_name())

        page_id_list = self.get_page_id_from_links(facebook_links)
        aggregated_source_data = []

        fb = FacebookClient()

        for page_id in page_id_list:
            source_data = fb.get_facebook_data(page_id)
            aggregated_source_data.append(source_data)

        return aggregated_source_data

    def get_page_id_from_links(self, facebook_links):
        page_id_list = []
        for facebook_link in facebook_links:
            if not re.match(r'http(s?)\:', facebook_link):
                facebook_link = 'https://' + facebook_link
            parsed = urlsplit(facebook_link)
            path = parsed.path
            page_id = path.split('/')[1]
            # print (page_id)
            if page_id not in page_id_list:
                page_id_list.append(page_id)

        return page_id_list


'''
source = Facebook()
source.get_source_name()
source.get_source_data()
'''
'''
dict1= {}
dict1[EntityInfoEnum.entity]='midtown comics'
#dict1[EntityInfoEnum.facebook_links.name]=['https://www.facebook.com/happihormones/photos', 'https://www.facebook.com/happihormones/']
a = Facebook(dict1)
#a.get_page_id_from_links(['https://www.facebook.com/happihormones/photos', 'https://www.facebook.com/happihormones/'])

a.get_source_data()
'''