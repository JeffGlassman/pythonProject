# cluster_sizer/forms.py
from django import forms

class ClusterSizingForm(forms.Form):
    daily_ingest_rate = forms.FloatField(
        label="Daily Ingest Rate (GB)",
        help_text="Enter the expected daily data ingest volume in gigabytes."
    )
    
    retention_days = forms.IntegerField(
        label="Retention Period (Days)",
        help_text="Specify the number of days the data should be retained."
    )
    replicas = forms.IntegerField(
        label="Number of Replicas",
        help_text="Enter the number of replicas to store for each shard. Typically 1-2."
    )
    endpoints = forms.IntegerField(
        label="Number of Endpoints",
        help_text="Enter the number of endpoints on the network."
    )
    write_speed = forms.BooleanField(
        label="Write Speed",
        help_text="Check if you require high write speed. If unsure, leave unchecked."
    )
    
    hot_retention_days = forms.IntegerField(
        label="Hot phase retention Period (roughly)",
        help_text="Specify the number of days the data should be retained in the hot phase."
    )
    warm_retention_days = forms.IntegerField(
        label="Warm phase retention Period (roughly)",
        help_text="Specify the number of days the data should be retained in the warm phase."
    )
    cold_retention_days = forms.IntegerField(
        label="Cold phase retention Period (roughly)",
        help_text="Specify the number of days the data should be retained in the cold phase."
    )
    machine_learning = forms.BooleanField(
        label="Machine Learning",
        help_text="Check if you plan to run machine learning jobs on this cluster."
    )
    kibana = forms.IntegerField(
        label="Kibana Nodes",
        help_text="Enter the number of Kibana nodes to deploy."
    )   