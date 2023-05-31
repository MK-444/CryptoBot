from dotenv import load_dotenv
import os
load_dotenv()
import uuid


uid = uuid.uuid4().hex[:9]


# dictionary = {
#     'btc':{
#         'cryptocurrency': 'BTC',
#         'min_deposit': 0.0001,
#         'fee': 0,
#         'method': 'Bitcoin',
#         'confirm': 3,
#         }
# }
# cryptocurrency = {
#     'btc': 'BTC',
#     'ltc': 'LTC'
# }
    
btc_msg = f"\n\
Вы собираетесь пополнить баланс: BTC \n\
\n\
Min: 0.001 \n\
Комиссия: 0\n\
\n\
Метод: Bitcoin\n\
\n\
⚠️ Внимание\n\
Средства будут зачислены на ваш баланс после 3 подтверждений\
"



msc = f"Ваш 👤 UID: `{uid}`\n\n \
USD: 0\n \
EUR: 0\n \
EUR: 0\n\n \
BTC: 0\n \
LTC: 0\n \
ETH: 0\n \
TRX: 0\n \
XRP: 0\n \
USDT: 0\n \
XMR: 0\n \
BNB: 0\n \
USDC: 0"

start_text = "\nЭто удобный telegram сервис, который всегда под рукой.\n\
\n\
<b>С помощью бота ты можешь:</b>\n\
🦹🏻‍♂️ Получить доступ к услугам без верификации;\n\
💰Безопасно хранить криптовалюты;\n\
🚀Мгновенно и без комиссии отправлять криптовалюты между пользователями;\n\
💵 Покупать/продавать криптовалюты за наличные;\n\
💱Обменивать валюты с минимальным процентом;\n\
📤Выводить криптовалюту на другие сервисы и криптокошельки.\n\
\n\
Пользуясь сервисом ты соглашаешься с правилами 📖\n\
https://telegra.ph/Pravila-polzovaniya-08-17"



deposit_price = "Вы собираетесь пополнить баланс: TRX\n\
\n\
Min: 1 TRX\n\
Комиссия: Бесплатно\n\
\n\
Метод: Tron\n\
\n\
⚠️ Внимание\n\
Средства будут зачислены на ваш баланс после 19 подтверждений\n"


online_banking = f"Вы собираетесь пополнить баланс: USD\n\
\n\
Min: 2 500 Kč\n\
Комиссия: Бесплатно\n\
\n\
Метод: Банковский перевод в рамках Чехии\n\
Отправить на банковский счет: {os.environ.get('CZK_WALLET')} \n\
Variablilni symbol: {uid}\n\
\n\
⚠️ Внимание\n\
Средства будут зачислены на ваш баланс после 4 подтверждений\n"


online_banking_withdraw = f"Вы собираетесь вывести баланс: USD\n\
\n\
Min: 2 500 Kč\n\
Комиссия: Бесплатно\n\
\n\
Метод: Банковский перевод в рамках Чехии\n\
\n\
⚠️ Внимание\n\
Средства будут зачислены на ваш баланс после 4 подтверждений\n"

history = "История Обменов\n\
\n\
Страница: 1/1\n\
\n\
Статус:\n\
🔵 - Открыт\n\
🌀 - Обрабатывается\n\
✅ - Успешно\n\
❌ - Ошибка/Отмена\n\
🔆 - Другое\n\
"


regeral = "🤝 Реферальная программа\n\
Приглашайте новых пользователей и зарабатывайте!\n\
\n\
Мы платим Вам процент от прибыли сервиса за операции, которые совершают привлеченные Вами клиенты.\n"



usd_get = "Введите сумму (Вы получите):\n\
\n\
Min: 100 USD\n\
\n\
Комиссия: 1 % "


czk_give = "Введите сумму (Вы отдаёте):\n\
\n\
Min: 2 500 Kč\n\
\n\
Комиссия: 1 % "


btc = f"BTC Депозит адрес\n\
`{os.environ.get('BTC_ADDRESS')}`\n\
\n\
_Чтобы скопировать кошелек — нажмите на него_"


usd = "Выберите валюту, которую хотите отдать"



settings =f"Ваш 👤 UID: `{uid}`\n\
\n\
Настройки"

info = f"Ваш 👤 UID: `{uid}`\n\
\n\
ℹ️ Инфо"



nalichka = "Город: *Прага*\n\
Свяжитесь с администратором:\n\
email: `maxkostenko18@gmail.com`\n\
phone: `+420774094930`"




twofactory = f"Двухфакторная аутентификация:\n\
\n\
Статус: Отключена 🔴\n\
\n\
Двухфакторная аутентификация (2FA) — это дополнительный уровень защиты вашего аккаунта при помощи кода, известного только вам. Детальнее о 2FA можно прочесть тут\n\
\n\
Вы можете добавить 2FA на вашем аккаунте, нажав кнопку ниже ⬇️\n\
"


"""
вариабильный символ 
высвечивается сумма перевода 
комментарий к платежу - должно ваш айди аккаунта и имя фамилия"""



fee_deposit = \
" Tether (USDT ERC20) = 0\n\
USD COIN (USDC ERC20) = 0\n\
AAVE TOKEN (AAVE) ERC20 = 0 \n\
APE - (ApeCoin, ERC20) = 0\n\
Bitcoin (BTC) = 0\n\
COMP - Compound, ERC20 = 0\n\
CRV - Curve DAO Token ERC20 = 0\n\
DAI $ (DAI) (ERC20) = 0\n\
Dogecoin (Doge) = 0\n\
Ethereum = 0\n\
Ethereum Classic #1 = 0\n\
Gala = 0\n\
CHZ - chiliZ = 0\n\
LINK, CHAIN LINK ERC20 = 0\n\
Litecoin (LTC) = 0\n\
Near Protocol ERC20 = 0\n\
Pax DollarUSDP = 0\n\
SNX (Synthetix ,ERC20) = 0\n\
SUSHI - SushiToken, ERC20 = 0\n\
UNI - Uniswap ERC20 = 0\n\
USDC USD COIN ERC2O = 0\n\
WBTC - Wrapped BTC (ERC20) = 0\n\
YFI - yearn finance, ERC20 = 0\n\
"



fee_withdrawal = \
" Tether (USDT ERC20) = 9 USDT\n\
USD COIN (USDC ERC20) = 13 USDC\n\
AAVE TOKEN (AAVE) ERC20 = 0,06 (AAVE)\n\
APE - (ApeCoin, ERC20) = 1,1 Apecoin\n\
Bitcoin (BTC) = 0,0005 BTC\n\
COMP - Compound, ERC20 = 0,14 COMP\n\
CRV - Curve DAO Token ERC20 = 9,29 CRV\n\
DAI $ (DAI) (ERC20) = 15 Dai $\n\
Dogecoin (Doge) = 77,47 DOGE\n\
Ethereum = 0,008 ETH\n\
Ethereum Classic #1 = 0,65 ETH CLASSIC\n\
Gala = 140,88 GALA\n\
CHZ - chiliZ = 49,84 CHZ\n\
LINK, CHAIN LINK ERC20 = 0,978 LINK\n\
Litecoin (LTC) = 0,001 LTC\n\
Near Protocol ERC20 = 3,6645 NEAR\n\
Pax DollarUSDP = 6,046 USDP\n\
SNX (Synthetix ,ERC20) = 3,38 SNX\n\
SUSHI - SushiToken, ERC20 = 4,46 SUSHI\n\
UNI - Uniswap ERC20 = 0,865 UNI\n\
USDC USD COIN ERC2O = 5 USDC\n\
WBTC - Wrapped BTC (ERC20) = 0,0005 WBTC\n\
YFI - yearn finance, ERC20 = 0,00085 YFI\n\
"




referal_msc = "How to join a referral program?\n\
\n\
Our bot now has a passive income function, which includes a referral program: you can invite a friend and get a cash bonus for it.  The MKCRYPTO bot service uses a 3-level referral program (50% of the profit of our service is invested in this bonus program).\n\
\n\
Example:\n\
We pay a bonus for the fact that a person makes an exchange: if the service earned 100 USDT = 100%.  From this amount, for an operation performed by a referral, you will receive:\n\
\n\
 25 USDT (1st level referral);\n\
\n\
15 USDT (2nd level referral);\n\
\n\
 10 USDT (3rd level referral).\n\
\n\
How the referral program works:\n\
\n\
If a person registers using your invitation link, then he will become your referral, and you will receive 25% of the income of the exchange service made by your referral.  This is your first level referral.\n\
\n\
If this person invites someone to the service using his referral link, then he will also have a first-level referral.  The person invited by her will become a second-level referral for you and you will receive 15% of the income from the exchange service made by your referral. In other words, a second-level referral is a user who was invited by your first-level referral.\n\
\n\
By the same analogy, if your second-level referral invites a new user to the service with his link, then this user will become a third-level referral for you and you will receive 10% of the service's income from the exchange made by your referral.\n\
\n\
By creating different referral links, you will also be able to track their performance and statistics through our bot.\n\
\n\
What do you need to do to start a referral program?\n\
\n\
Step 1. Enter the bot, open the Menu, click on the Info tab, and then - Referral program\n\
\n\
 Step 2. To create a personal invitation, click on the button 'My invites' and then 'Create'\n\
\n\
 Step 3. Creating and naming the invite.\n\
\n\
 Step 4. Confirmation of the created invitation.\n\
\n\
 Done!\n\
\n\
 Now with the help of this link you can invite your acquaintances and friends to the bot.\n\
\n\
 💎 To view earnings from your referrals, go to the 'My Statistics' tab.  In this section, you can view general statistics for all invites or for a single invitation.\n\
\n\
 💎 All bonuses will be accumulated until the user clicks the pay button.  After clicking, the entire accumulated amount will be credited to the account in the bot."