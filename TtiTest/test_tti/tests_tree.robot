*** Settings ***
#pybot -d test_tti/results test_tti/tests_tree.robot
Documentation  Verify count elements and opportunity adding measurement to objects of module tree

Library  modules/UserAuthorization.py
Library  modules/TreeFunc.py
Library  modules/config.py

Suite Setup  Session authorization
Suite Teardown  Close session

*** Keywords ***

Get count all objects in tree
    TreeFunc.get_count_element
Verify that count objects more 0
    TreeFunc.verify_count_elements_tree

Verify for GTK-10-4 objects
    TreeFunc.get_mode_gtk_object
    TreeFunc.verify_mode_number_gtk

Verify for PS-90 objects
    TreeFunc.get_mode_ps_object
    TreeFunc.verify_mode_number_ps

Verify for DG-90 objects
    TreeFunc.get_mode_dg_object
    TreeFunc.verify_mode_number_dg

Verify for other type(AVO object)
    TreeFunc.get_mode_avo_object
    TreeFunc.verify_mode_number_avo

*** Test Cases ***

Count elements in tree
    Get count all objects in tree
    Verify that count objects more 0

Return possible variants options for different TTI type
    Verify for GTK-10-4 objects
    Verify for PS-90 objects
    Verify for DG-90 objects
    Verify for other type(AVO object)



