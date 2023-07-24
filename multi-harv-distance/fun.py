import math
import numpy as np
from numba import njit
import pandas as pd
import random

def dummy_dataset(n_resto=120, max_onpo=80,center=(106.816634, -6.2124234)):
    list_array_lat = []
    list_array_long = []
    len_point = []
    for i in range(n_resto):
        # N = random.randint(0,max_onpo)
        if max_onpo<=20:
            N = min(int(np.random.beta(1,5) * max_onpo * 2), max_onpo)
        else:
            N = min(int(np.random.beta(1,10) * max_onpo * 1.25), max_onpo)
        lat1 = []
        long1 = []
        for i in range(N):
            diff1 = random.random()*(random.random()*0.1)
            diff2 = random.random()*(random.random()*0.1)

            lat1.append(center[1]+diff1)
            long1.append(center[0]+diff2)
        list_array_lat.append(lat1)
        list_array_long.append(long1)
        len_point.append(N)

    df = pd.DataFrame()
    df['long_array'] = list_array_long
    df['lat_array'] = list_array_lat
    df['n_point'] = len_point
    return df

## current hdist
def haversine_distance_summary(coord_list: list, coord2: tuple):
    lon2, lat2 = coord2
    phi_2 = math.radians(lat2)
    R = 6371000
    km_array = []

    for coord1 in coord_list:
        lon1, lat1 = coord1
        phi_1 = math.radians(lat1)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        meters = R * c 
        km = meters / 1000.0
        km_array.append(round(km, 3))

    # Taking statistics summary of distance 
    if len(km_array)==0:
        return (25, 25)
    else:
        # return (np.max(km_array),  np.min(km_array) , np.mean(km_array))
        return (np.min(km_array) , np.mean(km_array))

# def haversine_distance_summary2(coord_list: list, coord2: tuple):
#     km_array = []

#     for coord1 in coord_list:
#         lon1 = np.array([coord1[0]])
#         lat1 = np.array([coord1[1]])
#         km = haversine_dist_np(lon1, lat1, center_coord=coord2)[0]
#         km_array.append(round(km, 3))

#     # Taking statistics summary of distance 
#     if len(km_array)==0:
#         return (25, 25)
#     else:
#         # return (np.max(km_array),  np.min(km_array) , np.mean(km_array))
#         return (np.min(km_array) , np.mean(km_array))

## hdist for 2 distance
def haversine_dist(coord1: tuple, coord2: tuple):
    lon2, lat2 = coord2
    lon1, lat1 = coord1
    phi_2 = math.radians(lat2)
    R = 6371000

    phi_1 = math.radians(lat1)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    meters = R * c 
    km = meters / 1000.0
    
    return round(km,5)

@njit
def haversine_dist_np(lon1: np.array, lat1: np.array, center_coord: tuple):
    R = 6371
    N0 = len(lat1)
    lon2 = np.ones(N0)*center_coord[0]
    lat2 = np.ones(N0)*center_coord[1]
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    delta_lambda = lon2 - lon1
    delta_phi = lat2 - lat1
    a = np.sin(delta_phi / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(delta_lambda / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    km = R * c
    return km

def hdist_summary(lon, lat, center):
    lon = np.array(lon)
    lat = np.array(lat)
    km_array = haversine_dist_np(lon, lat, center)

    if len(km_array)==0:
        return (25, 25)
    else:
        return (np.min(km_array) , np.mean(km_array))


