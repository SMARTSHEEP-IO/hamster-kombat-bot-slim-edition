from pyrogram import Client
from app.config import settings
from app.sysout import logger
import base64
class Frame:
    def headers(self):
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en-GB,en;q=0.9',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'Origin': 'https://hamsterkombat.io',
            'Referer': 'https://hamsterkombat.io/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Ch-Ua': '"Safari";v="15", "Mobile";v="15", "Not.A/Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"iOS"',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
        }
        return headers

    async def register_sessions(self) -> None:
        API_ID = settings.API_ID
        API_HASH = settings.API_HASH

        if not API_ID or not API_HASH:
            raise ValueError("API_ID and API_HASH not found in the .env file.")

        session_name = input('\nEnter the session name (press Enter to exit): ')

        if not session_name:
            return None

        session = Client(
            name=session_name,
            api_id=API_ID,
            api_hash=API_HASH,
            workdir="sessions/"
        )

        async with session:
            user_data = await session.get_me()

        logger.success(f'Session added successfully @{user_data.username} | {user_data.first_name} {user_data.last_name}')

    def escape_html(self,text: str) -> str:
        return text.replace('<', '\\<').replace('>', '\\>')


    def decode_cipher(self,cipher: str) -> str:
        encoded = cipher[:3] + cipher[4:]
        return base64.b64decode(encoded).decode('utf-8')


frame = Frame()
