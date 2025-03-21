import json
from collections import defaultdict

# Sample JSON data
locations_json = '''[
{"id": "loc_01", "latitude": 37.7749, "longitude": -122.4194},
{"id": "loc_04", "latitude": 27.8749, "longitude": 122.4194},
{"id": "loc_05", "latitude": 57.2749, "longitude": -112.4344},
{"id": "loc_06", "latitude": 14.0522, "longitude": -119.2531},
{"id": "loc_07", "latitude": 64.0522, "longitude": -108.2330},
{"id": "loc_02", "latitude": 34.0522, "longitude": -118.2437},
{"id": "loc_08", "latitude": 24.0522, "longitude": -168.2197},
{"id": "loc_03", "latitude": 40.7128, "longitude": -74.0060}
]'''

metadata_json = '''[
{"id": "loc_01", "type": "restaurant", "rating": 4.5, "reviews": 120},
{"id": "loc_04", "type": "restaurant", "rating": 4.1, "reviews": 500},
{"id": "loc_05", "type": "restaurant", "rating": 3.7, "reviews": 110},
{"id": "loc_02", "type": "hotel", "rating": 4.2, "reviews": 200},
{"id": "loc_06", "type": "hotel", "rating": 4.0, "reviews": 700},
{"id": "loc_07", "type": "hotel", "rating": 2.0, "reviews": 900},
{"id": "loc_03", "type": "cafe", "rating": 4.7, "reviews": 150},
{"id": "loc_08", "type": "cafe", "rating": 4.5, "reviews": 750}
]'''

locations = json.loads(locations_json)
metadata = json.loads(metadata_json)

location_dict = {loc["id"]: loc for loc in locations}

merged_data = []
for meta in metadata:
    loc_id = meta["id"]
    if loc_id in location_dict:
        merged_data.append({**location_dict[loc_id], **meta})
    else:
        merged_data.append(meta) 

type_counts = defaultdict(int)
for data in merged_data:
    type_counts[data["type"]] += 1

rating_sums = defaultdict(float)
rating_counts = defaultdict(int)
for data in merged_data:
    rating_sums[data["type"]] += data["rating"]
    rating_counts[data["type"]] += 1

average_ratings = {t: rating_sums[t] / rating_counts[t] for t in rating_sums}

highest_reviews_location = max(merged_data, key=lambda x: x["reviews"])

incomplete_data = [data for data in merged_data if "latitude" not in data or "longitude" not in data]

# Display results
print("Valid Points Per Type:", type_counts)
print("Average Ratings Per Type:", average_ratings)
print("Location with Highest Reviews:", highest_reviews_location)
print("Locations with Incomplete Data:", incomplete_data)
