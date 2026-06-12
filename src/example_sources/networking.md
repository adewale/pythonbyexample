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

:::unsupported
`socketpair()` returns two connected endpoints. `sendall` writes encoded bytes into one end, and `recv` reads up to 16 bytes off the other. The byte boundary is the whole point: `"ping".encode("utf-8")` produces `b'ping'`, which is what the socket actually moves. (The in-browser Run button cannot open sockets — the sandbox disables outbound access — so pressing Run on this page fails; the verified output below comes from a real socket pair under standard CPython at build time.)

```python
left, right = socket.socketpair()
left.sendall("ping".encode("utf-8"))
data = right.recv(16)
```
:::

:::cell
The complete version adds two things: a `try`/`finally` so both endpoints close even if `recv` or the surrounding work raises, and a second `print` that `decode`s the received bytes back into a Python `str` for display. The first `print` shows the raw bytes `b'ping'`; the second shows the decoded text `ping`.

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
- Cloudflare Workers support HTTP-style networking through platform APIs; this example avoids outbound calls so the editable lesson stays deterministic and safe.
:::
