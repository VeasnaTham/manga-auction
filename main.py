from fastapi import FastAPI
import uvicorn
from modules.manga.controller import router as manga_router
from modules.user.controller import router as user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    docs_URL = '/docs'
)
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify the allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(manga_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
    