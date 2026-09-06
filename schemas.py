"""Pydantic schemas for LastPass Enterprise Connector."""
from __future__ import annotations
from typing import Any, Optional, List, Dict
from pydantic import BaseModel, Field

class NoParams(BaseModel):
    """Empty parameters model."""
    pass

class ConnectParams(BaseModel):
    label: str = Field(default="", description="Friendly connection label, e.g. Primary LastPass Enterprise.")
    api_key: str = Field(description="Enterprise API Key / Access Token")
    base_url: str = Field(default="https://lastpass.com/enterpriseapi.php", description="LastPass Enterprise API base URL.")

class ConnectionIdParams(BaseModel):
    connection_id: str = Field(default="", description="Connection identifier (empty uses active connection).")

class ConnectionRecord(BaseModel):
    id: str
    label: str
    masked_key: str
    base_url: str
    is_active: bool

class ConnectionList(BaseModel):
    connections: list[ConnectionRecord]
    total: int

class DeleteResult(BaseModel):
    success: bool
    message: str

class VaultItemRecord(BaseModel):
    id: str
    name: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    raw: Dict[str, Any] = Field(default_factory=dict)

class VaultItemList(BaseModel):
    vault_items: list[VaultItemRecord]
    total: int

class ListVaultItemParams(BaseModel):
    connection_id: str = Field(default="", description="Optional connection ID.")
    limit: int = Field(default=20, ge=1, le=100, description="Max records to return.")

class GetVaultItemParams(BaseModel):
    connection_id: str = Field(default="", description="Optional connection ID.")
    vaultitem_id: str = Field(description="LastPass Enterprise VaultItem ID.")

class AuditHealthReport(BaseModel):
    healthy: bool
    total_vault_items: int
    details: Dict[str, Any] = Field(default_factory=dict)
    summary: str
