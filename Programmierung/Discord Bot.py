import discord
import random
from discord.ext import commands

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Define pre-saved dice options
dice_options = {
    'd6': 6,
    'd10': 10,
    'd20': 20
}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='roll', help='Roll custom or predefined dice. Example: !roll 2d6+3 or !roll d10')
async def roll_dice(ctx, dice_notation: str):
    try:
        if dice_notation.lower() in dice_options:
            result = roll_predefined(dice_notation.lower())
        else:
            result = roll_custom(dice_notation)
            
        await ctx.send(f'Rolling {dice_notation}: {result}')
    except Exception as e:
        await ctx.send(f'Error: {str(e)}')

def roll_custom(dice_notation):
    parts = dice_notation.split('d')
    num_rolls = int(parts[0]) if parts[0] else 1

    if '+' in parts[1]:
        dice_info, modifier = parts[1].split('+')
    elif '-' in parts[1]:
        dice_info, modifier = parts[1].split('-')
        modifier = -int(modifier)
    else:
        dice_info = parts[1]
        modifier = 0

    dice_info = dice_info.split('s')
    if len(dice_info) == 2:
        num_sides, sides = int(dice_info[0]), dice_info[1]
    else:
        num_sides, sides = 1, dice_info[0]

    rolls = [random.choice(list(sides)) for _ in range(num_rolls)]
    result = ', '.join(map(str, rolls))
    total = sum(map(int, rolls)) + modifier

    return f'{result} + {modifier} = {total}'

def roll_predefined(dice_name):
    dice = dice_options[dice_name]
    result = random.randint(1, dice)
    return f'Rolled a {dice}-sided die: {result}'

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')
### Generated Using Chat GPT
