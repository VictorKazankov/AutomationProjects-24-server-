*** Settings ***
#pybot -d test_tti/results test_tti/tests_dg_90.robot
Documentation  Add,edit and delete TTI of DG-90 type. Verify calculation of power,coefficient_efficiency and KTS

Library  modules/UserAuthorization.py
Library  modules/DgFunc.py
Library  modules/config.py

Suite Setup  Session authorization
Suite Teardown  Close session

*** Keywords ***

Adding new measurement 3 mode
    DgFunc.adding_measurement_3mode
    DgFunc.verify_adding_measurement_3mode
    DgFunc.get_list_key_params_measurement_3mode

Save and edit measurement 3 mode
    DgFunc.save_measurement_3mode
    DgFunc.verify_edit_measurement_3mode

Verify new calculation result for 3 mode
    DgFunc.updata_gpa_list
    DgFunc.verify_calculation_power_dg_3mode
    DgFunc.verify_calculation_coefficient_efficiency_dg_3mode
    DgFunc.verify_calculation_ktc_dg_3mode

Delete measurement 3 mode
    DgFunc.delete_measurement_3mode
    DgFunc.verify_deleting_measurement_3mode

*** Test Cases ***

Verify adding and deleting measurement of 3 mode
    Adding new measurement 3 mode
    Save and edit measurement 3 mode
    Verify new calculation result for 3 mode
    Delete measurement 3 mode