import asyncio

async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Sunucu {addr!r} adresinden {message!r} mesajını aldı.")

    print(f"Sunucu {addr!r} adresine yanıt gönderiliyor.")
    writer.write(f"Sunucu mesajınızı aldı: {message}".encode())
    await writer.drain()

    print("Bağlantı kapatılıyor.")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f"Sunucu {addr} adresinde başlatıldı.")

    async with server:
        await server.serve_forever()

asyncio.run(main())
