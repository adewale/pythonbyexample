+++
slug = "networking"
title = "Networking"
section = "Standard Library"
summary = "Networking code exchanges bytes across explicit protocol boundaries."
doc_path = "/library/socket.html"
expected_output = "b'ping'\nping\n"
+++

Networking code sends and receives bytes. Higher-level HTTP clients hide many details, but the core boundary is still explicit: text must be encoded before sending and decoded after receiving.

This example uses `socket.socketpair()` so it stays local and deterministic in ordinary Python. Real network clients often use `socket.create_connection()` or a higher-level HTTP library, but the same byte boundary applies.

The useful mental model is endpoint plus bytes plus cleanup. A socket connects two endpoints, transfers byte strings, and must be closed when the conversation is finished.

:::program
```python
import socket

left, right = socket.socketpair()
try:
    message = "ping"
    left.sendall(message.encode("utf-8"))
    data = right.recv(16)
    print(data)
    print(data.decode("utf-8"))
finally:
    left.close()
    right.close()
```
:::

:::unsupported
Dynamic Workers do not provide arbitrary low-level sockets, and this app disables Dynamic Worker outbound access.

```python
left, right = socket.socketpair()
left.sendall("ping".encode("utf-8"))
data = right.recv(16)
```
:::

:::cell
Sockets exchange bytes. Encoding and decoding make the boundary between Python text and network data visible.

```python
import socket

left, right = socket.socketpair()
try:
    message = "ping"
    left.sendall(message.encode("utf-8"))
    data = right.recv(16)
    print(data)
    print(data.decode("utf-8"))
finally:
    left.close()
    right.close()
```

```output
b'ping'
ping
```
:::

:::note
- Network protocols move bytes, not Python `str` objects.
- Close real sockets when finished, usually with a context manager or `finally` block.
- Use high-level HTTP libraries for application HTTP unless socket-level control is the lesson.
:::
