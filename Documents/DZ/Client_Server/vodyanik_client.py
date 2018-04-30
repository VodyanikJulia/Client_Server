import asyncio
import struct
import time
connection=60000
seq_num = 1
while connection>0:
    async def tcp_echo_client(message, loop):
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888,
                                                   loop=loop)

        #print('Send: %r' % message)
        writer.write(message)

        data = await reader.read(100)
        dataf=struct.unpack("!Hd", data)
        #print('Received:', dataf)
        (seq, timestamp) = (dataf)
        #print(timestamp)
        current_time = time.time()
        timediff = current_time - timestamp
        print("seq_number=", seq)
        print("time_diff= ", timediff)

        print('Close the socket')
        writer.close()

    times=time.time()
    message = struct.pack("!Hd", seq_num, times)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(tcp_echo_client(message, loop))

    seq_num +=1
    connection-=1
loop.close()