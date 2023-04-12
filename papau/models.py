from django.db import models

class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    license_number = models.CharField(max_length=20)

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    property_type = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.DecimalField(max_digits=10, decimal_places=2)
    listing_agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    listing_date = models.DateField()
    listing_status = models.CharField(max_length=20)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=20)
    transaction_date = models.DateField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='buyer_transactions')
    seller_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='seller_transactions')
    buyer_client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='buyer_transactions')
    seller_client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='seller_transactions')
    transaction_status = models.CharField(max_length=20)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2)

