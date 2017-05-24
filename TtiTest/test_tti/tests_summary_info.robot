*** Settings ***
#pybot -d test_tti/results test_tti/tests_summary_info.robot
Documentation  Verify count elements > 0 in summary information section

Library  modules/UserAuthorization.py
Library  modules/SummaryFunc.py
Library  modules/config.py

Suite Setup  Session authorization
Suite Teardown  Close session

*** Keywords ***

Get count all objects in table
    SummaryFunc.get_count_element_ks
Verify that count objects more 0
    SummaryFunc.verify_count_elements_list_ks

*** Test Cases ***

Count elements in summary table
    Get count all objects in table
    Verify that count objects more 0