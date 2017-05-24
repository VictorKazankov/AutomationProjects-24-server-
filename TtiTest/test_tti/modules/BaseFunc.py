# -*- coding: utf-8 -*-

from config import *
from ParsingXmlResponses import *

import requests
from requests_toolbelt import MultipartEncoder


class BaseFunc():
    def __init__(self):
        pass



    def formation_params_get_tree(self):
        tree_params = {'inType':2,
                       'subsystem':SUBSYSTEM_KEY,
                       'isCompress':0,
                       'inSQL':'gmt_mapd.tti_api.getFullTree'}
        return tree_params

    def decode_responce_to_text(self,responce_measurement):
        result_decode = ParsingXmlResponses.decode_body_text(responce_measurement)
        return result_decode

    def get_list_elements_tree(self,get_list_elements_tree):
        print 'test'
        count_elements = ParsingXmlResponses.assert_elements_count(get_list_elements_tree)
        return count_elements

    def get_param_mode(self,object_key):
        param = {'inType':2,
                 'subsystem':SUBSYSTEM_KEY,
                 'isCompress':0,
                 'inSQL':'gmt_mapd.tti_api.getTestMode(%s)'% object_key}
        return param

    def get_number_mode(self,xml_str):
        number = ParsingXmlResponses.get_number_mode(xml_str)
        return number



    def formation_measuremenr_params(self, key, mode):
        # формируем данные добавляемого запроса
        data_request = ",".join([key,
                                 USER,
                                 DATA,
                                 TYPETESTOPEREXPLOR,
                                 mode])
        # формируем параметры добавляемого запроса
        params_request = {'isCheckXsd': 1,
                          'inType': 2,
                          'subsystem': SUBSYSTEM_KEY,
                          'isCompress': 0,
                          'inSQL': 'gmt_mapd.tti_api.createTest({0})'.format(data_request)}
        return params_request

    def decode_responce_to_text(self, result):
        result_decode = ParsingXmlResponses.decode_body_text(result)
        return result_decode

    def get_number_measurement(self,decode_result_adding_measurement):
        number_measurement = ParsingXmlResponses.get_number_measurement_or_save_delete_flags(
            decode_result_adding_measurement)
        return number_measurement

    def formation_list_params_key(self, key):
        data_request = ",".join([key,
                                 DATA])
        params_request = {'isCheckXsd': 1,
                          'inType': 2,
                          'subsystem': SUBSYSTEM_KEY,
                          'isCompress': 0,
                          'inSQL': 'gmt_mapd.tti_api.refreshParamValues({0})'.format(data_request)}
        return params_request

    def get_key_value_measurement(self, decode_result_get_list_params):
        string_keys = ParsingXmlResponses.get_params_key_number(decode_result_get_list_params)
        # с помощью регулярных выражений разделяем целую строку на элементы-ключи
        list_keys = string_keys.split()
        return list_keys

    def formation_save_params_gtk_3mode(self, number_measurement, dtk_list_key_params):
        # собираем данные результатов обследования, поочередно доставая из списка ключ для каждого параметра и
        # связывая его со значением атрибута в переменой
        data_third_mode = "|".join(["'" + dtk_list_key_params[0] + barometric_pressure_3mode,
                                    dtk_list_key_params[1] + outdoor_temperature_3mode,
                                    dtk_list_key_params[2] + temperature_before_ok_3mode,
                                    dtk_list_key_params[3] + tvd_rotor_rotation_frequency_3mode,
                                    dtk_list_key_params[4] + st_rotor_rotation_frequency_3mode,
                                    dtk_list_key_params[5] + vacuum_air_before_ok_3mode,
                                    dtk_list_key_params[6] + excessive_air_pressure_ok_3mode,
                                    dtk_list_key_params[7] + excessive_pressure_ps_for_st_3mode,
                                    dtk_list_key_params[8] + temperature_ps_the_st_3mode,
                                    dtk_list_key_params[9] + consumption_gas_3mode + "'"])
        # формируем данные добавляемого запроса
        data_request = ",".join([number_measurement,
                                 USER,
                                 DATA,
                                 TYPETESTOPEREXPLOR,
                                 data_third_mode])
        # собираем это все вместе с параметрами самого запроса
        param_request = {'inType': 2,
                         'subsystem': SUBSYSTEM_KEY,
                         'isCompress': 0,
                         'inSQL': 'gmt_mapd.tti_api.editTest({0})'.format(data_request)}
        return param_request

    def formation_save_params_gtk_1mode(self, gtk_number_measurement, dtk_list_key_params):
        # собираем данные результатов обследования, поочередно доставая из списка ключ для каждого параметра и
        # связывая его со значением атрибута в переменой
        data_first_mode = "|".join(["'" + dtk_list_key_params[0] + barometric_pressure_1mode,
                                    dtk_list_key_params[1] + outdoor_temperature_1mode,
                                    dtk_list_key_params[2] + temperature_before_ok_1mode,
                                    dtk_list_key_params[3] + tvd_rotor_rotation_frequency_1mode,
                                    dtk_list_key_params[4] + st_rotor_rotation_frequency_1mode,
                                    dtk_list_key_params[5] + vacuum_air_before_ok_1mode,
                                    dtk_list_key_params[6] + excessive_air_pressure_ok_1mode,
                                    dtk_list_key_params[7] + excessive_pressure_ps_for_st_1mode,
                                    dtk_list_key_params[8] + temperature_ps_the_st_1mode,
                                    dtk_list_key_params[9] + consumption_gas_1mode + "'"])
        # формируем данные добавляемого запроса
        data_request = ",".join([gtk_number_measurement,
                                 USER,
                                 DATA,
                                 TYPETESTOPEREXPLOR,
                                 data_first_mode])
        # собираем это все вместе с параметрами самого запроса
        param_request = {'inType': 2,
                         'subsystem': SUBSYSTEM_KEY,
                         'isCompress': 0,
                         'inSQL': 'gmt_mapd.tti_api.editTest({0})'.format(data_request)}
        return param_request

    def formation_save_params_ps_3mode(self, ps_number_measurement, ps_list_key_params):
        # собираем данные результатов обследования, поочередно доставая из списка ключ для каждого параметра и
        # связывая его со значением атрибута в переменой
        data_3mode = "|".join(["'" + ps_list_key_params[0] + ps_atmospheric_air_pressure,
                               ps_list_key_params[1] + ps_outdoor_temperature,
                               ps_list_key_params[2] + ps_temperature_before_ok,
                               ps_list_key_params[3] + ps_relative_humidity,
                               ps_list_key_params[4] + ps_vacuum_total_air_pressure_before_ok,
                               ps_list_key_params[5] + ps_vacuum_static_air_pressure_before_ok,
                               ps_list_key_params[6] + ps_excessive_total_pressure_combustion_products_st,
                               ps_list_key_params[7] + ps_speed_rotor_gas_generator,
                               ps_list_key_params[8] + ps_st_rotor_rotation_frequency,
                               ps_list_key_params[9] + ps_temperature_combustion_products_gg,
                               ps_list_key_params[10] + ps_temperature_combustion_products_st,
                               ps_list_key_params[11] + ps_consumption_gas + "'"])
        # формируем данные добавляемого запроса
        data_request = ",".join([ps_number_measurement,
                                 USER,
                                 DATA,
                                 TYPEBEFOREREPAIR,
                                 data_3mode])
        # собираем это все вместе с параметрами самого запроса
        param_request = {'inType': 2,
                         'subsystem': SUBSYSTEM_KEY,
                         'isCompress': 0,
                         'inSQL': 'gmt_mapd.tti_api.editTest({0})'.format(data_request)}
        return param_request

    def formation_save_params_dg_3mode(self, dg_number_measurement, dg_list_key_params):
        # собираем данные результатов обследования, поочередно доставая из списка ключ для каждого параметра и
        # связывая его со значением атрибута в переменой
        data_3mode = "|".join(["'" + dg_list_key_params[0] + atmospheric_air_pressure,
                               dg_list_key_params[1] + outdoor_temperature,
                               dg_list_key_params[2] + temperature_before_ok,
                               dg_list_key_params[3] + excessive_air_pressure_entry_cbn,
                               dg_list_key_params[4] + excessive_air_pressure_exit_cbn,
                               dg_list_key_params[5] + temperature_gas_entry_cbn,
                               dg_list_key_params[6] + temperature_gas_exit_cbn,
                               dg_list_key_params[7] + differential_pressure_confusor_cbn,
                               dg_list_key_params[8] + tvd_rotor_rotation_frequency,
                               dg_list_key_params[9] + st_rotor_rotation_frequency,
                               dg_list_key_params[10] + temperature_ps_tnd,
                               dg_list_key_params[11] + consumption_gas + "'"])
        # формируем данные добавляемого запроса
        data_request = ",".join([dg_number_measurement,
                                 USER,
                                 DATA,
                                 TYPEAFTERREPAIR,
                                 data_3mode])
        # собираем это все вместе с параметрами самого запроса
        param_request = {'inType': 2,
                         'subsystem': SUBSYSTEM_KEY,
                         'isCompress': 0,
                         'inSQL': 'gmt_mapd.tti_api.editTest({0})'.format(data_request)}
        return param_request

    def formation_calculation_params(self, gtk_number_measurement):
        data_calculation = ",".join([gtk_number_measurement,
                                     DATA])
        params_calculation = {'inType': 2,
                              'subsystem': SUBSYSTEM_KEY,
                              'isCompress': 0,
                              'inSQL': 'gmt_mapd.tti_api.refreshParamValues({0})'.format(data_calculation)}
        return params_calculation

    def formation_updata_list_params(self, type):
        params_list = {'inType': 2,
                       'subsystem': SUBSYSTEM_KEY,
                       'isCompress': 0,
                       'inSQL': 'gmt_mapd.tti_api.getTestList(%s)' % type}
        return params_list

    def get_value_save_correct(self, decode_result_save_measurement_third_mode):
        saved_value = ParsingXmlResponses.get_number_measurement_or_save_delete_flags(
            decode_result_save_measurement_third_mode)
        return saved_value

    def get_value_power(self, number_measurement, decode_result_updata_list):
        list_keys_values = self.get_list_key_measurement(decode_result_updata_list)
        # достаем из списка измерений все значения мощностей и формируем их список
        list_power_values = (ParsingXmlResponses.get_power(decode_result_updata_list)).split(',')
        # соединяем ключ + значение мощности в словарь и находим нужную мощность по ключу последнего созданного измерения
        key_power_dict = dict(zip(list_keys_values,
                                  list_power_values))
        value_power_Kvt = key_power_dict.get(str(number_measurement))
        # переводим это значение из Квт в Мвт
        value_pover_Mvt = float(value_power_Kvt) / 1000
        return value_pover_Mvt

    def get_coefficient_efficiency(self, number_measurement, decode_result_updata_list):
        # достаем из списка измерений все ключи для каждого измерения и формируем список этих ключей
        list_keys_values = self.get_list_key_measurement(decode_result_updata_list)
        # достаем из списка измерений все значения коофициентов эффективности и формируем их список
        coefficient_efficiency_values = (ParsingXmlResponses.get_coefficient_efficiency(
            decode_result_updata_list)).split(',')
        # соединяем ключ + значение мощности в словарь и находим нужную мощность по ключу последнего созданного измерения
        key_coefficient_efficiency_dict = dict(zip(list_keys_values,
                                                   coefficient_efficiency_values))
        value_coefficient_efficiency = key_coefficient_efficiency_dict.pop(number_measurement)
        # округляем полученное значение до одной цифре после запятой
        value_coefficient_efficiency = round(float(value_coefficient_efficiency), 1)
        return value_coefficient_efficiency

    def get_ktc(self, number_measurement, decode_result_updata_list):
        list_keys_values = self.get_list_key_measurement(decode_result_updata_list)
        # достаем из списка измерений все значения КТС и формируем их список
        list_ktc_value = (ParsingXmlResponses.get_ktc_values(decode_result_updata_list)).split(',')
        # соединяем ключ + значение мощности в словарь и находим нужную мощность по ключу последнего созданного измерения
        key_ktc_dict = dict(zip(list_keys_values,
                                list_ktc_value))
        value_last_ktc = key_ktc_dict.pop(number_measurement)
        # округляем полученное значение до двух знаков после запятой
        value_ktc = round(float(value_last_ktc), 2)
        return value_ktc

    def formation_delete_request(self, gtk_number_measurement):
        # формируем данные запроса удаления
        params_request = {'isCheckXsd': 1,
                          'inType': 2,
                          'subsystem': SUBSYSTEM_KEY,
                          'isCompress': 0,
                          'inSQL': 'gmt_mapd.tti_api.dropTest({0})'.format(gtk_number_measurement)}
        return params_request

    def get_key_deleting_measurement(self, decode_result_delete_measurement_gtk):
        number_delete = ParsingXmlResponses.get_number_measurement_or_save_delete_flags(
            decode_result_delete_measurement_gtk)
        return number_delete

    ########### Media ###########

    def formation_schema_params(self, key):
        # формируем данные добавляемого запроса
        data_request = ",".join([key,
                                 DATA,
                                 'null'])
        # формируем параметры добавляемого запроса
        params_request = {'isCheckXsd': 1,
                          'inType': 2,
                          'subsystem': SUBSYSTEM_KEY,
                          'isCompress': 0,
                          'inSQL': 'gmt_mapd.tti_api.modifySchema({0})'.format(data_request)}
        return params_request

    def get_number_schema(self, decode_result_adding_schema):
        number_schema = ParsingXmlResponses.get_number_measurement_or_save_delete_flags(decode_result_adding_schema)
        print type(number_schema)
        return number_schema

    def formation_media_params(self, number_schema):
        data = {
                        'subsystem': SUBSYSTEM_KEY,
                        'file': (open('test_tti/resources/images.png', 'rb'),'image/png'),
                        'description': 'Тестовый файл',
                        'parentObjectKey': '%s' % number_schema,
                        'fileName': 'images.png',
                        'Upload': 'Submit Query',
                        'uniqueRandom': '61610209',
                        'fileType': '3',
                        'previewWidth': '135',
                        'previewHeight': '104'
        }
        encoder = MultipartEncoder(data, boundary='skvxymfggiwhcdmtqwxgkanffrnvimsp')
        return encoder

    def formation_params_list_schems(self, GTK_GPA_KEY):
        data_request = ",".join([GTK_GPA_KEY,
                                 'null'])
        # формируем параметры запроса
        params_request = {'isCheckXsd': 1,
                          'inType': 2,
                          'subsystem': SUBSYSTEM_KEY,
                          'isCompress': 0,
                          'inSQL': 'gmt_mapd.tti_api.getSchemaDetails({0})'.format(data_request)}
        return params_request

    def get_value_keys_schemas(self,decode_result_get_list_schema):
        list_keys_schemas = ParsingXmlResponses.get_list_keys_schemas(decode_result_get_list_schema)
        return list_keys_schemas

    def get_params_delete(self,key_schema):
        params_request = {'isCheckXsd': 1,
                          'inType': 2,
                          'subsystem': SUBSYSTEM_KEY,
                          'isCompress': 0,
                          'inSQL': 'gmt_mapd.tti_api.deleteSchema({0})'.format(key_schema)}
        return params_request

    def get_key_deleting_schema(self,decode_result_deleting_schema):
        key_delete = ParsingXmlResponses.get_number_measurement_or_save_delete_flags(
            decode_result_deleting_schema)
        return key_delete


    ########### Summary information ###########

    def formation_params_get_list(self):
        tree_params = {'inType':2,
                       'subsystem':SUBSYSTEM_KEY,
                       'isCompress':0,
                       'inSQL':'gmt_mapd.tti_api.getTotalInfoLevel1'}
        return tree_params

    def get_list_ks(self,get_list_elements):
        count_elements = ParsingXmlResponses.assert_elements_count_summer_table(get_list_elements)
        return count_elements

    ################################################################

    def get_list_key_measurement(self, decode_result_updata_list):
        key_values = ParsingXmlResponses.get_key_param_measurement(decode_result_updata_list)
        list_keys_values = key_values.split(',')


        return list_keys_values
