from farmer.views import [
    FarmerView,

]


app_name = 'farmer'

urlpatterns = [
     path('', FarmerView.as_view(), name='farmer'),
    # path('', FarmerView.as_view(), name='farmer'),



]
