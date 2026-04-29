import asyncio
from centrifuge import Client

url = "wss://ws.nobitex.ir/connection/websocket"

async def main():
    client = Client(url)

    sub = client.new_subscription(
        "public:orderbook-BTCIRT",
        {"delta": "fossil"}
    )

    @sub.on("subscribed")
    def on_subscribed(ctx):
        print("subscribed")

    @sub.on("publication")
    def on_publication(ctx):
        print(ctx.data)

    await client.connect()
    await sub.subscribe()

    while True:
        await asyncio.sleep(1)

asyncio.run(main())