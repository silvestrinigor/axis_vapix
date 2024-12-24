from datetime import datetime, timezone
from .defaults import ApiVersion

def serialize_datetime(date_time: datetime) -> str:
    if not _is_timezone_aware(date_time=date_time): 
        raise ValueError("The datetime object must be timezone-aware")
    date_time_utc = date_time.astimezone(timezone.utc)
    serialized_date_time = date_time_utc.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
    return serialized_date_time

def _is_timezone_aware(date_time: datetime) -> bool:
    return date_time.tzinfo is not None and date_time.tzinfo.utcoffset(date_time) is not None

def get_apiversion_type_from_string(api_version: str):
    parts = api_version.split('.')
    if len(parts) != 2:
        raise ValueError(f"Invalid API version format: '{api_version}'. Expected 'major.minor'.")
    try:
        major = int(parts[0])
        minor = int(parts[1])
    except ValueError:
        raise ValueError(f"Invalid version numbers in '{api_version}'. Both major and minor must be integers.")
    return ApiVersion(major, minor)