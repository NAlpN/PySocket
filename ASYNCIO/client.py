import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f"Istemci olarak sunucuya mesaj gönderiliyor: {message!r}")
    writer.write(message.encode())

    data = await reader.read(100)
    print(f"Sunucudan yanıt alındı: {data.decode()!r}")

    print("Bağlantı kapatılıyor")
    writer.close()
    await writer.wait_closed()

mesaj = input("Mesajınız: ")
asyncio.run(tcp_echo_client(mesaj))