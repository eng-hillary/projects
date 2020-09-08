    district = models.ForeignKey(District, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)# ICT4Farmers
This is system is mainly dedicated to help farmers help each other. 
Imagine a platform where people can share information, imagine the kind of boundaries that will be overtaken. 
Eight Tech Consults and UNFFE are working daily to achieve this goal.
