Feature: Reset validation

Scenario Outline: Reset button when there is text
    Given I fill the input text "<text>"
    When I click the Reset button
    Then The input field is empty

Examples:
  | text            |
  | bob y alice     |
  | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA |
  | |
  | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA |
  | 213213187)(&)(& ) 9 7 |

Scenario: Reset button when there is no text
    Given I fill the input text ""
    When I click the Reset button
    Then Nothing happens