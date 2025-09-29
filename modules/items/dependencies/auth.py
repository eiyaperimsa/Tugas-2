# from fastapi import Depends, HTTPException, status, Request

# def get_current_user_role(request: Request) -> str:
#     # Dummy: ambil role dari header 'X-Role'.
#     # Di aplikasi nyata, ambil dari token/session/database
#     role = request.headers.get('X-Role')
#     if not role:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Role header missing")
#     return role

# def admin_required(role: str = Depends(get_current_user_role)):
#     if role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Admin only"
#         )
