# -*- coding: utf-8 -*-

URL_TTI = 'http://192.168.17.81'

URL_GIS_MT_AUTH = URL_TTI + '/fl/auth'
URL_ORAWCI = URL_TTI + '/orawci/v6/getxmlbysql'
URL_MEDIA = URL_TTI + '/MediaFileManager/mediafile/'

SUBSYSTEM_KEY = '1158968669994'

GTK_GPA_KEY = '10509456629959'  # КС Самсоновская - КЦ-2 - ГПА-28
PS_GPA_KEY = '10509456999959'   # КС Пуртазовская - КЦ-1 - ГПА-16
DG_GPA_KEY = '10509457629959'   # КС Демьяновская - КЦ-1 - ГПА-16
AVO_KEY = '10511120139959'  # КС Ново-Уренгойская - КЦ-1 - АВО-1


################ Test Type ##############

TYPETESTOPEREXPLOR = '70074238359947'
TYPEBEFOREREPAIR = '70074237849947'
TYPEAFTERREPAIR = '70074237989947'


############### Test Mode ###############

MODE_1 = '1'
MODE_3 = '3'

DATA = '978314400'  # data create measurement - 01.01.2001
USER = "'auto_test'"  # author


############### Input data - GTK-10-4 type ###############

barometric_pressure_3mode = '=740;740;740'  # Барометрическое давление
outdoor_temperature_3mode = '=-21.6;-21.6;-21.6'  # Температура наружнего воздуха
temperature_before_ok_3mode = '=-19.5;-19.5;-19.5'  # Температура перед ОК
tvd_rotor_rotation_frequency_3mode = '=5034;4945;4852'  # Частота вращения ротора ТВД
st_rotor_rotation_frequency_3mode = '=4500;4400;4300'  # Частота вращения ротора СТ
vacuum_air_before_ok_3mode = '=115;110;105'  # Разрежение воздуха перед ОК
excessive_air_pressure_ok_3mode = '=3.432;3.312;3.192'  # Избыточное давление воздуха за ОК
excessive_pressure_ps_for_st_3mode = '=310;290;270'  # Избыточное давление ПС за СТ
temperature_ps_the_st_3mode = '=464;449;436'  # Температура продуктов сгорания за СТ
consumption_gas_3mode = '=3887;3668;3454'  # Расход топливного газа (ТГ)

barometric_pressure_1mode = '=735;;'
outdoor_temperature_1mode = '=-19.6;;'
temperature_before_ok_1mode = '=-20.5;;'
tvd_rotor_rotation_frequency_1mode = '=5025;;'
st_rotor_rotation_frequency_1mode = '=4450;;'
vacuum_air_before_ok_1mode = '=117;;'
excessive_air_pressure_ok_1mode = '=3.532;;'
excessive_pressure_ps_for_st_1mode = '=305;;'
temperature_ps_the_st_1mode = '=460;;'
consumption_gas_1mode = '=3887;;'


# Correct values for verify calculation
correct_value_power_3mode = 9.19
correct_value_coefficient_efficiency_3mode = 27.4
correct_value_ktc_3mode = 0.92

correct_value_power_1mode = 9.703
correct_value_coefficient_efficiency_1mode = 28.8
correct_value_ktc_1mode = 0.97


############### Input data - PS-90 type ###############

ps_atmospheric_air_pressure = '=100.3;100.3;100.3'  # Атмосферное давление воздуха
ps_outdoor_temperature = '=7.8;8.7;8.2'  # Температура атмосферного воздуха
ps_temperature_before_ok = '=7.8;8.7;8.2'  # Температура перед ОК
ps_relative_humidity = '=29;31;30'  # Относительная влажность
ps_vacuum_total_air_pressure_before_ok = '=0.68;0.44;0.85'  # Разрежение полного давления воздуха перед ОК
ps_vacuum_static_air_pressure_before_ok = '=7.63;8.48;9.64'  # Разрежение статического давления воздуха перед ОК
ps_excessive_total_pressure_combustion_products_st = '=3.51;4.32;5.39'  # Избыточное полное давление продуктов сгорания за СТ
ps_speed_rotor_gas_generator = '=10300;10526;10627'  # Частота вращения ротора газогенератора
ps_st_rotor_rotation_frequency = '=4800;5000;5188'  # Частота вращения ротора СТ
ps_temperature_combustion_products_gg = '=655;706;750'  # Температура продуктов сгорания за ГГ
ps_temperature_combustion_products_st = '=441;459;479'  # Температура продуктов сгорания за СТ
ps_consumption_gas = '=3601;4077;4561'  # Расход топливного газа (ТГ)


# Correct values for verify calculation
ps_correct_value_power_3mode = 12.824
ps_correct_value_coefficient_efficiency_3mode = 28.7
ps_correct_value_ktc_3mode = 0.80




############### Input data - DG-90 type ###############

atmospheric_air_pressure = '=101.3;101.3;101.3'  # Атмосферное давление воздуха
outdoor_temperature = '=8.1;8.2;8.3'  # Температура атмосферного воздуха
temperature_before_ok = '=10.1;10.2;10.5'  # Температура перед ОК
excessive_air_pressure_entry_cbn = '=4.488;4.495;4.504'  # Избыточное давление газа на входе ЦБН
excessive_air_pressure_exit_cbn = '=6.247;6.249;6.242'  # Избыточное давление газа на выходе ЦБН
temperature_gas_entry_cbn = '=8.50;8.60;8.30'  # Температура газа на входе ЦБН
temperature_gas_exit_cbn = '=37.30;37.20;36.70'  # Температура газа на выходе ЦБН
differential_pressure_confusor_cbn = '=15.74;14.27;12.73'
tvd_rotor_rotation_frequency = '=8566;8533;8464'  # Частота вращения ротора ТВД
st_rotor_rotation_frequency = '=4750;4650;4550'  # Частота вращения ротора СТ
temperature_ps_tnd = '=560;551;539'  # Температура ПС за ТНД
consumption_gas = '=3728;3631;3445'  # Расход топливного газа


# Correct values for verify calculation
dg_correct_value_power_3mode = 14.810
dg_correct_value_coefficient_efficiency_3mode = 35.9
dg_correct_value_ktc_3mode = 0.93