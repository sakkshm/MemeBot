import telegram

my_token = '#####################'
my_chat_id = '*****'

def send(msg, chat_id = my_chat_id, token=my_token):
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)

def sendImg(path, chat_id = my_chat_id, token=my_token):
	bot = telegram.Bot(token=token)
	bot.send_photo(chat_id=chat_id, photo=open(path, 'rb'))
