from app.tools import get_vehicle_speed, check_fault_codes, get_adas_status

def route_query(query):
    query_lower = query.lower()

    if "speed" in query_lower:
        return "tool", get_vehicle_speed()
    elif "fault" in query_lower or "diagnostic" in query_lower:
        return "tool", check_fault_codes()
    elif "adas status" in query_lower or "lane assist" in query_lower:
        return "tool", get_adas_status()
    else:
        return "rag", None