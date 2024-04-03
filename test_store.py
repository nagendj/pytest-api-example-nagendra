from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
def test_patch_order_by_id():
    sample_order_data = {"id": "sample_order_32",
        "pet_id": 0}
    # Create a sample order
    response = api_helpers.post_api_data('/store/order', sample_order_data)
    assert response.status_code == 201  # Check if the order creation was successful

    # Get the order ID from the response
    order_id = response.json().get('id')

    # Update the order status to 'sold'
    update_data = {"status": "sold"}
    response = api_helpers.patch_api_data(f'/store/order/{order_id}', update_data)

    # Validate the response
    assert response.status_code == 200  # Check if the PATCH request was successful
    assert response.json().get("message") == "Order and pet status updated successfully"   
    
