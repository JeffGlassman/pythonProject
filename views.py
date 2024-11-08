# cluster_sizer/views.py

from django.shortcuts import render
from .forms import ClusterSizingForm
from .sizer_calculations import calculate_cluster_requirements


def calculate_cluster_size(request):
    if request.method == 'POST':
        form = ClusterSizingForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            daily_ingest = form.cleaned_data['daily_ingest_rate']
            retention_days = form.cleaned_data['retention_days']
            replicas = form.cleaned_data['replicas']

            # Call the Python function to perform the calculations
            result = calculate_cluster_requirements(daily_ingest, retention_days, replicas)

            # Render the results page with calculated data
            return render(request, 'cluster_sizer/results.html', {'result': result})
    else:
        form = ClusterSizingForm()

    return render(request, 'cluster_sizer/input.html', {'form': form})
