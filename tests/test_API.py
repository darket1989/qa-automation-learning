import pytest
from playwright.sync_api import *

#Create a reusable API client with a default base URL
@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )
    # Execution pauses here during the test, once the test finishes, control returns and the lines after yield will run
    yield api_context
    api_context.dispose()


def test_users_search(api_context: APIRequestContext):
    # Target name to search on the response
    query = "Emily"
    #Perform GEt operation using the base url
    response = api_context.get(f"/users/search?q={query}")

    # Parse response JSON into a python dict
    users_data = response.json()

    # Log how many users were found
    print("Users found:", users_data["total"])

    # Validate each returned user matches the target user name
    for user in users_data["users"]:
        print("Checking user:", user["firstName"])

    # E-nsure the first name contains the search query
        assert query in user["firstName"]

def test_create_user(api_context: APIRequestContext):
    response = api_context.post(
        "users/add",
         headers = {"Content-Type" : "application/json"},
         data = {"firstName": "Damien", "lastName": "Smith", "age": 27}
    )

    user_data = response.json()
    assert user_data["id"] == 209
    assert user_data["firstName"] == "Damien"
    print(f"\n {user_data}")

def test_count_users(api_context: APIRequestContext):
    response = api_context.get("/users")
    user_data = response.json()

    print(f"\n Total users : {user_data["total"]}")