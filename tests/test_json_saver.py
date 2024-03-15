from abc import ABC

from src.AbstractJsonSaver import AbstractJsonSaver
from src.JsonSaver import JsonSaver


def test_json_saver_issubclass():
    assert issubclass(JsonSaver, AbstractJsonSaver)
    assert issubclass(AbstractJsonSaver, ABC)


def test_save_file_read_file(fixture_class_json_saver):
    fixture_class_json_saver.save_file([{'name': 'Ilya'}])

    assert isinstance(fixture_class_json_saver.read_file(), list)
    assert fixture_class_json_saver.read_file() == [{'name': 'Ilya'}]


def test_add_vacancy_to_file_and_delete(fixture_class_list):
    fixture_class_list.add_vacancy_to_file([{'name': 'Not Ilya'}])

    assert fixture_class_list.read_file() == [{'name': 'Not Ilya'}, {'name': 'Ilya'}]

    fixture_class_list.delete_vacancy('Ilya')
    assert fixture_class_list.read_file() == [{'name': 'Not Ilya'}]