# -*- coding: utf-8 -*-

from UserAuthorization import session
from BaseFunc import BaseFunc
from config import GTK_GPA_KEY,\
    MODE_1,\
    MODE_3,\
    correct_value_power_3mode,\
    correct_value_power_1mode, \
    correct_value_ktc_1mode, \
    correct_value_ktc_3mode,\
    correct_value_coefficient_efficiency_1mode,\
    correct_value_coefficient_efficiency_3mode, URL_ORAWCI


class GtkFunc(BaseFunc):
    def __init__(self):
        self.gtk_number_measurement_3mode = ''
        self.gtk_number_measurement_1mode = ''

        self.dtk_list_key_params_3mode = []
        self.dtk_list_key_params_1mode = []

        self.result_save_measurement_third_mode = ''
        self.list_params_value = ''
        self.decode_result_updata_list = ''
        self.agree_deleted_number = ''

    ######################## Добавление пустого измерения #####################

    def adding_measurement_3mode(self):
        # собираем данные
        data_adding_third_mode = self.formation_measuremenr_params(GTK_GPA_KEY,
                                                                   MODE_3)
        # выполняем запрос добавления нового измерения
        result_adding_measurement_gtk = session.post('%s' % URL_ORAWCI,
                                                     data_adding_third_mode)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_adding_measurement_gtk = self.decode_responce_to_text(result_adding_measurement_gtk)
        # вытаскиваем номер добавленного измерения из запроса
        self.gtk_number_measurement_3mode = self.get_number_measurement(decode_result_adding_measurement_gtk)
        print self.gtk_number_measurement_3mode


    def adding_measurement_1mode(self):
        # собираем данные
        data_adding_one_mode = self.formation_measuremenr_params(GTK_GPA_KEY,
                                                                 MODE_1)
        # выполняем запрос добавления нового измерения
        result_adding_measurement_gtk = session.post('%s' % URL_ORAWCI,
                                                     data_adding_one_mode)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_adding_measurement_gtk = self.decode_responce_to_text(result_adding_measurement_gtk)
        # вытаскиваем номер добавленного измерения из запроса
        self.gtk_number_measurement_1mode = self.get_number_measurement(decode_result_adding_measurement_gtk)

    def verify_adding_measurement_3mode(self):
        # проверяем что длина строки > 0, т.е. в ней номер добавленного измерения
        assert len(self.gtk_number_measurement_3mode) > 0,\
            "AssertionError: Measurement wasn't added"

    def verify_adding_measurement_1mode(self):
        # проверяем что длина строки > 0, т.е. в ней номер добавленного измерения
        assert len(self.gtk_number_measurement_1mode) > 0,\
            "AssertionError: Measurement wasn't added"

    ###################### Получение ключей-параметров для полей закладки Входные данные ######

    def get_list_key_params_measurement_3mode(self):
        # получаем ключи параметров для каждого из значений данных, они используются для заполнения данными измерения
        gtk_list_params_key = self.formation_list_params_key(self.gtk_number_measurement_3mode)
        result_get_list_params = session.get('%s' % URL_ORAWCI,
                                             params=gtk_list_params_key)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_get_list_params = self.decode_responce_to_text(result_get_list_params)
        # вытаскиваем ключи для всех параметров и складываем их в список
        self.dtk_list_key_params_3mode = self.get_key_value_measurement(decode_result_get_list_params)
        print len(self.dtk_list_key_params_3mode)

    def get_list_key_params_measurement_1mode(self):
        # получаем ключи параметров для каждого из значений данных, они используются для заполнения данными измерения
        gtk_list_params_key = self.formation_list_params_key(self.gtk_number_measurement_1mode)
        result_get_list_params = session.get('%s' % URL_ORAWCI,
                                             params=gtk_list_params_key)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_get_list_params = self.decode_responce_to_text(result_get_list_params)
        # вытаскиваем ключи для всех параметров и складываем их в список
        self.dtk_list_key_params_1mode = self.get_key_value_measurement(decode_result_get_list_params)
        print len(self.dtk_list_key_params_1mode)

    ######################## Добавление числовых значений в поля входных данных

    def save_measurement_3mode(self):
        # собираем данные для добавление данных в измерение
        data_save_measurement_third_mode = self.formation_save_params_gtk_3mode(self.gtk_number_measurement_3mode,
                                                                            self.dtk_list_key_params_3mode)
        # выполняем запрос сохранения нового измерения
        self.result_save_measurement_third_mode = session.post('%s' % URL_ORAWCI,
                                                               data_save_measurement_third_mode)
        # формируем данные что бы получить отображение расчетов
        data_for_calculation = self.formation_calculation_params(self.gtk_number_measurement_3mode)
        self.list_params_value = session.get('%s' % URL_ORAWCI,
                                             params=data_for_calculation)

    def save_measurement_1mode(self):
        # собираем данные для добавление данных в измерение
        data_save_measurement_first_mode = self.formation_save_params_gtk_1mode(self.gtk_number_measurement_1mode,
                                                                            self.dtk_list_key_params_1mode)
        # выполняем запрос сохранения нового измерения
        self.result_save_measurement_first_mode = session.post('%s' % URL_ORAWCI,
                                                               data_save_measurement_first_mode)
        # формируем данные что бы получить отображение расчетов
        data_for_calculation = self.formation_calculation_params(self.gtk_number_measurement_1mode)
        self.list_params_value = session.get('%s' % URL_ORAWCI,
                                             params=data_for_calculation)

    def verify_edit_measurement_3mode(self):
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_save_measurement_third_mode = self.decode_responce_to_text(
            self.result_save_measurement_third_mode)
        # проверяем что сохранение измерения было успешным и нам возвратилась 1
        index_save_correct = self.get_value_save_correct(decode_result_save_measurement_third_mode)
        assert index_save_correct == '1',\
            "AssertionError: Measurement wasn't saved correctly"

    def verify_edit_measurement_1mode(self):
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_save_measurement_first_mode = self.decode_responce_to_text(
            self.result_save_measurement_first_mode)
        # проверяем что сохранение измерения было успешным и нам возвратилась 1
        index_save_correct = self.get_value_save_correct(decode_result_save_measurement_first_mode)
        assert index_save_correct == '1',\
            "AssertionError: Measurement wasn't saved correctly"

    ########################## Проверка полей Мощность,КПД,КТУ ###################

    def updata_gpa_list(self):
        # получаем данные для обновления списка ГПА
        updata_list_params = self.formation_updata_list_params(GTK_GPA_KEY)
        # выполняем запрос получения списка измерений в ГПА
        result_updata_list = session.get('%s' % URL_ORAWCI,
                                         params=updata_list_params)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        self.decode_result_updata_list = self.decode_responce_to_text(result_updata_list)

    def verify_calculation_power_gtk_3mode(self):
        print self.decode_result_updata_list
        # достаем значение мощности для добавленного измерения из списка измерений
        power_value_Mvt_3mode = self.get_value_power(self.gtk_number_measurement_3mode,
                                                     self.decode_result_updata_list)
        # проверяем что полученное значение равно контрольному
        assert power_value_Mvt_3mode == correct_value_power_3mode,\
            "AssertionError: Power 3 mode wasn't calculated correctly"

    def verify_calculation_power_gtk_1mode(self):
        # достаем значение мощности для добавленного измерения из списка измерений
        power_value_Mvt_1mode = self.get_value_power(self.gtk_number_measurement_1mode,
                                                     self.decode_result_updata_list)
        # проверяем что полученное значение равно контрольному
        assert power_value_Mvt_1mode == correct_value_power_1mode,\
            "AssertionError: Power 1 mode wasn't calculated correctly"

    def verify_calculation_coefficient_efficiency_gtk_3mode(self):
        # достаем значение коофициента эфективности для добавленного измерения из списка измерений
        coefficient_efficiency_value_3mode = self.get_coefficient_efficiency(self.gtk_number_measurement_3mode,
                                                                             self.decode_result_updata_list)
        # проверяем что полученное значение равно контрольному
        assert coefficient_efficiency_value_3mode == correct_value_coefficient_efficiency_3mode,\
            "AssertionError:Coefficient_efficiency 3 mode wasn't calculated correctly"

    def verify_calculation_coefficient_efficiency_gtk_1mode(self):
        # достаем значение коофициента эфективности для добавленного измерения из списка измерений
        coefficient_efficiency_value_1mode = self.get_coefficient_efficiency(self.gtk_number_measurement_1mode,
                                                                             self.decode_result_updata_list)
        # проверяем что полученное значение равно контрольному
        assert coefficient_efficiency_value_1mode == correct_value_coefficient_efficiency_1mode,\
            "AssertionError: Coefficient_efficiency 1 mode wasn't calculated correctly"

    def verify_calculation_ktc_gtk_3mode(self):
        # достаем значение КТС для добавленного измерения из списка измерений
        ktc_value_3mode = self.get_ktc(self.gtk_number_measurement_3mode,
                                       self.decode_result_updata_list)
        # проверяем что полученное значение равно контрольному
        assert ktc_value_3mode == correct_value_ktc_3mode,\
            "AssertionError: Ktc 3 mode wasn't calculated correctly"

    def verify_calculation_ktc_gtk_1mode(self):
        # достаем значение КТС для добавленного измерения из списка измерений
        ktc_value_1mode = self.get_ktc(self.gtk_number_measurement_1mode,
                                       self.decode_result_updata_list)
        # проверяем что полученное значение равно контрольному
        assert ktc_value_1mode == correct_value_ktc_1mode,\
            "AssertionError: Ktc 3 mode wasn't calculated correctly"

    ############################ Удаление измерения ###############################

    def delete_measurement_3mode(self):
        # собираем данные для удаления измерения
        data_deleting_measurement = self.formation_delete_request(self.gtk_number_measurement_3mode)
        # выполняем запрос удаления измерения
        result_delete_measurement_gtk = session.post('%s' % URL_ORAWCI,
                                                     data_deleting_measurement)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_delete_measurement_gtk = self.decode_responce_to_text(result_delete_measurement_gtk)
        # получаем значения потверждющее удаления
        self.agree_deleted_number_3mode = self.get_key_deleting_measurement(decode_result_delete_measurement_gtk)

    def verify_deleting_measurement_3mode(self):
        print self.agree_deleted_number_3mode
        # проверяем что функция удаления возвращает 1, т.е. измерение было удалено
        assert self.agree_deleted_number_3mode == '1',\
            "AssertionError: Measurement wasn't deleted"


    def delete_measurement_1mode(self):
        # собираем данные для удаления измерения
        data_deleting_measurement = self.formation_delete_request(self.gtk_number_measurement_1mode)
        # выполняем запрос удаления измерения
        result_delete_measurement_gtk = session.post('%s' % URL_ORAWCI,
                                                     data_deleting_measurement)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_delete_measurement_gtk = self.decode_responce_to_text(result_delete_measurement_gtk)
        # получаем значения потверждющее удаления
        self.agree_deleted_number_1mode = self.get_key_deleting_measurement(decode_result_delete_measurement_gtk)

    def verify_deleting_measurement_1mode(self):
        print self.agree_deleted_number_1mode
        # проверяем что функция удаления возвращает 1, т.е. измерение было удалено
        assert self.agree_deleted_number_1mode == '1',\
            "AssertionError: Measurement wasn't deleted"
