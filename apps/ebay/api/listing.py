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
        print(api.response.dict())
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
    return api.response.dict()


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
            "PrimaryCategory": {"CategoryID": item.ebay_cat_primary},
            "StartPrice": item.price,
            "CategoryMappingAllowed": "true",
            "ConditionID": "1000",
            "Currency": "USD",
            "Country": item.item_country,
            "Location": item.item_location,
            "PostalCode": item.item_postal,
            "Quantity": item.quality,
            "DispatchTimeMax": item.dispatch_time_max,
            "ListingType": item.list_type,
            "ListingDuration": item.duration,
            "PaymentMethods": "PayPal",
            "PayPalEmailAddress": item.payment_account,
            "AutoPay": "true",
            "PictureDetails": {
                "PictureURL": item.get_image_checked_list(),
            },
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
                    "ShippingService": item.shipping_internal_service,
                    # "ShippingService": "USPSMedia",
                    # "ShippingService": "ePacketChina",
                    "ShippingServiceCost": item.shipping_internal_cost,
                    "ShippingServiceAdditionalCost": item.shipping_internal_additional_cost,
                    # "FreeShipping": "true",
                },
                "InternationalShippingServiceOption": {
                    "ShippingServicePriority": "1",
                    "ShippingService": item.shipping_international_service,
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