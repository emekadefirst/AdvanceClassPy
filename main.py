import asyncio
import requests

async def fetch_data(url):
    print(f"Start fetching {url}")
    data = requests.get(url)
    print(f"Finished fecting {url}")
    return f"Data from {data}"


async def main():
    urls = ['https://dummyjson.com/producta', 'https://dummyjson.com/users', 'https://dummyjason.com/comments']
    task = [fetch_data (url) for url in urls]
    results = await asyncio .gather(*task)
    print(f"Results: {results}")

asyncio.run(main())

# def print(
#     *values: object,
#     sep: str | None = " ",
#     end: str | None = "\n",
#     file: SupportsWrite[str] | None = None,
#     flush: Literal[False] = False
# ) -> None