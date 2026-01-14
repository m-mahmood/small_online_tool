from django.shortcuts import render
from .forms import BarkCalculatorForm

BARK_RATES = {
    "USA": {"Budget": 20, "Average": 45, "Premium": 85},
    "UK": {"Budget": 18, "Average": 40, "Premium": 75},
    "Canada": {"Budget": 25, "Average": 50, "Premium": 90},
    "France": {"Budget": 22, "Average": 45, "Premium": 85},
    "New Zealand": {"Budget": 30, "Average": 60, "Premium": 100},
    "China": {"Budget": 10, "Average": 22, "Premium": 40},
    "India": {"Budget": 8, "Average": 18, "Premium": 35},
    "Pakistan": {"Budget": 7, "Average": 15, "Premium": 28},
    "Saudi Arabia": {"Budget": 20, "Average": 42, "Premium": 80},
    "UAE": {"Budget": 22, "Average": 45, "Premium": 85}
}

def bark_calculator_view(request):
    result = None
    if request.method == 'POST':
        form = BarkCalculatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            l = data['length']
            w = data['width']
            d_cm = data['depth']
            country = data['country']
            quality = data['quality']

            # Convert depth to meters
            d_m = d_cm / 100
            
            # 1. Calculate Base Volume (Cubic Meters)
            volume_m3 = l * w * d_m
            
            # 2. Add 7% Safety Margin for compaction and uneven ground
            volume_with_margin = volume_m3 * 1.07
            
            # 3. Calculate Bags based on Standard Bulk Bag size (0.75 m³ or 750 Litres)
            standard_bag_size_m3 = 0.75
            # We use math.ceil to ensure we suggest buying whole bags to cover the area
            import math
            num_bags = math.ceil(volume_with_margin / standard_bag_size_m3)
            
            # 4. Calculate Cost
            rate = BARK_RATES[country][quality]
            cost = volume_with_margin * rate

            result = {
                'qty_m3': f"{volume_with_margin:.2f}",
                'qty_bags': f"{num_bags}",
                'cost': f"${cost:.2f}",
            }
    else:
        form = BarkCalculatorForm()
    return render(request, 'bark_calc/tool.html', {'form': form, 'result': result})