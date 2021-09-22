# Order Status Enum
INITIALIZED = "Initialized"
CONFIRMED = "Confirmed"
IN_PROGRESS = "In_Progress"
CREATED = "Created"
BEING_DELIVERED = "Being_Delivered"
DELIVERED = "Delivered"
PAID = "Paid"

order_statuses = (
    (INITIALIZED, 'initialized'),
    (CONFIRMED, 'confirmed'),
    (IN_PROGRESS, 'in_progress'),
    (CREATED, 'created'),
    (BEING_DELIVERED, 'being_delivered'),
    (DELIVERED, 'delivered'),
    (PAID, 'paid')
)