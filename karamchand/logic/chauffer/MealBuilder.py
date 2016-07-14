from karamchand.logic.sources.Facebook import Facebook
from karamchand.logic.sources.Twitter import Twitter
from karamchand.logic.config.DataSourceEnum import DataSourceEnum
from karamchand.logic.config.EntityInfoEnum import EntityInfoEnum


class MealBuilder():
    def __init__(self, entity_info, required_data_source):
        self.entity_info = entity_info
        self.required_data_sources = required_data_source

    def build_meal(self):
        meal_items = self.get_data_source_object_list(self.required_data_sources)
        data={}

        for meal_item in meal_items:
            data[meal_item.get_source_name()]=meal_item.get_source_data()

        return data

    def get_data_source_object_list(self, required_data_sources):
        object_list = []

        '''
        if DataSourceEnum.Facebook.name in required_data_source:
            facebook = Facebook(self.entity_info)
            object_list.append(facebook)

        #more sources

        '''

        for required_data_source in required_data_sources:
            for data_source in DataSourceEnum:
                if data_source.name==required_data_source:

                    constructor = globals()[data_source.name]
                    instance = constructor(self.entity_info)
                    object_list.append(instance)

                    break

        return object_list

'''
dict1 = {}
dict1[EntityInfoEnum.facebook_links.name] = ['https://www.facebook.com/happihormones/photos', 'https://www.facebook.com/happihormones/']
a = MealBuilder(entity_info=dict1, required_data_source=['Facebook', 'Twitter'])
a.build_meal()
'''