import aiohttp
import asyncio
import json
from lxml import html

class ZaraScanner:
    def __init__(self, username, site_data):
        self.username = username
        self.site_data = site_data
        self.results = {}

    async def fetch(self, session, site, info):
        url = info["url"].format(self.username)
        try:
            async with session.get(url, timeout=10) as response:
                text = await response.text()
                exists = info["exists"] in text
                avatar, activity = None, None

                if exists:
                    tree = html.fromstring(text)
                    if info.get("avatar_xpath"):
                        avatar = tree.xpath(info["avatar_xpath"])
                        avatar = avatar[0] if avatar else None
                    if info.get("activity_xpath"):
                        activity = tree.xpath(info["activity_xpath"])
                        activity = activity[0] if activity else None

                self.results[site] = {
                    "url": url,
                    "exists": exists,
                    "avatar": avatar,
                    "activity": activity
                }
        except Exception as e:
            self.results[site] = {
                "url": url,
                "error": str(e)
            }

    async def run(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, site, info) for site, info in self.site_data.items()]
            await asyncio.gather(*tasks)
        return self.results
