import os
from django.core.management.base import BaseCommand
from django.conf import settings
from waste.models import WasteListing  # adjust if your model is named differently

class Command(BaseCommand):
    help = 'Check if waste listing images exist on disk.'

    def handle(self, *args, **kwargs):
        missing_images = 0
        total = 0

        for listing in WasteListing.objects.all():
            total += 1
            if listing.image:
                image_path = listing.image.path
                if not os.path.exists(image_path):
                    self.stdout.write(
                        self.style.ERROR(f"[MISSING] Listing ID {listing.id} - {image_path}")
                    )
                    missing_images += 1
                else:
                    self.stdout.write(self.style.SUCCESS(f"[OK] Listing ID {listing.id} - {listing.image.url}"))
            else:
                self.stdout.write(self.style.WARNING(f"[NO IMAGE] Listing ID {listing.id} - No image assigned"))

        self.stdout.write(self.style.NOTICE(f"\nChecked {total} listings. Missing images: {missing_images}"))
