# coding=utf-8
from lxml import etree


# class for work with responces by lxml library

class ParsingXmlResponses():

    def __init__(self):
        pass
# метод для декодирования responds в UTF-8
    @staticmethod
    def decode_body_text(result):
        body_text = result.content.decode("utf-8")
        return body_text


    # метод получения количества элементов в дереве
    @staticmethod
    def assert_elements_count(body_text_tree):
        xml_root = etree.XML(body_text_tree)
        find_text = etree.XPath("//CNAME/text()")
        values = find_text(xml_root)
        return len(values)

    # метод получения номера режима ГПА
    @staticmethod
    def get_number_mode(body_text):
        xml_root = etree.XML(body_text)
        find_text = etree.XPath("//NTTI_MODE/text()")
        values_arr = find_text(xml_root)
        values_num = ' '.join(values_arr)
        return values_num

    # метод получения как номера созданного измерения так и флагов сохранения и удаления измерения
    @staticmethod
    def get_number_measurement_or_save_delete_flags(body_text):
        xml_root = etree.XML(body_text)
        find_text = etree.XPath("//res/text()")
        values_arr = find_text(xml_root)
        values_num = ' '.join(values_arr)
        return values_num

    # метод для получения параметров-ключей для заполнения данных в измерении
    @staticmethod
    def get_params_key_number(body_text):
        xml_root = etree.XML(body_text)
        find_text = etree.XPath("//NVALUEKEY/text()")
        values_arr = find_text(xml_root)
        values_num = ' '.join(values_arr)
        return values_num

    # метод получения значения поля Мощность в измерении
    @staticmethod
    def get_power(body_text):
        xml_root = etree.XML(body_text)
        find_text_power = etree.XPath("//NPOWER/text()")
        value_arr_power = find_text_power(xml_root)
        list_power = ','.join(value_arr_power)
        return list_power


    @staticmethod
    def get_key_param_measurement(body_text):
        xml_root = etree.XML(body_text)
        find_text = etree.XPath("//NTESTKEY/text()")
        values_arr = find_text(xml_root)
        values_num = ','.join(values_arr)
        return values_num

    # метод получения значения поля КПД в измерении
    @staticmethod
    def get_coefficient_efficiency(body_text):
        xml_root = etree.XML(body_text)
        find_text_coof = etree.XPath("//NEFFICIENCY/text()")
        value_arr_coof = find_text_coof(xml_root)
        list_coof = ','.join(value_arr_coof)
        return list_coof

    # метод получения значения поля КТС в измерении
    @staticmethod
    def get_ktc_values(body_text):
        xml_root = etree.XML(body_text)
        find_text_ktc = etree.XPath("//NKTS/text()")
        value_arr_ktc = find_text_ktc(xml_root)
        list_ktc = ','.join(value_arr_ktc)
        return list_ktc

    # метод получения ключей добавленных схем
    @staticmethod
    def get_list_keys_schemas(body_text):
        xml_root = etree.XML(body_text)
        find_text_keys = etree.XPath("//NSCHEMAKEY/text()")
        value_arr_keys = find_text_keys(xml_root)
        list_keys = ','.join(value_arr_keys)
        return list_keys

    # метод получения количества элементов в сводной таблице
    @staticmethod
    def assert_elements_count_summer_table(body_text_tree):
        xml_root = etree.XML(body_text_tree)
        find_text = etree.XPath("//CNAMEKS/text()")
        values = find_text(xml_root)
        return len(values)