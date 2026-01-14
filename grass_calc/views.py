from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .forms import GrassCalculatorForm

# Mock Database of Prices (USD per sq meter)
GRASS_PRICES = {
    "USA": {"Budget": 5, "Average": 12, "Premium": 25},
    "UK": {"Budget": 4, "Average": 10, "Premium": 20},
    "Canada": {"Budget": 6, "Average": 13, "Premium": 26},
    "France": {"Budget": 5.5, "Average": 11, "Premium": 22},
    "New Zealand": {"Budget": 7, "Average": 15, "Premium": 28},
    "China": {"Budget": 3, "Average": 6, "Premium": 12},
    "India": {"Budget": 2.5, "Average": 5, "Premium": 10},
    "Pakistan": {"Budget": 2, "Average": 4, "Premium": 8},
    "Saudi Arabia": {"Budget": 5, "Average": 11, "Premium": 24},
    "UAE": {"Budget": 6, "Average": 13, "Premium": 30},
}

@cache_page(60 * 5)
def grass_calculator_view(request):
    result = None
    
    if request.method == 'POST':
        form = GrassCalculatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            length = data['length']
            width = data['width']
            country = data['country']
            quality = data['quality']
            
            # Calculate Base Area
            area = length * width
            
            # Add 5% Wastage
            waste_factor = 0.05 
            total_area_with_waste = area * (1 + waste_factor)
            
            # Calculate Total Cost
            price_per_unit = GRASS_PRICES[country][quality]
            total_cost = total_area_with_waste * price_per_unit
            
            # Calculate Rolls (2m x 25m = 50 sqm per roll)
            roll_area = 2 * 25  # 50 sq meters
            num_rolls = total_area_with_waste / roll_area
            
            result = {
                'total_area': f"{total_area_with_waste:.2f}",
                'num_rolls': f"{num_rolls:.2f}",
                'cost': f"${total_cost:.2f}",
                'unit': ' m²'
            }
    else:
        form = GrassCalculatorForm()

    return render(request, 'grass_calc/tool.html', {'form': form, 'result': result})