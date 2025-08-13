from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client
import asyncio

async def main():
    async with stdio_client("python", ["server/mcp_server.py"]) as streams:
        session = ClientSession(streams)
        await session.start()

        result = await session.call_tool("pokemon_data", {"name": "pikachu"})
        print("Pokemon Data:", result)

        battle = await session.call_tool("battle_simulator", {"pokemon1": "pikachu", "pokemon2": "charizard"})
        print("Battle Result:", battle)

asyncio.run(main())
