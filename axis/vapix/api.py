from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Dict

class VapixApiABC(ABC):
    API_PATH: str

    def _remove_none_values(self, body: Dict) -> Dict:
        if not isinstance(body, Dict):
            return body
        return {
            key: self._remove_none_values(value)
            for key, value in body.items() if value is not None
        }

    def _serialize_datetime(self, date_time: datetime) -> str:
        if not self._is_timezone_aware(date_time): 
            raise ValueError("The datetime object must be timezone-aware")
        date_time_utc = date_time.astimezone(timezone.utc)
        serialized_date_time = date_time_utc.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        return serialized_date_time

    def _is_timezone_aware(self, date_time: datetime) -> bool:
        return date_time.tzinfo is not None and date_time.tzinfo.utcoffset(date_time) is not None

class VapixApiWithVersionABC(VapixApiABC, ABC):

    @abstractmethod
    def getSupportedVersions(self):
        pass