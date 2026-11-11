from fastmcp import FastMCP

from contextlib import asynccontextmanager
from routes.mcp_server_router import mcp_router
from migrations.migration import Migration
from migrations.seeder import Seeder
 
from dotenv import load_dotenv

load_dotenv()
# ==================== LIFESPAN EVENTS ====================
@asynccontextmanager
async def lifespan(app: FastMCP):
    migration = Migration()
    migration.run_startup_migration()
    

    seeder = Seeder()
    seeder.run_startup_seeding()
    yield
 
# ==================== FASTAPI APPLICATION ====================
app = FastMCP(
    
    name = "mcp-server-chatbot",
    lifespan=lifespan
)

app.mount(mcp_router)
# ==================== MAIN ENTRY ====================
if __name__ == "__main__":
    app.run(transport= "streamable-http")
