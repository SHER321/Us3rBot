 

# By @NGYNY. Kangers keep credits @ANKITH_M

# All in one code.

"""Available Commands:

.tlol

.lol

.heart

.candy

.NIKHIL

.nothappy"""

from telethon import events

import asyncio

from collections import deque

from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"candy"))

async def _(event):

	if event.fwd_from:		return

	deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))

	for _ in range(999):

		await asyncio.sleep(1)

		await event.edit("".join(deq))

		deq.rotate(1)

    

@borg.on(admin_cmd(pattern=r"nothappy"))

async def _(event):

	if event.fwd_from:

		return

	deq = deque(list("😁☹️😁☹️😁☹️😁"))

	for _ in range(999):

		await asyncio.sleep(1)

		await event.edit("".join(deq))

		deq.rotate(1)

@borg.on(admin_cmd(pattern=r"heart"))

async def _(event):

	if event.fwd_from:

		return

	deq = deque(list("❤️🧡💛💚💙💜🖤"))

	for _ in range(999):

		await asyncio.sleep(1)

		await event.edit("".join(deq))

		deq.rotate(1)

    

@borg.on(admin_cmd(pattern=r"tlol"))

async def _(event):

	if event.fwd_from:

		return

	deq = deque(list("🤔🧐🤨🤔🧐🤨"))

	for _ in range(999):

		await asyncio.sleep(1)

		await event.edit("".join(deq))

		deq.rotate(1)

    

@borg.on(admin_cmd(pattern=r"lol"))

async def _(event):

	if event.fwd_from:

		return

	deq = deque(list("😂🤣😂🤣😂🤣"))

	for _ in range(999):

		await asyncio.sleep(1)

		await event.edit("".join(deq))

		deq.rotate(1)

    
    
    
    @borg.on(admin_cmd(pattern=r"NIKHIL"))

async def _(event):

	if event.fwd_from:

		return

	deq = deque(list("😎N😎I😎K😎H😎I😎L😎"))

	for _ in range(999):

		await asyncio.sleep(1)

		await event.edit("".join(deq))

		deq.rotate(1)

    
    
   
