# -*- coding: utf-8 -*-

from UserAuthorization import session
from BaseFunc import BaseFunc
from config import GTK_GPA_KEY, URL_ORAWCI, URL_MEDIA


class MediaFunc(BaseFunc):
    def __init__(self):
        self.number_schema = ''
        self.id_adding_media = ''
        self.key_delete = ''

    def create_schema(self):
        # собираем данные
        data_schema = self.formation_schema_params(GTK_GPA_KEY)
        # выполняем запрос добавления новой схемы
        result_adding_schema = session.post('%s' % URL_ORAWCI,
                                                    data_schema)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_adding_schema = self.decode_responce_to_text(result_adding_schema)
        # вытаскиваем номер добавленной схемы
        self.number_schema = self.get_number_schema(decode_result_adding_schema)
        print self.number_schema

    def add_media(self):
        # собираем данные для добавления медиаматериала
        encoder = self.formation_media_params(self.number_schema)
        # добавляем медиа
        result_adding_media = session.post('%s' % URL_MEDIA,
                                           data = encoder,
                                           headers={'Content-Type': encoder.content_type})
        # декодируем приходящий ответ в строку и получаем id добавленного медиа
        self.id_adding_media = self.decode_responce_to_text(result_adding_media)

    def verify_schema_added(self):
        # формируем данные для запроса списка схем
        data_list_schema = self.formation_params_list_schems(GTK_GPA_KEY)
        # выполняем запрос получения списка схем
        result_get_list_schema = session.post('%s' % URL_ORAWCI,
                                                    data_list_schema)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_get_list_schema = self.decode_responce_to_text(result_get_list_schema)
        # достаем значения всех ключей схем из списка
        keys_list_schemas = self.get_value_keys_schemas(decode_result_get_list_schema)
        # проверяем что в списке присутствует ключ добавленной схемы
        assert keys_list_schemas.find(self.number_schema) != -1,\
            "AssertionError: Media wasn't added"

    def delete_schema(self):
        # собираем данные для удаления схемы
        data_deleted_schema = self.get_params_delete(self.number_schema)
        # выполняем запрос удаления схемы
        result_deleting_schema = session.post('%s' % URL_ORAWCI,
                                                    data_deleted_schema)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_deleting_schema = self.decode_responce_to_text(result_deleting_schema)
        # получаем значения потверждющее удаления из ответа сервера
        self.key_delete = self.get_key_deleting_schema(decode_result_deleting_schema)
        print self.key_delete

    def verify_schema_deleted(self):
        assert self.key_delete == '1',\
            "AssertionError: Schema wasn't deleted"
