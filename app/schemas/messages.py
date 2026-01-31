from pydantic import BaseModel
from typing import Optional, Literal

# مدل تنظیمات اولیه (که اول کار از موبایل می‌آید)
class ClientConfig(BaseModel):
    type: Literal["config"]
    hostLanguage: str
    targetLanguage: str
    voiceGender: Literal["MALE", "FEMALE"]

# پیام‌های عادی موبایل (صدا و دستورات)
class MobileMessage(BaseModel):
    type: str  # "audio_chunk", "cycle_agent", یا "config"
    data: Optional[str] = None


# پیام‌های سرور به موبایل - هماهنگ با انتظارات موبایل
class ServerMessage(BaseModel):
    type: str
    data: Optional[str] = None


# پیام صدای ترجمه شده - type باید "audio_delta" باشد
class AudioDeltaMessage(BaseModel):
    type: Literal["audio_delta"] = "audio_delta"
    data: str  # Base64 encoded audio


# پیام متن ترجمه - type باید "transcript" باشد
class TranscriptMessage(BaseModel):
    type: Literal["transcript"] = "transcript"
    text: str
    isFinal: bool = True
    agentId: str


# پیام خطا
class ErrorMessage(BaseModel):
    type: Literal["error"] = "error"
    code: int
    message: str