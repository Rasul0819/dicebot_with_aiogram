from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command,CommandObject
from aiogram.enums.dice_emoji import DiceEmoji
import asyncio,random,time

token = '6746576025:AAHUguDA0Vrp_UQdX5mGCETYhorq5jMpAeU'
bot = Bot(token)

dp = Dispatcher()
@dp.message(Command('start'))
async def start(message:types.Message):
    await message.answer(f"Hello {message.from_user.first_name}")

@dp.message(Command(commands=['rn','random-number']))
async def get_random_number(message:types.Message,command:CommandObject):
    a,b =[int(n) for n in command.args.split('-')]
    rnum = random.randint(a,b)
    await message.reply(f'Random number {rnum}')

@dp.message(F.text=='play')
async def play(message:types.Message):
    xs = await message.answer_dice(DiceEmoji.DICE)
    first= xs.dice.value
    xr = await message.answer_dice(DiceEmoji.DICE)
    second = xr.dice.value
    time.sleep(4)

    if first> second:
        await message.answer('First win')
    else:
        await message.answer('Second win')



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    


