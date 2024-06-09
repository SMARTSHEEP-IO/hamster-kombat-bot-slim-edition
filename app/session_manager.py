from pyrogram import Client
from pyrogram.errors import RPCError
from app.config import settings
from app import logger


async def register_sessions() -> None:
    API_ID = settings.API_ID
    API_HASH = settings.API_HASH

    if not API_ID or not API_HASH:
        raise ValueError("API_ID and API_HASH must be set in the .env file.")

    while True:
        session_name = input('\nEnter the session name (press Enter to exit): ').strip()

        if not session_name:
            logger.info("Session registration cancelled by the user.")
            break

        session = Client(
            name=session_name,
            api_id=API_ID,
            api_hash=API_HASH,
            workdir="sessions/"
        )

        try:
            async with session:
                user_data = await session.get_me()
                logger.success(f'Session added successfully: @{user_data.username} | {user_data.first_name} {user_data.last_name}')
                break
        except RPCError as e:
            logger.error(f"Failed to register session: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
