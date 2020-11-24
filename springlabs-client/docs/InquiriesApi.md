# springlabs.InquiriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inquiry**](InquiriesApi.md#create_inquiry) | **POST** /api/v1/inquiries | Purchase an inquiry on a Subject (a property)


# **create_inquiry**
> InquiriesResponse create_inquiry(inquiries_request=inquiries_request)

Purchase an inquiry on a Subject (a property)

Input identifying information for a property to purchase an inquiry containing attestation groups reporting lien status data. For security, nothing is automatically saved, so be sure to save the response!

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import springlabs
from springlabs.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = springlabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration = springlabs.Configuration(
    host = "http://localhost",
    api_key = {
        'X-API-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with springlabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = springlabs.InquiriesApi(api_client)
    inquiries_request = springlabs.InquiriesRequest() # InquiriesRequest |  (optional)

    try:
        # Purchase an inquiry on a Subject (a property)
        api_response = api_instance.create_inquiry(inquiries_request=inquiries_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InquiriesApi->create_inquiry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inquiries_request** | [**InquiriesRequest**](InquiriesRequest.md)|  | [optional] 

### Return type

[**InquiriesResponse**](InquiriesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Inquiry created successfully |  -  |
**400** | Invalid input data error response. |  -  |
**401** | Unauthorized error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

