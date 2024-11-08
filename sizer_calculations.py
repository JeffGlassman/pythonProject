# cluster_sizer/sizer_calculations.py
import math
def calculate_cluster_requirements(daily_ingest, retention_days, replicas):
    # Calculate total data volume (in GB)
    total_data_volume = daily_ingest * retention_days * (1 + replicas)
    total_data_volume =+ total_data_volume * .15  # Add 15% buffer for watermarkng
        

def calculate_hot_nodes(hot_retention_days, daily_ingest, replicas, write_speed):
    # calculate data volume in warm phase
    hot_data_volume = hot_retention_days * daily_ingest * (1 + replicas)
    # calculate number of nodes needed based off a 1:100 ram to disk ratio
    ram = hot_data_volume / 64
    ram = ram.round()
    recommended_hot_nodes = ram / 64
    if write_speed == True and recommended_hot_nodes > 3 and replicas == 1:
        primary_shards >= 2
    else:
        primary_shards = 1
    global eru_hot
    eru_hot = ram / 64
    eru_hot = math.ceil(eru_hot)
    return {
        'recommended_nodes': int(recommended_hot_nodes),
        'primary_shards': int(primary_shards),
        'eru_hot': int(eru_hot),        
    }   

def calculate_warm_nodes(warm_retention_days, daily_ingest, replicas):
    # calculate data volume in warm phase
    warm_data_volume = warm_retention_days * daily_ingest * (1 + replicas)
    # calculate number of nodes needed based off a 1:100 ram to disk ratio
    ram = warm_data_volume / 100
    ram = ram.round()
    recommended_warm_nodes = ram / 64
    global eru_warm
    eru_warm = ram / 64
    eru_warm = math.ceil(eru_warm)
    return {
        'recommended_nodes': int(recommended_warm_nodes),
        'eru_warm': int(eru_warm),
    }
    
def calculate_cold_nodes(cold_retention_days, daily_ingest, replicas):
    # calculate data volume in warm phase
    cold_data_volume = cold_retention_days * daily_ingest * (1 + replicas)
    # calculate number of nodes needed based off a 1:100 ram to disk ratio
    ram = cold_data_volume / 200
    ram = ram.round()
    recommended_nodes = ram / 64
    global eru_cold
    eru_cold = ram / 64
    eru_cold = math.ceil(eru_cold)
    return {
        'recommended_nodes': int(recommended_nodes),
        'eru_cold': int(eru_cold),
    }
    
def calculate_ml_nodes(machine_learning):
    if machine_learning == True:
        ml_nodes = 1
        global eru_ml
        ram = input("Enter the amount of RAM in GB for the machine learning node: ")
        eru_ml = ram / 64
        eru_ml = math.ceil(eru_ml)
    else:
        ml_nodes = 0
        eru_ml = 0
    return {
        'recommended_nodes': int(ml_nodes),
        'eru_ml': int(eru_ml),
    }

def kibana_nodes(kibana):
    ram = 8 * kibana
    global eru_kibana
    eru_kibana = ram / 64
    eru_kibana = math.ceil(eru_kibana)
    return {
        'recommended_nodes': int(kibana),
        'eru_kibana': int(eru_kibana),
    }

def frozen_nodes(daily_ingest, frozen_retention_days, disk_size):
    ram = (daily_ingest * frozen_retention_days * .5) / 50
    recommended_nodes = frozen_retention_days * daily_ingest / disk_size
    recommended_nodes = math.ceil(recommended_nodes)
    disk_cache = frozen_retention_days * .04
    global eru_frozen
    eru_frozen = ram / 64
    return {
        'recommended_nodes': int(recommended_nodes),
        'eru_frozen': float(eru_frozen),
        'disk_cache': float(disk_cache),
    }
# Assumption of 8 GB of RAM per node for dedicated master nodes
def master_nodes():
    master_nodes = 3
    ram = 8 * master_nodes
    global eru_master
    eru_master = ram / 64
    return {
        'master_nodes': int(master_nodes),
    }
# Setting Kibana nodes to 16 GB of RAM
# Setting Eru Kibana to 64 GB of RAM
    
def kibana_nodes(kibana):
    ram = 16 * kibana
    global eru_kibana
    eru_kibana = ram / 64
    eru_kibana = math.ceil(eru_kibana)
    return {
        'recommended_nodes': int(kibana),
        'eru_kibana': int(eru_kibana),
    }
# Get total ERU count
def total_eru():
    global eru_count
    eru_count = eru_master + eru_hot + eru_warm + eru_cold + eru_ml + eru_kibana + eru_frozen
    eru_count = math.ceil(total_eru)
    return {
        'total_eru_count': int(total_eru),
    }