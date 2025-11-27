from ninja import Router
from django.contrib.auth import get_user_model

router = Router(
    tags=["users"],
)

User = get_user_model()


@router.post("/create")
async def create_user(request):
    return []