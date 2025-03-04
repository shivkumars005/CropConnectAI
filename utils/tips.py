def get_rotation_tips(crop, region):
    # Mock database
    crop_rotation_database = {
        ("wheat", "north america"): {
            "primary": "Legumes",
            "alternatives": ["Barley", "Canola", "Soybean"],
            "region_tip": "Alternate with legumes for nitrogen replenishment."
        },
        ("rice", "south asia"): {
            "primary": "Pulses",
            "alternatives": ["Wheat", "Corn", "Mustard"],
            "region_tip": "Avoid monocropping to reduce pest risks."
        },
        ("corn", "europe"): {
            "primary": "Clover",
            "alternatives": ["Oats", "Rye", "Beans"],
            "region_tip": "Incorporate cover crops to improve soil structure."
        }
    }
    
    # Normalize inputs
    crop = crop.lower()
    region = region.lower()
    
    # Fetch rotation tips or return None
    return crop_rotation_database.get((crop, region), None)

def get_organic_farming_tips():
    return [
        "Use compost and organic manure to enrich soil health.",
        "Practice crop rotation to prevent pest buildup and maintain soil fertility.",
        "Adopt natural pest control methods like neem oil or biological controls.",
        "Grow cover crops to prevent soil erosion and suppress weeds."
    ]
