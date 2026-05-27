from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["threatguard"])


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/incidents/timeline")
def get_incident_timeline() -> dict[str, list[dict[str, str]]]:
    return {
        "incidents": [
            {
                "id": "inc-001",
                "severity": "high",
                "summary": "Anomalia comportamental detectada em endpoint corporativo"
            }
        ]
    }
