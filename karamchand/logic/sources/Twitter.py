from karamchand.logic.sources.DataSource import DataSource
from karamchand.logic.clients.GoogleSearchClient import GoogleSearchClient
from karamchand.logic.clients.TwitterClient import TwitterClient
from karamchand.logic.config.EntityInfoEnum import EntityInfoEnum

class Twitter(DataSource):
    def __init__(self, entity_info):
        super(Twitter, self).__init__()
        self.entity_info = entity_info

    def get_source_name(self):
        return ('Twitter')

    def get_source_data(self):
        twitter_links = self.entity_info.get(EntityInfoEnum.twitter_links.name)

        if not twitter_links:
            GS = GoogleSearchClient()
            twitter_links = GS.get_links_from_google_search(entity_info=self.entity_info, domain=self.get_source_name())

        page_id_list = self.get_page_id_from_links(twitter_links)
        aggregated_source_data = []

        twitter = TwitterClient()

        for page_id in page_id_list:
            source_data = twitter.get_twitter_data(page_id)
            aggregated_source_data.append(source_data)

        return aggregated_source_data