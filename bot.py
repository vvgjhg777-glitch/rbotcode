"""
███████╗██╗  ██╗ █████╗ ███████╗ ██████╗ ██╗    ██╗ ██████╗ ██████╗ ██████╗ ██████╗ 
██╔════╝██║  ██║██╔══██╗██╔════╝██╔═══██╗██║    ██║██╔════╝██╔═══██╗██╔══██╗██╔══██╗
███████╗███████║███████║██║     ██║   ██║██║ █╗ ██║██║     ██║   ██║██████╔╝██████╔╝
╚════██║██╔══██║██╔══██║██║     ██║   ██║██║███╗██║██║     ██║   ██║██╔══██╗██╔═══╝ 
███████║██║  ██║██║  ██║███████╗╚██████╔╝╚███╔███╔╝╚██████╗╚██████╔╝██║  ██║██║     
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     

COMMANDES: !code (tout se passe en MP ensuite)
"""

import discord
from discord.ext import commands
import asyncio
import random
import string
import json
import os
from datetime import datetime

ACCOUNTS_FILE = 'accounts.json'

def create_accounts():
    accounts = [
        {"email": "elite1@shadowcorp.net", "password": "Shadow!2024#VIP", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite2@shadowcorp.net", "password": "Cyber@Access99", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite3@shadowcorp.net", "password": "Matrix#Secure77", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite4@shadowcorp.net", "password": "Phantom$Pass88", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite5@shadowcorp.net", "password": "Ghost!Entry55", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite6@shadowcorp.net", "password": "Nexus@Code2024", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite7@shadowcorp.net", "password": "Titan#Key777", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite8@shadowcorp.net", "password": "Omega$Access", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite9@shadowcorp.net", "password": "Vortex!Pass99", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite10@shadowcorp.net", "password": "Zenith@2024", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite11@shadowcorp.net", "password": "Alpha#Secure11", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite12@shadowcorp.net", "password": "Beta@Pass2024", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite13@shadowcorp.net", "password": "Gamma!Code13", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite14@shadowcorp.net", "password": "Delta$Key14", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite15@shadowcorp.net", "password": "Epsilon#15", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite16@shadowcorp.net", "password": "Zeta@Pass16", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite17@shadowcorp.net", "password": "Eta!Secure17", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite18@shadowcorp.net", "password": "Theta$Code18", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite19@shadowcorp.net", "password": "Iota#Key19", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite20@shadowcorp.net", "password": "Kappa@2024", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite21@shadowcorp.net", "password": "Lambda!Pass21", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite22@shadowcorp.net", "password": "Mu$Secure22", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite23@shadowcorp.net", "password": "Nu#Code23", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite24@shadowcorp.net", "password": "Xi@Key24", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite25@shadowcorp.net", "password": "Omicron!25", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite26@shadowcorp.net", "password": "Pi$Pass26", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite27@shadowcorp.net", "password": "Rho#Secure27", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite28@shadowcorp.net", "password": "Sigma@Code28", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite29@shadowcorp.net", "password": "Tau!Key29", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite30@shadowcorp.net", "password": "Upsilon$30", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite31@shadowcorp.net", "password": "Phi#Pass31", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite32@shadowcorp.net", "password": "Chi@Secure32", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite33@shadowcorp.net", "password": "Psi!Code33", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite34@shadowcorp.net", "password": "Omega$Key34", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite35@shadowcorp.net", "password": "Nova#2024", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite36@shadowcorp.net", "password": "Stellar@Pass36", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite37@shadowcorp.net", "password": "Cosmic!Sec37", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite38@shadowcorp.net", "password": "Lunar$Code38", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite39@shadowcorp.net", "password": "Solar#Key39", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite40@shadowcorp.net", "password": "Nebula@2024", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite41@shadowcorp.net", "password": "Quasar!Pass41", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite42@shadowcorp.net", "password": "Pulsar$Sec42", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite43@shadowcorp.net", "password": "Orbit#Code43", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite44@shadowcorp.net", "password": "Galaxy@Key44", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite45@shadowcorp.net", "password": "Comet!2024", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite46@shadowcorp.net", "password": "Meteor$Pass46", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite47@shadowcorp.net", "password": "Asteroid#47", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite48@shadowcorp.net", "password": "Planet@Sec48", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite49@shadowcorp.net", "password": "Saturn!Code49", "url": "https://cosmo-digital-bank.base44.app/"},
        {"email": "elite50@shadowcorp.net", "password": "Jupiter$Key50", "url": "https://cosmo-digital-bank.base44.app/"}
    ]
    with open(ACCOUNTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(accounts, f, indent=4, ensure_ascii=False)
    return accounts

def load_accounts():
    # TOUJOURS créer les nouveaux comptes au démarrage
    return create_accounts()

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(accounts, f, indent=4, ensure_ascii=False)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
active_codes = {}

def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

async def loading_bar(channel, text):
    frames = [
        "```diff\n+ [▰▱▱▱▱▱▱▱▱▱] 10%  > Initializing secure connection...\n```",
        "```diff\n+ [▰▰▱▱▱▱▱▱▱▱] 20%  > Encrypting communication channel...\n```",
        "```diff\n+ [▰▰▰▱▱▱▱▱▱▱] 30%  > Establishing quantum tunnel...\n```",
        "```diff\n+ [▰▰▰▰▱▱▱▱▱▱] 40%  > Verifying biometric signatures...\n```",
        "```diff\n+ [▰▰▰▰▰▱▱▱▱▱] 50%  > Building secure protocol...\n```",
        "```diff\n+ [▰▰▰▰▰▰▱▱▱▱] 60%  > Bypassing security layers...\n```",
        "```diff\n+ [▰▰▰▰▰▰▰▱▱▱] 70%  > Synchronizing blockchain data...\n```",
        "```diff\n+ [▰▰▰▰▰▰▰▰▱▱] 80%  > Activating stealth mode...\n```",
        "```diff\n+ [▰▰▰▰▰▰▰▰▰▱] 90%  > Finalizing access protocol...\n```",
        "```diff\n+ [▰▰▰▰▰▰▰▰▰▰] 100% > COMPLETE!\n```"
    ]
    msg = await channel.send(f"**{text}**\n{frames[0]}")
    for frame in frames[1:]:
        await asyncio.sleep(3.0)  # 30 secondes au total (10 frames x 3 secondes)
        await msg.edit(content=f"**{text}**\n{frame}")
    return msg

def terminal_lines():
    lines = [
        ">>> [SHADOWCORP] Establishing encrypted tunnel to mainframe...",
        ">>> [CRYPTO] AES-256 quantum encryption activated... SUCCESS",
        ">>> [AUTH] Multi-factor authentication validated... SUCCESS",
        ">>> [NETWORK] Bypassing firewall layers [1/12]...[12/12] COMPLETE",
        ">>> [DATABASE] Accessing distributed ledger... Decryption in progress...",
        ">>> [SECURITY] Running deep pattern analysis... NO THREATS DETECTED",
        ">>> [VPN] Routing through 24 anonymous proxies... SUCCESS",
        ">>> [BLOCKCHAIN] Verifying cryptographic signatures... VALIDATED",
        ">>> [AI] Neural network authentication passed... SUCCESS",
        ">>> [QUANTUM] Quantum-resistant encryption layer active... MAXIMUM SECURITY",
        ">>> [STEALTH] Ghost protocol activated... INVISIBLE MODE ON",
        ">>> [FINAL] All systems operational... GRANTING ACCESS"
    ]
    return random.sample(lines, 10)

@bot.event
async def on_ready():
    print("\n" + "="*75)
    print("███████╗██╗  ██╗ █████╗ ███████╗ ██████╗ ██╗    ██╗")
    print("██╔════╝██║  ██║██╔══██╗██╔════╝██╔═══██╗██║    ██║")
    print("███████╗███████║███████║██║     ██║   ██║██║ █╗ ██║")
    print("╚════██║██╔══██║██╔══██║██║     ██║   ██║██║███╗██║")
    print("███████║██║  ██║██║  ██║███████╗╚██████╔╝╚███╔███╔╝")
    print("╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚══╝╚══╝")
    print("="*75)
    print(f'[+] BOT OPERATIONNEL: {bot.user}')
    print(f'[+] SERVEURS ACTIFS: {len(bot.guilds)}')
    print(f'[+] COMPTES DISPONIBLES: {len(load_accounts())}')
    print(f'[+] SYSTEME: PRET')
    print("="*75 + "\n")

@bot.command(name='code')
async def get_code(ctx):
    accounts = load_accounts()
    if not accounts:
        await ctx.send("```diff\n- ERREUR: Aucun compte disponible```")
        return
    
    code = generate_code()
    selected_account = random.choice(accounts)
    active_codes[ctx.author.id] = {
        'code': code, 
        'account': selected_account, 
        'step': 0,
        'used': False
    }
    
    # Message public simple
    embed = discord.Embed(title="SHADOWCORP PROTOCOL", color=0x00ff41)
    embed.description = "```Consultez vos messages prives```"
    await ctx.send(embed=embed)
    
    # TOUT EN MP MAINTENANT
    try:
        dm = await ctx.author.create_dm()
        
        # Animation
        await loading_bar(dm, "GENERATION CODE D'ACCES")
        await asyncio.sleep(1)
        
        # Message avec code
        code_embed = discord.Embed(title="CODE D'ACCES GENERE", color=0x00ff41)
        code_embed.description = f"""```ansi
\x1b[32m╔══════════════════════════════════════════════════╗
║                                                  ║
║              ACCES AUTORISE                      ║
║                                                  ║
╚══════════════════════════════════════════════════╝\x1b[0m

\x1b[33m>> VOTRE CODE PERSONNEL:\x1b[0m
\x1b[32m{code}\x1b[0m

\x1b[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[0m
```"""
        code_embed.add_field(
            name="PROCHAINE ETAPE",
            value="```Pour continuer, tapez:\n\n!continuer CODE\n\n(Remplacez CODE par votre code ci-dessus)```",
            inline=False
        )
        code_embed.set_footer(text="ShadowCorp Encrypted Channel")
        await dm.send(embed=code_embed)
        
    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention} ```Impossible d'envoyer des MP. Activez vos messages prives.```")

@bot.command(name='continuer')
async def continuer(ctx, user_code: str = None):
    # Vérifier si c'est en DM
    if not isinstance(ctx.channel, discord.DMChannel):
        return
    
    user_data = active_codes.get(ctx.author.id)
    if not user_data:
        await ctx.send("```diff\n- SESSION INEXISTANTE\n- Utilisez d'abord: !code```")
        return
    
    if user_data['used']:
        await ctx.send("```diff\n- CODE DEJA UTILISE```")
        return
    
    step = user_data['step']
    
    # ETAPE 0: Vérifier le code
    if step == 0:
        if not user_code or user_code.upper() != user_data['code']:
            await ctx.send("```diff\n- CODE INVALIDE\n- Verifiez votre code et reessayez```")
            return
        
        # Animation terminale spectaculaire
        initial = await ctx.send("```ansi\n\x1b[33m>>> INITIALISATION SYSTEME SHADOWCORP <<<\x1b[0m\n```")
        await asyncio.sleep(1)
        
        terminal = """```ansi
\x1b[32m╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║              SHADOWCORP ACCESS TERMINAL                        ║
║                                                                ║
║                  [CLEARANCE ULTRA SECURISEE]                   ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝\x1b[0m

\x1b[36m━━━━━━━━━━━━━━━━━ SEQUENCE D'AUTHENTIFICATION ━━━━━━━━━━━━━━━━\x1b[0m

"""
        await initial.edit(content=terminal + "```")
        await asyncio.sleep(0.8)
        
        code_lines = terminal_lines()
        for i, line in enumerate(code_lines, 1):
            terminal += f"\x1b[36m[{i:02d}/{len(code_lines):02d}]\x1b[0m {line}\n"
            await initial.edit(content=terminal + "```")
            await asyncio.sleep(0.7)
        
        terminal += """
\x1b[32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[0m

\x1b[32m>>> VERIFICATION REUSSIE <<<\x1b[0m
\x1b[32m>>> AUTHENTIFICATION VALIDEE <<<\x1b[0m
\x1b[32m>>> ACCES EN COURS DE PREPARATION <<<\x1b[0m

\x1b[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[0m
```"""
        await initial.edit(content=terminal)
        await asyncio.sleep(2)
        
        user_data['step'] = 1
        
        confirm_embed = discord.Embed(title="CONFIRMATION REQUISE", color=0xffaa00)
        confirm_embed.description = """```ansi
\x1b[33m╔════════════════════════════════════════════════════╗
║                                                    ║
║         VOULEZ-VOUS VRAIMENT CONTINUER ?           ║
║                                                    ║
╚════════════════════════════════════════════════════╝\x1b[0m

\x1b[36mCette action va declencher le processus\x1b[0m
\x1b[36md'attribution des identifiants.\x1b[0m
```"""
        confirm_embed.add_field(name="POUR CONTINUER", value="```Tapez: !continuer```", inline=False)
        await ctx.send(embed=confirm_embed)
        return
    
    # ETAPE 1-2: Confirmations réduites
    if step in [1, 2]:
        messages = [
            "```ansi\n\x1b[33m[VERIFICATION] Confirmez-vous votre decision ?\x1b[0m\n```",
            "```ansi\n\x1b[32m[FINAL] Preparation des identifiants...\nDernier !continuer pour recevoir l'acces complet.\x1b[0m\n```"
        ]
        
        await ctx.send(messages[step - 1])
        
        if step < 2:
            await ctx.send("```Pour continuer: !continuer```")
        
        user_data['step'] += 1
        return
    
    # ETAPE 3: Donner les identifiants
    if step == 3:
        account = user_data['account']
        
        # Animation finale
        final_loading = await ctx.send("```ansi\n\x1b[36m>>> EXTRACTION DES IDENTIFIANTS EN COURS...\x1b[0m\n```")
        await asyncio.sleep(2)
        
        # Message final avec identifiants
        final_embed = discord.Embed(title="IDENTIFIANTS D'ACCES", color=0x00ff41)
        final_embed.description = """```ansi
\x1b[32m╔════════════════════════════════════════════════════════╗
║                                                        ║
║              VOICI VOS IDENTIFIANTS                    ║
║                                                        ║
╚════════════════════════════════════════════════════════╝\x1b[0m
```"""
        final_embed.add_field(name="EMAIL", value=f"```{account['email']}```", inline=False)
        final_embed.add_field(name="MOT DE PASSE", value=f"```{account['password']}```", inline=False)
        final_embed.add_field(name="LIEN D'ACCES", value=f"[>>> CLIQUEZ ICI <<<]({account['url']})", inline=False)
        final_embed.add_field(
            name="",
            value="```Profitez bien.```",
            inline=False
        )
        final_embed.set_footer(text="ShadowCorp | Transmission complete")
        final_embed.timestamp = datetime.utcnow()
        await ctx.send(embed=final_embed)
        
        # Nettoyer
        user_data['used'] = True
        accounts = load_accounts()
        accounts.remove(account)
        save_accounts(accounts)
        print(f"[+] [{datetime.now().strftime('%H:%M:%S')}] Compte attribue a {ctx.author} | Restants: {len(accounts)}")

@bot.command(name='stats')
@commands.has_permissions(administrator=True)
async def stats(ctx):
    accounts = load_accounts()
    await ctx.send(f"```Comptes: {len(accounts)} | Codes actifs: {len(active_codes)}```")

@bot.command(name='guide')
async def guide(ctx):
    guide_embed = discord.Embed(title="GUIDE SHADOWCORP", color=0x00ff41)
    guide_embed.add_field(name="1. DEMANDER UN CODE", value="```!code```", inline=False)
    guide_embed.add_field(name="2. VALIDER", value="```!continuer VOTRE_CODE```", inline=False)
    guide_embed.add_field(name="3. CONFIRMER", value="```!continuer (plusieurs fois)```", inline=False)
    await ctx.send(embed=guide_embed)

if __name__ == "__main__":
    print("\n" + "="*75)
    print("[+] SHADOWCORP BOT - DEMARRAGE")
    print("="*75 + "\n")
    
    try:
        TOKEN = 'MTQ3MjIzNjQ3MDAyMTY1MjY3Ng.G0WJml.WtYPSxbXRXONtik79gMEkMVDi3BJnma3L-a_JE'
        print("[+] Connexion a Discord...\n")
        bot.run(TOKEN)
    except KeyboardInterrupt:
        print("\n[!] Bot arrete.")
    except Exception as e:
        print(f"\n[!] ERREUR: {e}")
