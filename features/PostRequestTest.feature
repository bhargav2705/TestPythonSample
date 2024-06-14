Feature: To test sample  for post methods

  Scenario: Verify the post method for sample API
    Given the payload details for the request
    When we execute the Post method
    Then verify the new resource is created a
    And  status code of response should be 200

