# coding: utf-8

"""
    Halla I/O

    <p><strong>Getting Started:</strong></p> <ol type=\"1\"> <li><p>Obtain Credentials (Please Contact Halla to Obtain Credentials):</p> <ol type=\"a\"> <li><p><strong>'serviceAccount'</strong>: Add your Service Account in the <strong>header</strong> for all API requests to the Halla services. This is used to track API usage for authorization, billing, etc.</p></li> <li><p><strong>'key'</strong>: Add your API Key to the <strong>query</strong> for all API requests to the Halla services. This is used as a first line of defense to authenticate API requests.</p></li> </ol></li> <li><p>Add Your Catalog:</p> <ol type=\"a\"> <li><p>Use the <strong>POST STORE</strong> route to create a virtual product catalog. Please add a minimum of 1 <strong>thousand products per store</strong>, each with a <strong>'primaryId'</strong> and <strong>'label'</strong>. This will trigger Halla to index the catalog, allowing for Recommendation, Substitution, and Search services within minutes.</p></li> </ol></li> <li><p>Get Recommendations:</p> <ol type=\"a\"> <li><p>Use the <strong>GET PRODUCTS</strong> route and set the strategy to <strong>'recommend'</strong>.</p></li> <li><p>Fill in the <strong>'storeId'</strong> query parameter to use a specific catalog.</p></li> <li><p>Provide <strong>one or more</strong> of the following query parameters:</p> <ol type=\"i\"> <li><p><strong>'productId'</strong>: Biases recommendations to be relevant for a specific product.</p></li> <li><p><strong>'cartProductIds'</strong>: Biases recommendations to be relevant for all products in the cart.</p></li> <li><p><strong>'consumerId'</strong>: Biases recommendations to be relevant for the consumer's previous browsing and past purchase history.</p></li> </ol></li> <li><p>If multiple inputs are given, the recommendations will be blended to best satisfy multiple constraints.</p></li> </ol></li> <li><p>Get Substitutions:</p> <ol type=\"a\"> <li><p>Use the <strong>GET PRODUCTS</strong> route and set the strategy to <strong>'substitute'</strong>.</p></li> <li><p>Fill in the <strong>'storeId'</strong> query parameter to use a specific catalog.</p></li> <li><p>Fill in the <strong>'productId'</strong> query parameter.</p></li> </ol></li> <li><p>Get Search Results:</p> <ol type=\"a\"> <li><p>Use the <strong>GET PRODUCTS</strong> route and set the strategy to <strong>'search'</strong>.</p></li> <li><p>Fill in the <strong>'storeId'</strong> query parameter to use a specific catalog.</p></li> <li><p>Fill in the <strong>'text'</strong> query parameter.</p></li> </ol></li> <li><p>Supercharge Performance with Purchases:</p> <ol type=\"a\"> <li><p>Use the <strong>POST ORDER</strong> route to add one or more transactions to our system. Transactions will be used to fine tune our models to provide a better experience for your shoppers. To enable advanced personalization, please provide the <strong>'consumerId'</strong> field.</p></li> </ol></li> </ol> <p><strong>Advanced Integration:</strong></p> <ul> <li><p>Integrate Multi-Tenant Capabilities:</p> <ul> <li><p>Ensure that store and product <strong>ids</strong> are <strong>globally unique</strong> across all tenants. If needed, tenant name can be appended to the id in question to guarantee uniqueness.</p></li> <li><p>Attach <strong>'brand'</strong> field to allow for better personalization at scale.</p></li> </ul></li> <li><p>Enable Real-Time Inventory:</p> <ul> <li><p>Integrate the <strong>POST STORE</strong> route into your inventory management solution and do one of the following:</p> <ul> <li><p>Call the <strong>POST STORE</strong> route at regular intervals to overwrite existing store data.</p></li> <li><p>Call the <strong>ADD / DELETE</strong> product from store routes to update the catalog upon changes and current availabilities.</p></li> </ul></li> </ul></li> <li><p>(BETA) Enable Advanced Filtering:</p> <ul> <li><p>To enable SNAP, Own-Brand, Sponsored Product and other custom filters, create multiple virtual stores for each real store location. Each virtual store should correspond to a subset of products to include in the filter. Store ids can be generated by prepending the filter identifier to your store id.</p></li> </ul></li> <li><p>(BETA) Run an A/B Test:</p> <ul> <li><p>Work with your Halla Support Rep to define the scope of your A/B test.</p></li> <li><p>Call the <strong>POST ORDER</strong> route to add purchases with which to evaluate.</p></li> <li><p>If you are <strong>tracking spend</strong> between test groups, then it is <strong>required</strong> to attach the <strong>'campaign'</strong> field in the request body of the order.</p></li> <li><p>If you are <strong>testing at the consumer level</strong>, then it is <strong>required</strong> to attach the <strong>'consumerId'</strong> field in the request body of the order.</p></li> </ul></li> <li><p>(BETA) Add Fulfillment Data:</p> <ul> <li><p>Call the <strong>POST ORDER</strong> route multiple times corresponding to when an order is placed and later fulfilled. Set the <strong>'code'</strong> attribute in each item to <strong>'purchased' or 'fulfilled'</strong> corresponding to the order status.</p></li> </ul></li> </ul> 

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ProductUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, products=None, store_ids=None, action=None):
        """
        ProductUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'products': 'list[Product]',
            'store_ids': 'list[str]',
            'action': 'str'
        }

        self.attribute_map = {
            'products': 'products',
            'store_ids': 'storeIds',
            'action': 'action'
        }

        self._products = products
        self._store_ids = store_ids
        self._action = action

    @property
    def products(self):
        """
        Gets the products of this ProductUpdate.
        Product information to update.

        :return: The products of this ProductUpdate.
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this ProductUpdate.
        Product information to update.

        :param products: The products of this ProductUpdate.
        :type: list[Product]
        """

        self._products = products

    @property
    def store_ids(self):
        """
        Gets the store_ids of this ProductUpdate.
        Array of all stores to apply this update to.

        :return: The store_ids of this ProductUpdate.
        :rtype: list[str]
        """
        return self._store_ids

    @store_ids.setter
    def store_ids(self, store_ids):
        """
        Sets the store_ids of this ProductUpdate.
        Array of all stores to apply this update to.

        :param store_ids: The store_ids of this ProductUpdate.
        :type: list[str]
        """

        self._store_ids = store_ids

    @property
    def action(self):
        """
        Gets the action of this ProductUpdate.
        Defines the action this update will take. Choose from: ADD, DELETE, or OVERWRITE. Will default to ADD.

        :return: The action of this ProductUpdate.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ProductUpdate.
        Defines the action this update will take. Choose from: ADD, DELETE, or OVERWRITE. Will default to ADD.

        :param action: The action of this ProductUpdate.
        :type: str
        """

        self._action = action

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
