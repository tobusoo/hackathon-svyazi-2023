from telethon import TelegramClient, sync

#print('Для работы с этим приложением требуется клиент телеграма.')
#print('Для создания клиента телеграмма:')
#print(' 1) авторизуйстесь на https://my.telegram.org')
#print(' 2) перейдите https://my.telegram.org/apps')
#print(' 3) Заполните поля App title и Short name, нажимаем «Create application»')
#print(' 4) сохраните api_id и api_hash. они в дальнейшем пригодятся\n')

#api_id= input ('введите api_id: ')
#api_hash= input ('введите api_hash: ')

api_id = 20343413
api_hash = '5ac3d169381320ca0befa82dd98400b1'

client = TelegramClient('session_name', api_id, api_hash)

isShowDialogs= 'y' #хотите посмотреть ваши диалоги? (y/n)
chatName= -1001560117464 #введите id чата/канала, в котором вы хотите найти сообщения
isShowUsers= 'y' #хотите посмотреть список участников диалога? (y/n)
userName= 'me' #введите имя пользователя, чьи сообщения вы хотите найти

client.start()

dialogs = client.get_dialogs() # диалоги пользователей

if isShowDialogs== 'y': # вывод диалогов пользователя
	for dialog in dialogs:
		print(dialog.title)

# проверить находится ли дтиалог в подписках у пользователя
for i in range(len(dialogs)):
	if dialogs[i] == chatName:
		break

isJoin= 0 # 0- вступление не требуется 1- требуется 2- канал не существует
if i+1 == len(dialogs):
	# нет - добавить его в этот диалог
	from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
	try:
		client(JoinChannelRequest(chatName))
	except ValueError:
		# ошибка добавления - вывести ошибку и завершить программу
		print('канала с таким id не существует')
		client.disconnect()
		raise SystemExit(1) # завершение программы

# вывести участников

#participants = client.get_participants(chatName)
#print(participants)

messages= client.iter_messages(chatName)

for message in messages: #, from_user= 'me'):
	print()
	print(message.date)
	print(message.text)
client(LeaveChannelRequest(chatName))
client.disconnect()
