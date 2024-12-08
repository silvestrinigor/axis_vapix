from datetime import datetime, timezone

def serialize_datetime(date_time: datetime):
    if date_time.tzinfo is None:
        raise ValueError("The datetime object must be timezone-aware")
    date_time_utc = date_time.astimezone(timezone.utc)
    serialized_date_time = date_time_utc.strftime("%Y-%m-%dT%H:%M:$SZ")
    return serialized_date_time