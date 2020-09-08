import datetime

GENDER_CHOICES = (
     (None, "---please select---"),
    ('female', 'Female'),
    ('male', 'Male')
)

MARITAL_STATUSES = (
    (None, "--please select--"),
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
    ('widowed', 'Widowed')
)

LAND_TYPES = (
     (None, "---please select---"),
    ('rented', 'Rented'),
    ('owned', 'Owned')
)

PRODUCTION_SCALE = (
     (None, "---please select---"),
    ('subsistence', 'subsistence'),
    ('commercial', 'commercial')
)

YES_OR_NO=(
    (None, '--please select--'),
    (True, 'Yes'),
    (False, 'No')
)

ACTION_TYPE = (
    ('planting','Planting'),
    ('treatment', 'Treatment'),
    ('weeding', 'Weeding'),
    ('harvesting', 'Harvesting')
)

TRANSACTION_TYPE = (
    ('income', 'Income'),
    ('expense', 'expense')
)

PAYMENT_MEANS = (
    (None, '--please select--'),
    ('cash', 'Cash'),
    ('bank', 'Bank Transfer'),
    ('cheque', 'Cheque'),
    ('credit_card', 'Credit/Debit Card'),
    ('others', 'Others')

    )


WHEATHER_OPTIONS = (
    (None, '--please select--'),
    ('windy', 'Windy'),
    ('rainy', 'Rainy'),
    ('sunny', 'Sunny'),
    ('cloudy', 'Cloudy'),
    
    )