from django.db import models
from django.db.models import Avg
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
# from django.dispatch import receiver
# Create your models here.
class adminmodel(models.Model):
    admin_id=models.AutoField(primary_key=True)
    admin_first_name=models.CharField(max_length=255)
    admin_last_name=models.CharField(max_length=255, blank=True)
    admin_email=models.EmailField()
    admin_password=models.CharField(max_length=255)

    def __str__(self):
        return self.admin_first_name

def validate_phone_number(value):
     # Check if the phone number is exactly 10 digits
    if not re.match(r'^\d{10}$', value):
        raise ValidationError(
            _('Phone number must be exactly 10 digits.')
        )
    pass
class CustomerModel(models.Model):
    NORMAL_USER = 'Normal User'
    AGENT_USER = 'Agent User'
    USER_STATUS_CHOICES = [
        (NORMAL_USER, 'Normal User'),
        (AGENT_USER, 'Agent User'),
    ]
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    BOTH = 'Both'
    MALAYALAM = 'Malayalam'
    TAMIL = 'Tamil'
    LANGUAGE_CHOICES = [
        (BOTH, 'Both'),
        (MALAYALAM, 'Malayalam'),
        (TAMIL, 'Tamil'),
    ]
    customer_id = models.AutoField(primary_key=True)
    customer_first_name = models.CharField(max_length=100, default="guest")
    customer_last_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.EmailField(default="example@example.com")
    customer_phone_number = models.CharField(
        max_length=10,  # Ensure max length of 10
        unique=True,  # Enforce uniqueness
        validators=[validate_phone_number]  # Custom validation for exactly 10 digits
    )
    customer_password = models.CharField(max_length=100, default='unknown')
    rating = models.IntegerField(default=0)
    terms_conditions = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    is_existing = models.BooleanField(default=False)
    adhaar_no = models.CharField(max_length=50, default="unknown")
    # terms_conditions = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=USER_STATUS_CHOICES,
        default=NORMAL_USER,
    )
    languages = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default=BOTH,
    )

    def __str__(self):
        return f"{self.customer_first_name} {self.customer_last_name} Phone: {self.customer_phone_number}"

    @property
    def rating(self):
        # from .models import RatingModel
        rating = RatingModel.objects.filter(agent=self).aggregate(Avg('ratings')).get('ratings__avg')
        return rating if rating is not None else 0

    def save(self, *args, **kwargs):
        # Auto-generate serial number for last name if it is not provided
        if not self.customer_last_name:  # Only if customer_last_name is empty
            # Find the last customer with an auto-generated last name
            last_autogen_customer = CustomerModel.objects.filter(
                customer_last_name__startswith="user_"
            ).order_by('customer_id').last()

            if last_autogen_customer:
                # Extract the serial number from the last auto-generated customer
                match = re.match(r'user_(\d+)', last_autogen_customer.customer_last_name)
                if match:
                    new_serial = int(match.group(1)) + 1
                else:
                    new_serial = 1
            else:
                new_serial = 1  # Start with customer_1 if no auto-generated last name exists

            # Set the new customer last name
            self.customer_last_name = f"user_{new_serial}"

        # Call the original save method to save the object
        super(CustomerModel, self).save(*args, **kwargs)

class WalletModel(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    wallet_coins = models.IntegerField(default=300, null=True)
    call_amount = models.FloatField(default=0.0)
    total_minutes = models.IntegerField(default=0)
    total_amount = models.FloatField(default=0.0)

    def __str__(self):
        return f"Wallet of user : {self.user.customer_first_name} {self.user.customer_last_name} Id:- {self.user.customer_id} phone: {self.user.customer_phone_number}"

class CallPackageModel(models.Model):
    coin_id = models.AutoField(primary_key=True)
    package_price = models.FloatField()
    total_coins = models.IntegerField()


class UserPurchaseModel(models.Model):
    # # CHAT = 'Chat'
    # CALL = 'Call'
    # PURCHASE_TYPE_CHOICES = [
    #     (CHAT, 'Chat'),
    #     (CALL, 'Call'),
    # ]
    user_purchase_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()
    purchase_amount = models.FloatField()
    # purchase_type = models.CharField(max_length=10, choices=PURCHASE_TYPE_CHOICES, null=True)


class WithdrawalHistoryModel(models.Model):
    agent_purchase_id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    withdrawal_amount = models.FloatField()
    withdrawal_date = models.DateTimeField()

# call details
class CallDetailsModel(models.Model):
    call_id = models.AutoField(primary_key=True)
    caller = models.ForeignKey(CustomerModel, related_name='caller', on_delete=models.CASCADE)
    agent = models.ForeignKey(CustomerModel, related_name='agent', on_delete=models.CASCADE)
    agora_channel_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(default=0)  # Duration in minutes

class AgentTransactionModel(models.Model):
    # CHAT = 'Chat'
    # CALL = 'Call'
    # TRANSACTION_TYPE_CHOICES = [
    #     (CHAT, 'Chat'),
    #     (CALL, 'Call'),
    # ]
    agent_transaction_id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='received_transactions',
                                 null=True)
    transaction_amount = models.FloatField()
    transaction_date = models.DateTimeField()
    # transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES, null=True)

    def __str__(self):
        return f"{self.agent.customer_first_name} {self.agent.customer_last_name}"


class PaymentModel(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    # package_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # package_object_id = models.PositiveIntegerField()
    # package = GenericForeignKey('package_content_type', 'package_object_id')
    amount = models.FloatField()
    razorpay_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_signature = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.user.customer_first_name} {self.user.customer_last_name}"

class RatingModel(models.Model):
    rating_id = models.AutoField(primary_key = True)
    agent = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='agent_id')
    user = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='user')
    ratings = models.IntegerField()
    created_at = models.DateTimeField()

class Log_Register(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=255)
    message=models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)