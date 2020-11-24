# springlabs.RootApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_root**](RootApi.md#get_root) | **GET** / | Root endpoint for the service.
[**healthz**](RootApi.md#healthz) | **GET** /healthz | Health check endpoint


# **get_root**
> get_root()

Root endpoint for the service.

Endpoint for basic reachability check.

### Example

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


# Enter a context with an instance of the API client
with springlabs.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = springlabs.RootApi(api_client)
    
    try:
        # Root endpoint for the service.
        api_instance.get_root()
    except ApiException as e:
        print("Exception when calling RootApi->get_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server is reachable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **healthz**
> HealthResponse healthz()

Health check endpoint

Checks connectivity to Gateway Node and SmartyStreets API.

### Example

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


# Enter a context with an instance of the API client
with springlabs.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = springlabs.RootApi(api_client)
    
    try:
        # Health check endpoint
        api_response = api_instance.healthz()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RootApi->healthz: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server health is OK. |  -  |
**503** | Server is not ready to handle requests. See response body for more details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

