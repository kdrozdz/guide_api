from api.const import get_name_of_location


class MapperObj:
    def __init__(self, list_of_tupels, object_schema):
        self.list_of_tupels = list_of_tupels
        self.object_schema = object_schema
        self.list_of_dict = []


    def _create_list_of_dict(self):
        for _tuple in self.list_of_tupels:
            my_dict = {}
            for key, value in zip(self.object_schema, _tuple):
                my_dict[key] = value
            self.list_of_dict.append(my_dict)


    def _get_name_of_location(self):
        for _obj in self.list_of_dict:
            _obj['location'] = get_name_of_location(_obj['location'])


    def get_list_of_dict_with_location_name(self):
        self._create_list_of_dict()
        self._get_name_of_location()
        return self.list_of_dict