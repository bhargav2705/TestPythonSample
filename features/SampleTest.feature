Feature: To test sample feature

  Scenario: Verify the simple feature test in python
    Given I have the endpoint for the get pets
    When I hit the endpoint
    Then I validate the status code as 200

