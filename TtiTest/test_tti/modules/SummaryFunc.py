# -*- coding: utf-8 -*-

from UserAuthorization import session
from config import URL_ORAWCI
from BaseFunc import BaseFunc


class SummaryFunc(BaseFunc):

    def __init__(self):
        self.decode_text_list =''

    def get_count_element_ks(self):
        # формируем параметры для запроса получения списка КС в сводной таблице
        params_get_full_list_ks = self.formation_params_get_list()
        # выполняем запрос на получение списка всех компресорных станции
        full_list_ks = session.get('%s' % URL_ORAWCI,
                                params=params_get_full_list_ks)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        self.decode_text_list = self.decode_responce_to_text(full_list_ks)
        print self.decode_text_list

    def verify_count_elements_list_ks(self):
        # получаем количество всех компресорных станций в сводной таблице
        count_element_ks = self.get_list_ks(self.decode_text_list)
        assert count_element_ks > 0,\
            "AssertionError: Not objects in summary information table"