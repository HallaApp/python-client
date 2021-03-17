# Store

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Used across services to link to this store object. | 
**channel** | **str** | The application type that will be using Halla&#39;s services. &#39;Choose from E_COMMERCE, SELF_SCAN, SMART_CART, PROMOTIONS, OTHER.&#39; | [optional] 
**type** | **str** | The type of store that will be using Halla&#39;s services. &#39;Choose from GROCERY_STORE, SUPER_STORE, CONVENIENCE, DELI, OTHER.&#39; | [optional] 
**brand** | **str** | Brand of store. | [optional] 
**postal_code** | **str** | 5 digit zip code of store location. | [optional] 
**country** | **str** | 2 digit country abbreviation. &#39;US for United States and UK for United Kingdom.&#39; | [optional] 
**products** | [**list[Product]**](Product.md) | Products in the given store&#39;s catalog. | [optional] 
**product_summary** | [**ProductSummary**](ProductSummary.md) | Descriptive information on a store&#39;s products. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


