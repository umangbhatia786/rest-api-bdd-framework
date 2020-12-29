#Created by Umang Bhatia

Feature: Verify that a location can be added using Google Maps API
  @regression
  Scenario Outline: Verify Add Location API Functionality
    Given The Location Details with <lat>, <lng>, <name>, <contact> and address as <address>
    When We execute the AddLocation API method
    Then Response Status Code is 200
    Then Status Message is Ok
    Examples:
      | lat        | lng       | name            | contact          | address                 |
      | -51.383494 | 39.427362 | The Locha Shop | (+91) 9268886942 | 19, Ridge Street, Mayne |

  @regression
  Scenario: Verify Get Location API Functionality
    Given The Place Id of the desired location
    When We execute the Get Location API method
    Then Response Status Code is 200
    And The Response Body has correct details for the given location

  @regression @end
  Scenario Outline: Verify Update Location API Functionality
    Given The Place Id of the location along with New Address as <new_address>
    When We execute the Update Location API method
    Then Response Status Code is 200
    Examples:
      | new_address           |
      |20, Jump Street, Oregon|
