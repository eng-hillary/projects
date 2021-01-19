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

STATUS = (
    (None, "--please select--"),
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected')
 )

REGISTER_STATUS = (
    (None, "--please select--"),
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),

 )
CAPITAL = (
    (None, "--please select--"),
    (100000, '100,000'),
    (500000, '200,000-500,000'),
    (1000000, '1,000,000-2,000,000'),
    (2000000, '2,000,000-3,000,000'),
    (3000000, '3,000,000-5,000,000'),
    (6000000, '6,000,000-10,000,000'),
    (10000000, '10,000,000 and above'),
    
    
    
    

    # ('500,000-1,000,000', '500,000-1,000,000'),
    # ('1,000,000-2,000,000', '1,000,000-2,000,000'),
    # ('3,000,000-5,000,000', '3,000,000-5,000,000'),
    # ('5,000,000-10,000,000', '5,000,000-10,000,000'),
    # ('Above 10,000,000', 'Above 10,000,000'),
   
)
TYPE = (
    (None, "--please select--"),
    ('wholeseller', 'whole seller'),
    ('retail', 'Retail'),
)

SCALE = (
    (None, "--please select--"),
    ('subsistence', 'Subsistence Production'),
    ('small', 'small Commercial Production'),
    ('large','large Commercial Production')
)
SECTOR = (
    (None, "--please select--"),
    ('Animal Farming','Animal Farming'),
    ('Poultry Farming','Poultry Farming'),
    ('Fisheries','Fisheries'),
    ('Crop Farming','Crop Farming'),
    ('Agro Forestry','Agro Forestry'),
    

)
INCOME = (
    (None, "--please select--"),
    ("Below 500,000ugx", "Below 500,000ugx"),
    ("500,000-2,000,000","500,000-2,000,000"),
    ("Above 2,000,000","Above 2,000,000"),
)

INVENTORY_STATUS = (
     (None, "--please select--"),
     ('availabe', 'Available'),
     ('not_available', 'Not Available')
)

QUERIES = (
     (None, "--please select--"),
     ('pest', 'Pest'),
     ('disease', 'Disease'),
     ('general_query', 'General Query')
)

LAND_TYPES = (
     (None, "---please select---"),
    ('rented', 'Rented'),
    ('owned', 'Owned')
)



YES_OR_NO=(
    (None, '--please select--'),
    (True, 'Yes'),
    (False, 'No')
)


TRANSACTION_TYPE = (
    (None, '--please select--'),
    ('income', 'Income'),
    ('expense', 'expense')
)

PAYMENT_MODE = (
    (None, '--please select--'),
    ('cash', 'Cash'),
    ('bank', 'Bank Transfer'),
    ('cheque', 'Cheque'),
    ('mobilemoney', 'Mobile Money'),
    ('credit_card', 'credit card'),
    ('others', 'Others')

    )
SERVICE_CATEGORY = (
    (None, '--please select--'),
    ('storage', 'Storage'),
    ('transport', 'Transport'),
    ('value addition', 'Value Addition'),
    ('sorting and graining', 'Sorting and Graining'),
    ('Veterinary Services', 'Veterinary Services'),
    ('Agro-input providers','Agro-input providers'),
    ('machinery', 'Machinery'),
    ('land', 'Land'),
    ('others', 'Others')

    )


PAYMENT_OPTIONS = (
    (None, '--please select--'),
    ('credit', 'Credit'),
    ('full_payment', 'Full payment'),
    ('installements', 'Installements'),
    ('exchange', 'Exchange')
    )

WEATHER_OPTIONS = (
    (None, '--please select--'),
    ('windy', 'Windy'),
    ('rainy', 'Rainy'),
    ('sunny', 'Sunny'),
    ('cloudy', 'Cloudy'),
    
    )

RESOURCE_CATEGORY = (
    (None, "--please select--"),
    ('storage', 'Storage'),
    ('machinery', 'Machinery'),
    ('land', 'Land'),
    ('transportation', 'Transportation'),    
)
PROFESSION = (
    (None, "---please select---"),
    ('Agriculture related', 'Agriculture related'),
    ('Non-agriculture related', 'Non-agriculture related')
)

UNIT = (
    (None, "---please select---"),
    ('kgs', 'Kgs'),
    ('tonnes', 'Tonnes'),
    ('litres', 'litres'),

)
EDUCATION_LEVEL = (
    (None, "---please select---"),
    ('primary','primary'),
    ('olevel','Olevel'),
    ('Alevel','Alevel'),
    ('College','College'),
    ('tertiary','tertiary'),
    

    ('University','University'),
    ('Never gone to school','Never gone to school'),

)





PAST_YEARS = [year for year in range(datetime.date.today().year, 1899, -1)]