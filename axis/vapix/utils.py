from datetime import datetime, timezone


def serialize_datetime(date_time: datetime) -> str:
    if not is_timezone_aware(date_time=date_time): 
        raise ValueError("The datetime object must be timezone-aware")
    date_time_utc = date_time.astimezone(timezone.utc)
    serialized_date_time = date_time_utc.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
    return serialized_date_time


def is_timezone_aware(date_time: datetime) -> bool:
    return date_time.tzinfo is not None and date_time.tzinfo.utcoffset(date_time) is not None


def remove_none_values(body: dict) -> dict:
    """Utility function to recursively remove keys with None values."""
    if not isinstance(body, dict):
        return body
    return {
        key: remove_none_values(value)
        for key, value in body.items()
        if value is not None
    }