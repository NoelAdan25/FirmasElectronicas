import string
from Clases.School.SchoolActions import SchoolAction


class SchoolAreas(SchoolAction):
    __area_id: int
    __area_name: string

    def __init__(self, class_area: {}):
        self.__area_id = class_area["area_id"]
        self.__area_name = class_area["area_name"]  # We save that the classmate stayed

    @property
    def get_area_name(self):
        return self.__area_name

    @property
    def get_area_id(self):
        return self.__area_id

    def insert_area_school(self):
        return ""

    def update_area_school(self):
        return ""

    def select_area_school(self):
        return {0, "Telemática"}
