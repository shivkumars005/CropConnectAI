def get_mock_prices(crop, region=None):
    # Mock data for demonstration purposes
    mock_data = {
        "Wheat": {
            "prices": [
                {"date": "2025-01-01", "price": 100, "market": "Delhi"},
                {"date": "2025-01-02", "price": 110, "market": "Mumbai"},
                {"date": "2025-01-03", "price": 120, "market": "Chennai"},
            ]
        },
        "Rice": {
            "prices": [
                {"date": "2025-01-01", "price": 80, "market": "Delhi"},
                {"date": "2025-01-02", "price": 85, "market": "Mumbai"},
                {"date": "2025-01-03", "price": 90, "market": "Chennai"},
            ]
        },
        "Cotton": {
            "prices": [
                {"date": "2025-01-01", "price": 140, "market": "Delhi"},
                {"date": "2025-01-02", "price": 110, "market": "Mumbai"},
                {"date": "2025-01-03", "price": 150, "market": "Chennai"},
            ]
        }
    }

    if crop in mock_data:
        return mock_data[crop]
    else:
        return {"error": f"No data available for the crop '{crop}'."}