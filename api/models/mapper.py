import datetime
import os
import pytz

from api.const import get_name_of_location


class MapperObj:
    created_time = "created_time"
    average = "average"

    def __init__(self, raw_data, object_schema, location_name=False):
        self.raw_data = raw_data
        self.object_schema = object_schema
        self.location_name = location_name
        self.list_of_dict = []
        self.single_dict = {}

    @staticmethod
    def _get_time_with_utc(naive_datatime_str):
        user_time_zone = pytz.timezone(os.environ['USER_TIMEZONE'])
        naive = datetime.datetime.strptime(naive_datatime_str, '%Y-%m-%d %H:%M:%S.%f').replace(microsecond=0)
        aware = user_time_zone.localize(naive)
        return aware.strftime('%Y-%m-%d %H:%M:%S')

    def _looping_zip(self, schema, raw_data):
        my_dict = {}
        for key, value in zip(schema, raw_data):
            if key == self.created_time:
                my_dict[key] = self._get_time_with_utc(value)
            elif key == self.average:
                my_dict[key] = str(value)
            else:
                my_dict[key] = value
        return my_dict

    def _create_list_of_dict(self):
        for _tuple in self.raw_data:
            self.list_of_dict.append(self._looping_zip(self.object_schema, _tuple))

    def _get_name_of_location(self):
        if self.list_of_dict:
            for _obj in self.list_of_dict:
                _obj['location'] = get_name_of_location(_obj['location'])
        elif self.single_dict:
            self.single_dict["location"] = get_name_of_location(self.single_dict["location"])

    def get_specifict_dict(self):
        self.single_dict = self._looping_zip(self.object_schema, self.raw_data)
        if self.location_name:
            self._get_name_of_location()
        return self.single_dict

    def get_list_of_dict(self):
        self._create_list_of_dict()
        if self.location_name:
            self._get_name_of_location()
        return self.list_of_dict
