import os
import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

#define the MCP server
mcp_fetch_server = MCPServerStdio(
    command="python",
    args=["-m", "mcp_server_fetch"]
)

#configure groq api key
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


# Creating the AI Agent
agent = Agent(
    model = "groq:llama-3.3-70b-versatile",
    mcp_server = [mcp_fetch_server]
)

#main async function
async def main():
    url = input("Enter the URL to extract and summarize: ")

    async with agent.run_mcp_servers():
        result = await agent.run(f"extract the content and summarize it: {url}")
        output = result.output
        return output

# run the main function
if __name__ == "__main__":
    output = asyncio.run(main())
    print(output)