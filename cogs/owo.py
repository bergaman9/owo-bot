import discord
from discord.ext import commands, tasks

from asyncio import sleep
from random import randint

import requests
import random, os
import dotenv
dotenv.load_dotenv()

class OwO(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.won = None
        self.amount = 100
        self.earned = 0
        self.channel_id = os.getenv("CHANNEL_ID")
        self.owo_loop.start()

    headers = {
        "authorization": os.getenv("AUTH"),
    }

    def create_payload(self):
        choice = random.choice(["head", "tail"])
        return {
            "content": f"owo coinflip {choice} {self.amount}"
        }

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.author.id == 408785106942164992:  # owo botunun Discord ID'si
            if "and you won" in after.content.lower():  # Kazandıysak
                self.won = True
                self.amount += 50
                self.earned += self.amount * 2  # amount'un 2 katını ekleyin
            elif "and you lost it all..." in after.content.lower():  # Kaybettiysek
                self.won = False
                if self.amount > 50:
                    self.amount -= 50
                self.earned -= self.amount  # amount'un 2 katını çıkarın

    @tasks.loop(seconds=1)
    async def owo_loop(self):
        await self.bot.wait_until_ready()
        print(f"Kazanma Durumu: {self.won}, Toplam Kazanç: {self.earned}")  # Toplam kazanç veya kaybı yazdır
        payload = self.create_payload()
        requests.post(f"https://discord.com/api/v9/channels/{self.channel_id}/messages", headers=self.headers, json=payload)

        random_seconds = randint(20, 40)  # Örneğin, 20 ile 40 saniye arasında rastgele bir zaman seç
        print(f"{random_seconds} saniye sonra yeni komut çalıştırılacak.")
        await sleep(random_seconds)  # Seçilen süre kadar bekler

async def setup(bot):
    await bot.add_cog(OwO(bot))