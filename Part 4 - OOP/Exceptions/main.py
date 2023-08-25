'''Custom  exception classes'''
from http import HTTPStatus
from datetime import datetime
import json
from traceback import TracebackException

class WidgetException(Exception, TracebackException):
    '''Base class for all custom exceptions'''
    error_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_error_message = 'Something just crashed'
    user_error_message = 'Sorry, there is an error on our end. Please bare with us.'

    def __init__(self, *args, user_error_message=None) -> None:
        if args:
            super().__init__(*args)
            self.internal_error_message = args[0]
        else:
            super().__init__(self.internal_error_message)
        
        if user_error_message is not None:
            self.user_error_message = user_error_message
    
    @property
    def traceback(self):
        return TracebackException.from_exception(self).format()
    
    def log_exc(self):
        exception = {
            "time": datetime.utcnow().isoformat(),
            "type of error": type(self).__name__,
            "status": self.error_status,
            "internal message": self.internal_error_message,
            "args": self.args[1:],
            "traceback": list(self.traceback)
        }
        return exception
    
    def to_json(self):
        to_user = {
            "time": datetime.utcnow().isoformat(),
            "message": self.user_error_message,
            "category": type(self).__name__
        }
        json_obj = json.dumps(to_user)
        return json_obj

class SupplierException(WidgetException):
    internal_error_message = 'Supplier Exception'

class NotManufactured(SupplierException):
    internal_error_message = 'Widget is no longer manufactured by supplier'

class ProductionDelayed(SupplierException):
    internal_error_message = 'Widget production has been delayed by manufacturer'

class ShippingDelayed(SupplierException):
    internal_error_message = 'Widget shipping has been delayed by supplier'

class CheckoutException(WidgetException):
    internal_error_message = 'Checkout Exception'

class InventoryTypeException(CheckoutException):
    internal_error_message = 'Something just crashed'

class OutOfStock(InventoryTypeException):
    internal_error_message = 'Inventory is out of stock'

class PricingException(CheckoutException):
    internal_error_message = 'Pricing Exception'

class InvalidCoupon(PricingException):
    internal_error_message = 'Invalid Coupon code'
    user_error_message = 'Sorry, this coupon is invalid.'
    error_status = HTTPStatus.BAD_REQUEST

class CannotStackCoupons(PricingException):
    internal_error_message = 'Cannot Stack Coupons error'
    user_error_message = "Sorry, you can't stack coupons."
    error_status = HTTPStatus.BAD_REQUEST


try:
    raise CannotStackCoupons()
except CannotStackCoupons as ex:
    print(ex.log_exc())





