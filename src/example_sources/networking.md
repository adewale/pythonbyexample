+++
slug = "networking"
title = "Networking"
section = "Standard Library"
summary = "Networking code exchanges bytes across explicit protocol boundaries."
doc_path = "/library/socket.html"
see_also = [
  "bytes-and-bytearray",
  "subprocesses",
  "async-await",
]
expected_output = "b'ping'\nping\n"
+++

Networking code sends and receives bytes across protocol boundaries. Higher-level HTTP clients hide many details, but the core rule remains: text is encoded before it leaves the process and decoded after bytes come back.

In standard Python, the socket version of this lesson uses connected endpoints such as `socket.create_connection()` or, for a local deterministic demonstration, `socket.socketpair()`. This site's live example runner does not expose arbitrary OS sockets or outbound calls, so this page teaches the socket contract while making the runner constraint explicit.

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

:::cell
`socketpair()` returns two connected endpoints. `sendall` writes encoded bytes into one end and `recv` reads up to 16 bytes off the other — the byte boundary is the whole point: `"ping".encode("utf-8")` produces `b'ping'`, which is what the socket actually moves. The `try`/`finally` closes both endpoints even if `recv` raises, and the second `print` `decode`s the bytes back into a Python `str`. The in-browser sandbox cannot open sockets, so pressing Run here fails; this output came from a real socket pair under standard CPython at build time.

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
- The verified output came from a real `socketpair()` under standard CPython at build time; the in-browser sandbox cannot open sockets, so live runs of this page fail there.
:::
