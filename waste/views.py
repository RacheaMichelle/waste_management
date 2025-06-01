
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import WasteListingForm
from .models import WasteListing
from django.contrib import messages  # <-- Add this import

@login_required
def list_waste(request):
    if request.method == 'POST':
        form = WasteListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('waste_list')
    else:
        form = WasteListingForm()
    listings = WasteListing.objects.filter(user=request.user)
    return render(request, 'waste/list.html', {'form': form, 'listings': listings})

@login_required
def update_waste(request, pk):
    listing = get_object_or_404(WasteListing, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WasteListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing updated successfully!")
            return redirect('waste_list')
    else:
        form = WasteListingForm(instance=listing)
    
    return render(request, 'waste/update.html', {'form': form})

@login_required
def delete_waste(request, pk):
    listing = get_object_or_404(WasteListing, pk=pk, user=request.user)
    if request.method == 'POST':
        listing.delete()
        messages.success(request, "Listing deleted successfully!")
        return redirect('waste_list')
    
    return render(request, 'waste/delete.html', {'listing': listing})