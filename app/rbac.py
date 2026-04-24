from fastapi import HTTPException

ROLE_PERMISSIONS = {
    "Admin": ["upload", "view", "search"],
    "Analyst": ["view", "search"],
    "Client": ["upload", "view", "search"]   # ✅ FIXED
}

def check_permission(role: str, action: str):
    perms = ROLE_PERMISSIONS.get(role, [])

    if action not in perms:
        raise HTTPException(status_code=403, detail="Permission denied")

