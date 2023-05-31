from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("menu ", "Main menu"),
            types.BotCommand("help", "If you're lost"),
            types.BotCommand("start", "Start "),
            types.BotCommand("wallet", "Your Balances. Deposit/Withdrawal"),
            types.BotCommand("swap", "Converting internal balances"),
            types.BotCommand("settings", "Settings"),
            types.BotCommand("info", "Feedback(Support), Fees")
        ]
    )
