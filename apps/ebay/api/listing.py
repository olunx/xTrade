# -*- coding: utf-8 -*-
__author__ = 'olunx'

import json

from django.conf import settings

from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading

from apps.ebay.models import EbayProductItem


def add_fixed_price_item(data):
    """http://www.utilities-online.info/xmltojson/#.UXli2it4avc
    """

    try:
        api = Trading(domain='api.sandbox.ebay.com', config_file=settings.FILE_EBAY_API_CONFIG, warnings=True, timeout=1000, siteid=0)

        if not data:
            return None
        print data

        api.execute('AddFixedPriceItem', data)
        print(api.response.json())
    except ConnectionError as e:
        print(e)
        print(e.response.dict())


def gen_data_by_item(item_id):
    if not item_id:
        return None
    try:
        item = EbayProductItem.objects.get(id=item_id)
    except EbayProductItem.DoesNotExist:
        return None

    data = {
        "Item": {
            "Title": item.title,
            "Description": "<![CDATA[ %s ]]>" % item.describe,
            "PrimaryCategory": {"CategoryID": "377"},
            "StartPrice": item.price,
            "CategoryMappingAllowed": "true",
            "Country": "US",
            "ConditionID": "1000",
            "Currency": "USD",
            "DispatchTimeMax": item.dispatch_time_max,
            "ListingDuration": item.duration,
            "ListingType": item.list_type,
            "PaymentMethods": "PayPal",
            "PayPalEmailAddress": "lunzii@qq.com",
            "AutoPay": "true",
            "PictureDetails": {
                "PictureURL": item.get_image_checked_list(),
            },
            "PostalCode": "95125",
            "Quantity": item.quality,
            "ReturnPolicy": {
                "ReturnsAcceptedOption": "ReturnsAccepted",
                "RefundOption": "MoneyBack",
                "ReturnsWithinOption": "Days_30",
                "Description": "If you are not satisfied, return the book for refund.",
                "ShippingCostPaidByOption": "Buyer"
            },
            "ShippingDetails": {
                "ShippingType": "Flat",
                "ShippingServiceOptions": {
                    "ShippingServicePriority": "1",
                    "ShippingService": "USPSMedia",
                    # "ShippingService": "ePacketChina",
                    "ShippingServiceCost": item.shipping_internal_cost,
                    "ShippingServiceAdditionalCost": item.shipping_internal_additional_cost,
                    # "FreeShipping": "true",
                },
                "InternationalShippingServiceOption": {
                    "ShippingServicePriority": "1",
                    "ShippingService": "StandardInternational",
                    "ShippingServiceCost": item.shipping_international_cost,
                    "ShippingServiceAdditionalCost": item.shipping_international_additional_cost,
                    "ShipToLocation": item.shipping_international_area,
                }
            },
            "Site": "US"
        }
    }
    return data