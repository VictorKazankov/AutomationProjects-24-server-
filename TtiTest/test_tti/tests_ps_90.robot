*** Settings ***
#pybot -d test_tti/results test_tti/tests_ps_90.robot
Documentation  Add,edit and delete TTI of PS-90 type. Verify calculation of power,coefficient_efficiency and KTS

Library  modules/UserAuthorization.py
Library  modules/PsFunc.py
Library  modules/config.py

Suite Setup  Session authorization
Suite Teardown  Close session

*** Keywords ***

Adding new measurement 3 mode
    PsFunc.adding_measurement_3mode
    PsFunc.verify_adding_measurement_3mode
    PsFunc.get_list_key_params_measurement_3mode

Save and edit measurement 3 mode
    PsFunc.save_measurement_3mode
    PsFunc.verify_edit_measurement_3mode

Verify new calculation result for 3 mode
    PsFunc.updata_gpa_list
    PsFunc.verify_calculation_power_ps_3mode
    PsFunc.verify_calculation_coefficient_efficiency_ps_3mode
    PsFunc.verify_calculation_ktc_ps_3mode

Delete measurement 3 mode
    PsFunc.delete_measurement_3mode
    PsFunc.verify_deleting_measurement_3mode

*** Test Cases ***

Verify adding and deleting measurement of 3 mode
    Adding new measurement 3 mode
    Save and edit measurement 3 mode
    Verify new calculation result for 3 mode
    Delete measurement 3 mode