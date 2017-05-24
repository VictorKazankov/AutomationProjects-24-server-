# -*- coding: utf-8 -*-

from UserAuthorization import session
from BaseFunc import BaseFunc
from config import DG_GPA_KEY, MODE_3, dg_correct_value_power_3mode, dg_correct_value_coefficient_efficiency_3mode, \
    dg_correct_value_ktc_3mode, URL_ORAWCI


class DgFunc(BaseFunc):
    def __init__(self):
        self.dg_number_measurement_3mode = ''
        self.dg_list_key_params_3mode = ''
        self.result_save_measurement_3mode = ''
        self.list_params_value = ''
        self.decode_result_updata_list = ''
        self.agree_deleted_number = ''

    ######################## Добавление пустого измерения #####################

    def adding_measurement_3mode(self):
        # собираем данные
        data_adding_3mode = self.formation_measuremenr_params(DG_GPA_KEY,
                                                              MODE_3)
        # выполняем запрос добавления нового измерения
        result_adding_measurement_dg = session.post('%s' % URL_ORAWCI,
                                                    data_adding_3mode)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_adding_measurement_dg = self.decode_responce_to_text(result_adding_measurement_dg)
        # вытаскиваем номер добавленного измерения из запроса
        self.dg_number_measurement_3mode = self.get_number_measurement(decode_result_adding_measurement_dg)

    def verify_adding_measurement_3mode(self):
        # проверяем что длина строки > 0, т.е. в ней номер добавленного измерения
        assert len(self.dg_number_measurement_3mode) > 0, "AssertionError: Measurement wasn't added"

    def get_list_key_params_measurement_3mode(self):
        # получаем ключи параметров для каждого из значений данных, они используются для заполнения данными измерения
        dg_list_params_key = self.formation_list_params_key(self.dg_number_measurement_3mode)
        result_get_list_params = session.get('%s' % URL_ORAWCI,
                                             params=dg_list_params_key)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_get_list_params = self.decode_responce_to_text(result_get_list_params)
        # вытаскиваем ключи для всех параметров и складываем их в список
        self.dg_list_key_params_3mode = self.get_key_value_measurement(decode_result_get_list_params)
        print len(self.dg_list_key_params_3mode)


    ######################## Добавление числовых значений в поля входных данных ########


    def save_measurement_3mode(self):
        # собираем данные для добавление данных в измерение
        data_save_measurement_3mode = self.formation_save_params_dg_3mode(self.dg_number_measurement_3mode,
                                                                          self.dg_list_key_params_3mode)
        # выполняем запрос сохранения нового измерения
        self.result_save_measurement_3mode = session.post('%s' % URL_ORAWCI,
                                                          data_save_measurement_3mode)
        # формируем данные что бы получить отображение расчетов
        data_for_calculation = self.formation_calculation_params(self.dg_number_measurement_3mode)
        self.list_params_value = session.get('%s' % URL_ORAWCI,
                                             params=data_for_calculation)

    def verify_edit_measurement_3mode(self):
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_save_measurement_3mode = self.decode_responce_to_text(
            self.result_save_measurement_3mode)
        # проверяем что сохранение измерения было успешным и нам возвратилась 1
        index_save_correct = self.get_value_save_correct(decode_result_save_measurement_3mode)
        assert index_save_correct == '1', "AssertionError: Measurement wasn't saved correctly"


    ########################## Проверка полей Мощность,КПД,КТУ ###################

    def updata_gpa_list(self):
        # получаем данные для обновления списка ГПА
        updata_list_params = self.formation_updata_list_params(DG_GPA_KEY)
        # выполняем запрос получения списка измерений в ГПА
        result_updata_list = session.get('%s' % URL_ORAWCI,
                                         params=updata_list_params)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        self.decode_result_updata_list = self.decode_responce_to_text(result_updata_list)
        print self.decode_result_updata_list

    def verify_calculation_power_dg_3mode(self):
        # достаем значение мощности для добавленного измерения из списка измерений
        power_value_Mvt_3mode = self.get_value_power(self.dg_number_measurement_3mode,
                                                     self.decode_result_updata_list)
        # проверяем что полученное значение равно контрольному
        assert power_value_Mvt_3mode == dg_correct_value_power_3mode,\
            "AssertionError: Power 3 mode wasn't calculated correctly"

    def verify_calculation_coefficient_efficiency_dg_3mode(self):
        # достаем значение коофициента эфективности для добавленного измерения из списка измерений
        coefficient_efficiency_value_3mode = self.get_coefficient_efficiency(self.dg_number_measurement_3mode,
                                                                             self.decode_result_updata_list)
        # проверяем что полученное значение равно контрольному
        assert coefficient_efficiency_value_3mode == dg_correct_value_coefficient_efficiency_3mode,\
            "AssertionError:Coefficient_efficiency 3 mode wasn't calculated correctly"

    def verify_calculation_ktc_dg_3mode(self):
        # достаем значение КТС для добавленного измерения из списка измерений
        ktc_value_3mode = self.get_ktc(self.dg_number_measurement_3mode,
                                       self.decode_result_updata_list)
        # проверяем что полученное значение равно контрольному
        assert ktc_value_3mode == dg_correct_value_ktc_3mode,\
            "AssertionError: Ktc 3 mode wasn't calculated correctly"


    ############################ Удаление измерения ###############################

    def delete_measurement_3mode(self):
        # собираем данные для удаления измерения
        data_deleting_measurement = self.formation_delete_request(self.dg_number_measurement_3mode)
        # выполняем запрос удаления измерения
        result_delete_measurement_dg = session.post('%s' % URL_ORAWCI,
                                                     data_deleting_measurement)
        # декодируем приходящий ответ в строку с помощью библиотеки lxml
        decode_result_delete_measurement_dg = self.decode_responce_to_text(result_delete_measurement_dg)
        # получаем значения потверждющее удаления
        self.agree_deleted_number_3mode = self.get_key_deleting_measurement(decode_result_delete_measurement_dg)

    def verify_deleting_measurement_3mode(self):
        # проверяем что функция удаления возвращает 1, т.е. измерение было удалено
        assert self.agree_deleted_number_3mode == '1',\
            "AssertionError: Measurement wasn't deleted"