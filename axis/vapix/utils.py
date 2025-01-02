from datetime import datetime, timezone
from packaging import version
import re
import pytz

def serialize_datetime(date_time: datetime) -> str:
    if not _is_timezone_aware(date_time=date_time): 
        raise ValueError("The datetime object must be timezone-aware")
    date_time_utc = date_time.astimezone(timezone.utc)
    serialized_date_time = date_time_utc.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
    return serialized_date_time

def _is_timezone_aware(date_time: datetime) -> bool:
    return date_time.tzinfo is not None and date_time.tzinfo.utcoffset(date_time) is not None

def get_apiversion_type_from_string(api_version: str):
    return version.parse(api_version)

def get_firmwareversion_type_from_string(firmwareversion: str):
    try:
        return version.parse(firmwareversion)
    except:
        return _parse_to_packaging_version(firmwareversion)

def _parse_to_packaging_version(version_str):
    pattern = r"(\d+)\.(\d+)(?:-(.*))?"
    match = re.match(pattern, version_str)
    if match:
        major = match.group(1)
        minor = match.group(2)
        custom_part = match.group(3)
        if custom_part:
            version_string = f"{major}.{minor}.0+{custom_part}"
        else:
            version_string = f"{major}.{minor}.0"
        parsed_version = version.parse(version_string)
        return parsed_version
    else:
        raise ValueError(f"Invalid version format: {version_str}")

def get_all_timezones():
    return pytz.all_timezones

