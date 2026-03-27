def get_vehicle_speed():
    return {
        "speed_kmh": 87
    }


def get_ota_status():
    return {
        "ota_status": "Update available",
        "version": "2026.03",
        "recommended_action": "Install when parked"
    }


def get_dtc_codes():
    return {
        "dtc_codes": [
            {
                "code": "P0A1F",
                "description": "Battery energy control module performance"
            },
            {
                "code": "U0100",
                "description": "Lost communication with ECM/PCM"
            }
        ]
    }