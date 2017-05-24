# -*- coding: utf-8 -*-

from UserAuthorization import session
from config import GTK_GPA_KEY,\
    DG_GPA_KEY,\
    AVO_KEY,\
    PS_GPA_KEY, URL_ORAWCI
from BaseFunc import BaseFunc




class TreeFunc(BaseFunc):

    def __init__(self):

        self.number_mode_gtk = ''
        self.number_mode_ps90 = ''
        self.number_mode_dg90 = ''
        self.number_mode_avo = '-1'  # значальное значение -1 т.к. корректное присваемое значение - пустое


    def get_count_element(self):
        # формируем параметры для запроса получения дерева КС
        params_get_full_tree = self.formation_params_get_tree()
        # выполняем запрос на получение дерева
        full_tree = session.get('%s' % URL_ORAWCI,
                                params=params_get_full_tree)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        self.decode_text_tree = self.decode_responce_to_text(full_tree)

    def verify_count_elements_tree(self):
        # получаем количество всех объектов в дереве
        count_element_tree = self.get_list_elements_tree(self.decode_text_tree)
        assert count_element_tree > 0,\
            "AssertionError: Not objects in tree"


    def get_mode_gtk_object(self):
        # выполняем запрос для получения варианта проведение
        mode_gtk =  session.get('%s' % URL_ORAWCI,
                                params=self.get_param_mode(GTK_GPA_KEY))
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        self.decode_mode_gtk = self.decode_responce_to_text(mode_gtk)
        # вытаскиваем число соответствующее варианту из xml кода
        self.number_mode_gtk = self.get_number_mode(self.decode_mode_gtk)

    def verify_mode_number_gtk(self):
        # проверяем что возвращает правильные варианты проведения: 1 и 3
        assert self.number_mode_gtk == '13',\
            "AssertionError: Mode for GTK-10-4 object is wrong"
        print 'Mode for GTK-10-4 object is correct'


    def get_mode_ps_object(self):
        # выполняем запрос для получения варианта проведение
        mode_ps90 = session.get('%s' % URL_ORAWCI,
                                params=self.get_param_mode(PS_GPA_KEY))
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        self.decode_mode_ps90 = self.decode_responce_to_text(mode_ps90)
        # вытаскиваем число соответствующее варианту из xml кода
        self.number_mode_ps90 = self.get_number_mode(self.decode_mode_ps90)

    def verify_mode_number_ps(self):
        # проверяем что возвращает правильный вариант проведения: 3
        assert self.number_mode_ps90 == '3',\
            "AssertionError: Mode for PS-90 object is wrong"
        print 'Mode for PS-90 object is correct'


    def get_mode_dg_object(self):
        # выполняем запрос для получения варианта проведение
        mode_dg90 = session.get('%s' % URL_ORAWCI,
                                params=self.get_param_mode(DG_GPA_KEY))
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        self.decode_mode_dg90 = self.decode_responce_to_text(mode_dg90)
        # вытаскиваем число соответствующее варианту из xml кода
        self.number_mode_dg90 = self.get_number_mode(self.decode_mode_dg90)

    def verify_mode_number_dg(self):
        # проверяем что возвращает правильный вариант проведения: 3
        assert self.number_mode_dg90 == '3',\
            "AssertionError: Mode for DG-90 object is wrong"
        print 'Mode for DG-90 object is correct'


    def get_mode_avo_object(self):
        # выполняем запрос для получения варианта проведение
        mode_avo = session.get('%s' % URL_ORAWCI,
                               params=self.get_param_mode(AVO_KEY))
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        self.decode_mode_avo = self.decode_responce_to_text(mode_avo)
        # вытаскиваем число соответствующее варианту из xml кода
        self.number_mode_avo = self.get_number_mode(self.decode_mode_avo)

    def verify_mode_number_avo(self):
        # проверяем что возвращает правильный вариант проведения: пустое значение
        assert self.number_mode_avo == '',\
            "AssertionError: Mode for AVO object isn't empty value"
        print 'Mode for AVO object is empty value'
