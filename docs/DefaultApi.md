# swagger_client.DefaultApi

All URIs are relative to *https://devapi.develop.halla.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_orders**](DefaultApi.md#add_orders) | **POST** /v2/orders | 
[**add_products_to_many_stores**](DefaultApi.md#add_products_to_many_stores) | **POST** /v2/stores/products | 
[**add_products_to_store**](DefaultApi.md#add_products_to_store) | **POST** /v2/stores/{sid}/products | 
[**add_store**](DefaultApi.md#add_store) | **POST** /v2/stores | 
[**delete_store**](DefaultApi.md#delete_store) | **DELETE** /v2/stores/{sid} | 
[**get_products**](DefaultApi.md#get_products) | **GET** /v2/products | 
[**get_products_from_store**](DefaultApi.md#get_products_from_store) | **GET** /v2/stores/{sid}/products | 
[**get_search_terms**](DefaultApi.md#get_search_terms) | **GET** /v2/searchTerms | 
[**get_store**](DefaultApi.md#get_store) | **GET** /v2/stores/{sid} | 
[**get_store_ids**](DefaultApi.md#get_store_ids) | **GET** /v2/stores | 
[**remove_product_from_store**](DefaultApi.md#remove_product_from_store) | **DELETE** /v2/stores/{sid}/products/{pid} | 


# **add_orders**
> add_orders(service_account, orders=orders)



Adds new orders, updating associated consumer profiles to allow for real-time personalization.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
orders = swagger_client.Orders() # Orders | The orders to create. (optional)

try: 
    api_instance.add_orders(service_account, orders=orders)
except ApiException as e:
    print "Exception when calling DefaultApi->add_orders: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **orders** | [**Orders**](Orders.md)| The orders to create. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_products_to_many_stores**
> add_products_to_many_stores(service_account, updates=updates)



Bulk method to apply product updates across multiple stores. Note: OVERWRITE will remove products with matching product ids in stores not provided in the request.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
updates = swagger_client.Updates() # Updates | The updates to apply. (optional)

try: 
    api_instance.add_products_to_many_stores(service_account, updates=updates)
except ApiException as e:
    print "Exception when calling DefaultApi->add_products_to_many_stores: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **updates** | [**Updates**](Updates.md)| The updates to apply. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_products_to_store**
> add_products_to_store(service_account, sid, products=products)



Adds one or more products to a store. This method will create a new store if the store id does not exist and will index the newly created products, letting these products be used as input to the Halla services.  Notes:  -Halla will perform best on inventories between 1,000 and 50,000 products.  -Primary product ids persist across multiple stores for a given client.  -Never before seen products will be added in minutes.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
sid = 'sid_example' # str | Subscriber specific store id
products = swagger_client.Products() # Products | The products to create. (optional)

try: 
    api_instance.add_products_to_store(service_account, sid, products=products)
except ApiException as e:
    print "Exception when calling DefaultApi->add_products_to_store: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **sid** | **str**| Subscriber specific store id | 
 **products** | [**Products**](Products.md)| The products to create. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_store**
> add_store(service_account, store=store)



Creates / overwrites a store with a distinct catalog. Notes: -Halla will perform best on inventories between 1,000 and 50,000 products. -Primary product ids persist across multiple stores for a given client.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
store = swagger_client.Store() # Store | The store to create. (optional)

try: 
    api_instance.add_store(service_account, store=store)
except ApiException as e:
    print "Exception when calling DefaultApi->add_store: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **store** | [**Store**](Store.md)| The store to create. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_store**
> delete_store(service_account, sid)



Deletes store data.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
sid = 'sid_example' # str | Subscriber specific store id

try: 
    api_instance.delete_store(service_account, sid)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_store: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **sid** | **str**| Subscriber specific store id | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> list[ProductRecommendation] get_products(strategy, service_account, text=text, product_id=product_id, cart_product_ids=cart_product_ids, consumer_id=consumer_id, store_id=store_id, limit=limit)



Real-time, contextual product recommendation, substitution and search. Returns a list of products with attached relevance scores.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
strategy = 'strategy_example' # str | Determines which service should be used for this request. Choose from recommend, substitute, or search.
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
text = 'text_example' # str | Text input if search strategy is selected. (optional)
product_id = 'product_id_example' # str | Subscriber specific product identifier to recommend based on. Required for substitution strategy. (optional)
cart_product_ids = 'cart_product_ids_example' # str | A comma delimited string of subscriber specific product identifiers for a consumer's current cart. If productId is not passed in the query, then recommendations will be based on the cartProductIds. If a productId is passed in the query, then cartProductIds will be used to improve recommendation relevance. (optional)
consumer_id = 'consumer_id_example' # str | Subscriber specific consumer identifier to personalize recommendations. If productId and cartProductIds are not passed in the query, then recommendations will be based on previous consumer behavior. (optional)
store_id = 'store_id_example' # str | Subscriber specific store identifier, selecting the catalog of products to recommend from. If storeId is invalid or is not passed in the query, then recommendations will be sourced from the subscriber's master product list. (optional)
limit = 56 # int | Upper bound on the number of products to return. Default = 15. Max = 30. (optional)

try: 
    api_response = api_instance.get_products(strategy, service_account, text=text, product_id=product_id, cart_product_ids=cart_product_ids, consumer_id=consumer_id, store_id=store_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_products: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy** | **str**| Determines which service should be used for this request. Choose from recommend, substitute, or search. | 
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **text** | **str**| Text input if search strategy is selected. | [optional] 
 **product_id** | **str**| Subscriber specific product identifier to recommend based on. Required for substitution strategy. | [optional] 
 **cart_product_ids** | **str**| A comma delimited string of subscriber specific product identifiers for a consumer&#39;s current cart. If productId is not passed in the query, then recommendations will be based on the cartProductIds. If a productId is passed in the query, then cartProductIds will be used to improve recommendation relevance. | [optional] 
 **consumer_id** | **str**| Subscriber specific consumer identifier to personalize recommendations. If productId and cartProductIds are not passed in the query, then recommendations will be based on previous consumer behavior. | [optional] 
 **store_id** | **str**| Subscriber specific store identifier, selecting the catalog of products to recommend from. If storeId is invalid or is not passed in the query, then recommendations will be sourced from the subscriber&#39;s master product list. | [optional] 
 **limit** | **int**| Upper bound on the number of products to return. Default &#x3D; 15. Max &#x3D; 30. | [optional] 

### Return type

[**list[ProductRecommendation]**](ProductRecommendation.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products_from_store**
> list[Product] get_products_from_store(service_account, sid)



Gets all products in a store.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
sid = 'sid_example' # str | Subscriber specific store id

try: 
    api_response = api_instance.get_products_from_store(service_account, sid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_products_from_store: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **sid** | **str**| Subscriber specific store id | 

### Return type

[**list[Product]**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_terms**
> list[SearchTerm] get_search_terms(text, service_account, limit=limit)



Grocery specific autocomplete for search.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
text = 'text_example' # str | Text to autocomplete.
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
limit = 56 # int | Upper bound on the number of search terms to return. Default = 15. Max = 30. (optional)

try: 
    api_response = api_instance.get_search_terms(text, service_account, limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_search_terms: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text to autocomplete. | 
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **limit** | **int**| Upper bound on the number of search terms to return. Default &#x3D; 15. Max &#x3D; 30. | [optional] 

### Return type

[**list[SearchTerm]**](SearchTerm.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store**
> list[Product] get_store(service_account, sid)



Gets store data.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
sid = 'sid_example' # str | Subscriber specific store id

try: 
    api_response = api_instance.get_store(service_account, sid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_store: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **sid** | **str**| Subscriber specific store id | 

### Return type

[**list[Product]**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_ids**
> InlineResponse200 get_store_ids(service_account)



Gets all store ids.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.

try: 
    api_response = api_instance.get_store_ids(service_account)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_store_ids: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_product_from_store**
> remove_product_from_store(service_account, sid, pid)



Removes a product from a store.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
sid = 'sid_example' # str | Subscriber specific store id
pid = 'pid_example' # str | Subscriber specific product id

try: 
    api_instance.remove_product_from_store(service_account, sid, pid)
except ApiException as e:
    print "Exception when calling DefaultApi->remove_product_from_store: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account** | **str**| Identifies the serviceAccount for authorization purposes. | 
 **sid** | **str**| Subscriber specific store id | 
 **pid** | **str**| Subscriber specific product id | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

