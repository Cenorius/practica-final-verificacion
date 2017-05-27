Feature: Input validation

Scenario Outline: Verify normal input
    Given I fill the input text "<text>"
    When I click the Execute button
    Then I can see the list of words "<list>" with their number of appearances: "<count>"
    and The input field is empty

Examples:
  | text                | list         | count
  | bob bob y alice     | bob,alice   | 2,1
  | bob y alice         | bob,alice   | 1,1
  | bob y alice alice   | alice,bob   | 2,1
  | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA | 1


Scenario Outline: Verify input too large
    Given I fill the input text "<text>"
    When I click the Execute button
    Then An error message appears

Examples:
  | text            |
  | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA |


Scenario: Verify no input
    Given I fill the input text ""
    When I click the Execute button
    Then Nothing happens