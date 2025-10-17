from django.db import models

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('recycling', 'Recycling'),
        ('composting', 'Composting'),
        ('disposal', 'Disposal'),
    ]
    WASTE_TYPE_CHOICES = [
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('glass', 'Glass'),
        ('organic', 'Organic'),
        ('metal', 'Metal'),
        ('e-waste', 'E-Waste'),
        ('clothing', 'Clothing'),
        ('hazardous', 'Hazardous'),
        ('construction', 'Construction'),
        ('medical', 'Medical'),
    ]
    
    title = models.CharField(max_length=500)
    waste_type = models.CharField(max_length=50, choices=WASTE_TYPE_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    # Make sure these fields exist
    image = models.CharField(max_length=500, blank=True, null=True)  # Changed to CharField for file paths
    recycling_process = models.TextField()
    products_made = models.TextField()
    making_process = models.TextField()
    tutorial_links = models.TextField(blank=True, null=True)  # Changed to TextField for multiple links
    uganda_spotlight = models.TextField(blank=True, null=True)
    fun_fact = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Educational Resource"
        verbose_name_plural = "Educational Resources"
        ordering = ['waste_type']
        # Remove or modify unique_together if it's causing issues
        # unique_together = ['waste_type', 'category']

    def __str__(self):
        return self.title
    
    def get_waste_type_display(self):
        """Get human-readable waste type name"""
        return dict(self.WASTE_TYPE_CHOICES).get(self.waste_type, self.waste_type)
    
    def get_category_display(self):
        """Get human-readable category name"""
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)