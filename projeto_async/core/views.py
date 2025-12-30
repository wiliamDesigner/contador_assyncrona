import asyncio
import httpx
from django.http import JsonResponse

async def contador(request):
    tempo = 0

    for i in range(1, 6):
        await asyncio.sleep(1)
        tempo += 1

    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")

    return JsonResponse({
        "mensagem": "Contador finalizado",
        "tempo_em_segundos": tempo,
        "status_http": response.status_code
    })
