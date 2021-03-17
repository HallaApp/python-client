# Product

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_id** | **str** | The primary key for a product at a given store. | 
**sku** | **str** | Secondary id to link identical products inside of a retailer&#39;s system. | [optional] 
**upc_e** | **str** | Secondary link to third party databases to leverage rich product attributes. | [optional] 
**upc_a** | **str** | Secondary link to third party databases to leverage rich product attributes. | [optional] 
**ean** | **str** | Secondary link to third party databases to leverage rich product attributes. | [optional] 
**plu** | **str** | Secondary link to third party databases to leverage rich product attributes. | [optional] 
**label** | **str** | Primary product name. | 
**description** | **str** | Secondary descriptive text. | [optional] 
**quantity** | **float** | Amount of product sold. | [optional] 
**unit_of_measure** | **str** | Unit this product is measured in. &#39;pack, lb, kg, oz, ml, etc.&#39; | [optional] 
**brand** | **str** | Marketing and promotional brand this product is sold under. | [optional] 
**manufacturer** | **str** | Manufacturer of a given product. | [optional] 
**ingredients** | **str** | String of ingredients found in this product. | [optional] 
**nutrients** | [**list[Nutrient]**](Nutrient.md) | Nutrition information for this product. | [optional] 
**image_urls** | **list[str]** | Links to product images. | [optional] 
**tags** | **dict(str, list[str])** | Flexible data structure to capture custom attributes such as categorization, tags, flavors, diet complience, etc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


