Feature: Date validation

Scenario Outline: Verify date parsing
    Given I fill the input date with "<date>"
    And Select "<option>"
    When I click the Execute button
    Then An error message appears "<error>"

Examples:
  | date        | option    | error
  | 01/01/3001  | muw       | No future dates allowed
  | 01/01/3001  | wpa       | No future dates allowed
  | 32/01/2001  | muw       | Invalid date
  | 32/01/2001  | wpa       | Invalid date
  | 01/13/2001  | muw       | Invalid date
  | 01/13/2001  | wpa       | Invalid date

Scenario: Verify no input or option
    Given I fill the input date with "<date>"
    When I click the Execute button
    Then An error message appears "<error>"

Examples:
   | date       | error
   |            | You need to input a date
   | 02/02/2012 | You need to select an option
