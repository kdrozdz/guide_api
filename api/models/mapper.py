from api.const import get_name_of_location


class MapperObj:
    def __init__(self, list_of_tupels, req_object):
        self.list_of_tupels = list_of_tupels
        self.req_object = req_object
        self.list_of_dict = []


    def _create_list_of_dict(self):
        my_dict = {}
        for _tuple in self.list_of_tupels:
            for key, value in zip(self.req_object, _tuple):
                my_dict[key] = value
            self.list_of_dict.append(my_dict)


    def get_list_of_dict_with_location_name(self):
        self._create_list_of_dict()
        return self.list_of_dict