# springlabs.AttestationGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attestation_group_by_id**](AttestationGroupsApi.md#get_attestation_group_by_id) | **GET** /api/v1/attestationGroups/{id} | Get information about a previously created attestation group by ID
[**revoke_attestation_group_by_id**](AttestationGroupsApi.md#revoke_attestation_group_by_id) | **PUT** /api/v1/attestationGroups/{id}/revoke | Revoke an existing attestation group
[**upsert_attestation_group_by_id**](AttestationGroupsApi.md#upsert_attestation_group_by_id) | **PUT** /api/v1/attestationGroups/{id} | Update or create an attestation group
[**upsert_attestation_groups**](AttestationGroupsApi.md#upsert_attestation_groups) | **PUT** /api/v1/attestationGroups | Update or create registry attestation groups in bulk


# **get_attestation_group_by_id**
> AttestationGroupRecord get_attestation_group_by_id(id)

Get information about a previously created attestation group by ID

Information is retrieved from the Gateway Node database.

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
    api_instance = springlabs.AttestationGroupsApi(api_client)
    id = 'id_example' # str | Participant-provided unique ID of the attestation group to update, create, or get.

    try:
        # Get information about a previously created attestation group by ID
        api_response = api_instance.get_attestation_group_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttestationGroupsApi->get_attestation_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Participant-provided unique ID of the attestation group to update, create, or get. | 

### Return type

[**AttestationGroupRecord**](AttestationGroupRecord.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attestation group info successfully fetched. |  -  |
**400** | Invalid input data error response. |  -  |
**401** | Unauthorized error response. |  -  |
**404** | Not found error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_attestation_group_by_id**
> revoke_attestation_group_by_id(id, attestation_groups_revoke_request=attestation_groups_revoke_request)

Revoke an existing attestation group

This endpoint allows Participants to revoke an attestation group. Does nothing if the attestation group is already revoked.

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
    api_instance = springlabs.AttestationGroupsApi(api_client)
    id = 'id_example' # str | ID of the attestation group to revoke.
attestation_groups_revoke_request = springlabs.AttestationGroupsRevokeRequest() # AttestationGroupsRevokeRequest |  (optional)

    try:
        # Revoke an existing attestation group
        api_instance.revoke_attestation_group_by_id(id, attestation_groups_revoke_request=attestation_groups_revoke_request)
    except ApiException as e:
        print("Exception when calling AttestationGroupsApi->revoke_attestation_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the attestation group to revoke. | 
 **attestation_groups_revoke_request** | [**AttestationGroupsRevokeRequest**](AttestationGroupsRevokeRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All attestations in the attestation group were successfully revoked. |  -  |
**400** | Invalid input data error response. |  -  |
**401** | Unauthorized error response. |  -  |
**404** | Not found error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_attestation_group_by_id**
> AttestationGroupDigest upsert_attestation_group_by_id(id, attestation_group_input=attestation_group_input)

Update or create an attestation group

This endpoint allows Participants to update/create an attestation group for publication to the network. Attestations are updated/created for only the provided lien statuses.

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
    api_instance = springlabs.AttestationGroupsApi(api_client)
    id = 'id_example' # str | Participant-provided unique ID of the attestation group to update, create, or get.
attestation_group_input = springlabs.AttestationGroupInput() # AttestationGroupInput |  (optional)

    try:
        # Update or create an attestation group
        api_response = api_instance.upsert_attestation_group_by_id(id, attestation_group_input=attestation_group_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttestationGroupsApi->upsert_attestation_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Participant-provided unique ID of the attestation group to update, create, or get. | 
 **attestation_group_input** | [**AttestationGroupInput**](AttestationGroupInput.md)|  | [optional] 

### Return type

[**AttestationGroupDigest**](AttestationGroupDigest.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated the attestation group with the given ID. |  -  |
**400** | Invalid input data error response. |  -  |
**401** | Unauthorized error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_attestation_groups**
> AttestationGroupsBulkResponse upsert_attestation_groups(attestation_groups_bulk_request=attestation_groups_bulk_request)

Update or create registry attestation groups in bulk

This endpoint allows Participants to update/create attestation groups in bulk for publication to the network. Attestations are updated/created for only the provided lien statuses.

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
    api_instance = springlabs.AttestationGroupsApi(api_client)
    attestation_groups_bulk_request = springlabs.AttestationGroupsBulkRequest() # AttestationGroupsBulkRequest |  (optional)

    try:
        # Update or create registry attestation groups in bulk
        api_response = api_instance.upsert_attestation_groups(attestation_groups_bulk_request=attestation_groups_bulk_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttestationGroupsApi->upsert_attestation_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attestation_groups_bulk_request** | [**AttestationGroupsBulkRequest**](AttestationGroupsBulkRequest.md)|  | [optional] 

### Return type

[**AttestationGroupsBulkResponse**](AttestationGroupsBulkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully attempted update/creation. Success/failure is reported per attestation group. |  -  |
**400** | Invalid input data error response. |  -  |
**401** | Unauthorized error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

