# swagger_client
<p><strong>Getting Started:</strong></p> <ol type=\"1\"> <li><p>Obtain Credentials (Please Contact Halla to Obtain Credentials):</p> <ol type=\"a\"> <li><p><strong>'serviceAccount'</strong>: Add your Service Account in the <strong>header</strong> for all API requests to the Halla services. This is used to track API usage for authorization, billing, etc.</p></li> <li><p><strong>'key'</strong>: Add your API Key to the <strong>query</strong> for all API requests to the Halla services. This is used as a first line of defense to authenticate API requests.</p></li> </ol></li> <li><p>Add Your Catalog:</p> <ol type=\"a\"> <li><p>Use the <strong>POST STORE</strong> route to create a virtual product catalog. Please add a minimum of 1 <strong>thousand products per store</strong>, each with a <strong>'primaryId'</strong> and <strong>'label'</strong>. This will trigger Halla to index the catalog, allowing for Recommendation, Substitution, and Search services within minutes.</p></li> </ol></li> <li><p>Get Recommendations:</p> <ol type=\"a\"> <li><p>Use the <strong>GET PRODUCTS</strong> route and set the strategy to <strong>'recommend'</strong>.</p></li> <li><p>Fill in the <strong>'storeId'</strong> query parameter to use a specific catalog.</p></li> <li><p>Provide <strong>one or more</strong> of the following query parameters:</p> <ol type=\"i\"> <li><p><strong>'productId'</strong>: Biases recommendations to be relevant for a specific product.</p></li> <li><p><strong>'cartProductIds'</strong>: Biases recommendations to be relevant for all products in the cart.</p></li> <li><p><strong>'consumerId'</strong>: Biases recommendations to be relevant for the consumer's previous browsing and past purchase history.</p></li> </ol></li> <li><p>If multiple inputs are given, the recommendations will be blended to best satisfy multiple constraints.</p></li> </ol></li> <li><p>Get Substitutions:</p> <ol type=\"a\"> <li><p>Use the <strong>GET PRODUCTS</strong> route and set the strategy to <strong>'substitute'</strong>.</p></li> <li><p>Fill in the <strong>'storeId'</strong> query parameter to use a specific catalog.</p></li> <li><p>Fill in the <strong>'productId'</strong> query parameter.</p></li> </ol></li> <li><p>Get Search Results:</p> <ol type=\"a\"> <li><p>Use the <strong>GET PRODUCTS</strong> route and set the strategy to <strong>'search'</strong>.</p></li> <li><p>Fill in the <strong>'storeId'</strong> query parameter to use a specific catalog.</p></li> <li><p>Fill in the <strong>'text'</strong> query parameter.</p></li> </ol></li> <li><p>Supercharge Performance with Purchases:</p> <ol type=\"a\"> <li><p>Use the <strong>POST ORDER</strong> route to add one or more transactions to our system. Transactions will be used to fine tune our models to provide a better experience for your shoppers. To enable advanced personalization, please provide the <strong>'consumerId'</strong> field.</p></li> </ol></li> </ol> <p><strong>Advanced Integration:</strong></p> <ul> <li><p>Integrate Multi-Tenant Capabilities:</p> <ul> <li><p>Ensure that store and product <strong>ids</strong> are <strong>globally unique</strong> across all tenants. If needed, tenant name can be appended to the id in question to guarantee uniqueness.</p></li> <li><p>Attach <strong>'brand'</strong> field to allow for better personalization at scale.</p></li> </ul></li> <li><p>Enable Real-Time Inventory:</p> <ul> <li><p>Integrate the <strong>POST STORE</strong> route into your inventory management solution and do one of the following:</p> <ul> <li><p>Call the <strong>POST STORE</strong> route at regular intervals to overwrite existing store data.</p></li> <li><p>Call the <strong>ADD / DELETE</strong> product from store routes to update the catalog upon changes and current availabilities.</p></li> </ul></li> </ul></li> <li><p>(BETA) Enable Advanced Filtering:</p> <ul> <li><p>To enable SNAP, Own-Brand, Sponsored Product and other custom filters, create multiple virtual stores for each real store location. Each virtual store should correspond to a subset of products to include in the filter. Store ids can be generated by prepending the filter identifier to your store id.</p></li> </ul></li> <li><p>(BETA) Run an A/B Test:</p> <ul> <li><p>Work with your Halla Support Rep to define the scope of your A/B test.</p></li> <li><p>Call the <strong>POST ORDER</strong> route to add purchases with which to evaluate.</p></li> <li><p>If you are <strong>tracking spend</strong> between test groups, then it is <strong>required</strong> to attach the <strong>'campaign'</strong> field in the request body of the order.</p></li> <li><p>If you are <strong>testing at the consumer level</strong>, then it is <strong>required</strong> to attach the <strong>'consumerId'</strong> field in the request body of the order.</p></li> </ul></li> <li><p>(BETA) Add Fulfillment Data:</p> <ul> <li><p>Call the <strong>POST ORDER</strong> route multiple times corresponding to when an order is placed and later fulfilled. Set the <strong>'code'</strong> attribute in each item to <strong>'purchased' or 'fulfilled'</strong> corresponding to the order status.</p></li> </ul></li> </ul> 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build date: 2021-03-17T20:51:27.934Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = swagger_client.DefaultApi
service_account = 'service_account_example' # str | Identifies the serviceAccount for authorization purposes.
orders = swagger_client.Orders() # Orders | The orders to create. (optional)

try:
    api_instance.add_orders(service_account, orders=orders)
except ApiException as e:
    print "Exception when calling DefaultApi->add_orders: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://devapi.develop.halla.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add_orders**](docs/DefaultApi.md#add_orders) | **POST** /v2/orders | 
*DefaultApi* | [**add_products_to_many_stores**](docs/DefaultApi.md#add_products_to_many_stores) | **POST** /v2/stores/products | 
*DefaultApi* | [**add_products_to_store**](docs/DefaultApi.md#add_products_to_store) | **POST** /v2/stores/{sid}/products | 
*DefaultApi* | [**add_store**](docs/DefaultApi.md#add_store) | **POST** /v2/stores | 
*DefaultApi* | [**delete_store**](docs/DefaultApi.md#delete_store) | **DELETE** /v2/stores/{sid} | 
*DefaultApi* | [**get_products**](docs/DefaultApi.md#get_products) | **GET** /v2/products | 
*DefaultApi* | [**get_products_from_store**](docs/DefaultApi.md#get_products_from_store) | **GET** /v2/stores/{sid}/products | 
*DefaultApi* | [**get_search_terms**](docs/DefaultApi.md#get_search_terms) | **GET** /v2/searchTerms | 
*DefaultApi* | [**get_store**](docs/DefaultApi.md#get_store) | **GET** /v2/stores/{sid} | 
*DefaultApi* | [**get_store_ids**](docs/DefaultApi.md#get_store_ids) | **GET** /v2/stores | 
*DefaultApi* | [**remove_product_from_store**](docs/DefaultApi.md#remove_product_from_store) | **DELETE** /v2/stores/{sid}/products/{pid} | 


## Documentation For Models

 - [InlineResponse200](docs/InlineResponse200.md)
 - [Item](docs/Item.md)
 - [Nutrient](docs/Nutrient.md)
 - [Order](docs/Order.md)
 - [Orders](docs/Orders.md)
 - [Product](docs/Product.md)
 - [ProductRecommendation](docs/ProductRecommendation.md)
 - [ProductSummary](docs/ProductSummary.md)
 - [ProductUpdate](docs/ProductUpdate.md)
 - [Products](docs/Products.md)
 - [SearchTerm](docs/SearchTerm.md)
 - [Store](docs/Store.md)
 - [Updates](docs/Updates.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string


## Author


