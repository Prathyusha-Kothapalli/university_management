import re
from typing import Dict, Any, Optional
from sqlalchemy import text
from sqlalchemy.orm import Session


class TenantManager:
    """
    Enterprise Multi-Tenancy Manager providing dynamic schema isolation,
    tenant switching, and feature flag management per university tenant.
    """
    def __init__(self):
        self._tenant_feature_flags: Dict[str, Dict[str, bool]] = {
            "default": {
                "ai_assistant": True,
                "plagiarism_checker": True,
                "proctored_exams": True,
                "dr_library": True,
                "live_gps_transport": True,
                "obe_curriculum": True,
                "crypto_transcripts": True
            }
        }
        self._tenant_schemas: Dict[str, str] = {
            "default": "public"
        }

    def sanitize_schema_name(self, tenant_slug: str) -> str:
        clean = re.sub(r'[^a-zA-Z0-9_]', '_', tenant_slug.lower())
        return f"tenant_{clean}"

    def set_tenant_schema(self, db: Session, tenant_slug: str) -> str:
        schema_name = self.sanitize_schema_name(tenant_slug)
        self._tenant_schemas[tenant_slug] = schema_name
        
        # Execute PostgreSQL schema context switch safely
        try:
            db.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
            db.execute(text(f"SET search_path TO {schema_name}, public"))
            db.commit()
        except Exception:
            db.rollback()
            
        return schema_name

    def get_feature_flags(self, tenant_id: str) -> Dict[str, bool]:
        return self._tenant_feature_flags.get(
            tenant_id,
            self._tenant_feature_flags["default"]
        )

    def set_feature_flag(self, tenant_id: str, feature: str, enabled: bool) -> Dict[str, bool]:
        if tenant_id not in self._tenant_feature_flags:
            self._tenant_feature_flags[tenant_id] = self._tenant_feature_flags["default"].copy()
        
        self._tenant_feature_flags[tenant_id][feature] = enabled
        return self._tenant_feature_flags[tenant_id]


tenant_manager = TenantManager()
