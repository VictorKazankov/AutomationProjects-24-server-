*** Settings ***
#pybot -d test_tti/results test_tti/tests_media.robot
Documentation  Add,edit and delete media

Library  modules/UserAuthorization.py
Library  modules/MediaFunc.py
Library  modules/config.py

Suite Setup  Session authorization
Suite Teardown  Close session

*** Keywords ***
Add media to table
     MediaFunc.create_schema
     MediaFunc.add_media
     MediaFunc.verify_schema_added

Delete media from table
    MediaFunc.delete_schema
    MediaFunc.verify_schema_deleted


*** Test Cases ***
Add and delete media in table
    Add media to table
    Delete media from table
