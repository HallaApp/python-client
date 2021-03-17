# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_id** | **str** | Identifies the consumer to allow for one to one personalization. | [optional] 
**order_id** | **str** | Identifies the order. | 
**store_id** | **str** | Links the order to a store. | [optional] 
**date** | **str** | &#39;YYYY-MM-DD HH:mm:ss&#39; formatted date object specifying a (4 digit year, 2 digit month, 2 digit day, 0-24 hour, 2 digit minute and 2 digit second) time interval in GMT. Will use current date if not provided. | [optional] 
**campaign** | **str** | Flexible identifier specifying the campaign this order belongs to. Used for A/B testing. | [optional] 
**items** | [**list[Item]**](Item.md) | Individual transaction elements in this order. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


