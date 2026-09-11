from django.db import models


class Organization(models.Model):
    CATEGORY = [
        ('NPO', 'Non-Profit Organization'),
        ('NGO', 'Non-Governmental Organization'),
        ('NPC', 'Non-Profit Company'),
        ('CORP', 'Corporate Partner'),
    ]
    PROVINCE = [
        ('GP', 'Gauteng'),
        ('WC', 'Western Cape'),
        ('KZN', 'KwaZulu-Natal'),
        ('EC', 'Eastern Cape'),
        ('FS', 'Free State'),
        ('LP', 'Limpopo'),
        ('MP', 'Mpumalanga'),
        ('NC', 'Northern Cape'),
        ('NW', 'North West'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=4, choices=CATEGORY)
    province = models.CharField(max_length=2, choices=PROVINCE)
    description = models.TextField()
    mission = models.TextField(blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Member Organization"
        verbose_name_plural = "Communi-Connect Umbrella – Member Organizations"

    def __str__(self):
        return self.name


class Donation(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    donor_name = models.CharField(max_length=200)
    donor_email = models.EmailField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default='ZAR')
    message = models.TextField(blank=True)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor_name} – R{self.amount}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.subject}"
