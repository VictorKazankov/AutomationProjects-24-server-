*** Settings ***
#pybot -d test_tti/results test_tti/tests_gtk_10_4.robot
Documentation  Add,edit and delete TTI of GTK-10-4 type. Verify calculation of power,coefficient_efficiency and KTS

Library  modules/UserAuthorization.py
Library  modules/GtkFunc.py
Library  modules/config.py

Suite Setup  Session authorization
Suite Teardown  Close session

*** Keywords ***

Adding new measurement 3 mode
    GtkFunc.adding_measurement_3mode
    GtkFunc.verify_adding_measurement_3mode
    GtkFunc.get_list_key_params_measurement_3mode

Save and edit measurement 3 mode
    GtkFunc.save_measurement_3mode
    GtkFunc.verify_edit_measurement_3mode

Verify new calculation result for 3 mode
    GtkFunc.updata_gpa_list
    GtkFunc.verify_calculation_power_gtk_3mode
    GtkFunc.verify_calculation_coefficient_efficiency_gtk_3mode
    GtkFunc.verify_calculation_ktc_gtk_3mode

Delete measurement 3 mode
    GtkFunc.delete_measurement_3mode
    GtkFunc.verify_deleting_measurement_3mode

#############

Adding new measurement 1 mode
    GtkFunc.adding_measurement_1mode
    GtkFunc.verify_adding_measurement_1mode
    GtkFunc.get_list_key_params_measurement_1mode

Save and edit measurement 1 mode
    GtkFunc.save_measurement_1mode
    GtkFunc.verify_edit_measurement_1mode

Verify new calculation result for 1 mode
    GtkFunc.updata_gpa_list
    GtkFunc.verify_calculation_power_gtk_1mode
    GtkFunc.verify_calculation_coefficient_efficiency_gtk_1mode
    GtkFunc.verify_calculation_ktc_gtk_1mode

Delete measurement 1 mode
    GtkFunc.delete_measurement_1mode
    GtkFunc.verify_deleting_measurement_1mode



*** Test Cases ***
Verify adding and deleting measurement of 1 and 3 mode
    Adding new measurement 3 mode
    Save and edit measurement 3 mode
    Verify new calculation result for 3 mode
    Adding new measurement 1 mode
    Save and edit measurement 1 mode
    Verify new calculation result for 1 mode
    Delete measurement 3 mode
    Delete measurement 1 mode
