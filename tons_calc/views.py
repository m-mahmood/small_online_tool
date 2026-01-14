from django.shortcuts import render
from .forms import MaterialConverterForm

DENSITIES = {
    "Topsoil (dry)": 1.2, "Topsoil (wet)": 1.6, "Garden Soil": 1.3, "Fill Dirt": 1.2,
    "Sand (dry)": 1.35, "Sand (wet)": 1.6, "Gravel": 1.4, "Crushed Stone": 1.5,
    "Limestone": 1.45, "Granite": 1.6, "Asphalt (millings)": 1.3, "Concrete (broken)": 1.9,
    "Clay": 1.7, "Bark Mulch": 0.4, "Wood Mulch": 0.5, "Pine Bark": 0.35,
    "Compost": 0.75, "Pea Gravel": 1.45, "River Rock": 1.5, "Decorative Stone": 1.4,
    "Coal": 0.8, "Salt": 1.2, "Gypsum": 1.3,
}

def tons_calculator_view(request):
    result = None
    if request.method == 'POST':
        form = MaterialConverterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            material = data['material']
            value = data['value']
            mode = data.get('mode', 'tons_to_yards')
            density = data['density_custom'] if data['density_custom'] else DENSITIES[material]
            
            if mode == 'tons_to_yards':
                calculated_value = value / density
                input_label = "Tons"
                output_label = "Cubic Yards (yds³)"
                mode_display = "Tons to Yards"
            else:
                calculated_value = value * density
                input_label = "Cubic Yards"
                output_label = "Tons"
                mode_display = "Yards to Tons"

            result = {
                'qty': f"{calculated_value:.2f}", 'unit': output_label,
                'input_qty': f"{value:.2f}", 'input_unit': input_label,
                'formula_used': f"Density: {density} t/yd³", 'mode': mode_display
            }
    else:
        form = MaterialConverterForm()
    return render(request, 'tons_calc/tool.html', {'form': form, 'result': result})