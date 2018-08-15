def welcome(bot, update, user_data):
	from main import start_dict
	from chats_data import chats_data
	chat_id = update.message.chat_id

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('welcome', None):
		return


	reply_markup=[]

	msg = update.message
	if msg.new_chat_members:
		user_name = msg.new_chat_members[0]['username']
		if "_" in user_name:
			user_name = user_name.replace("_","\_")

		if chat_id in start_dict.keys():
			if 'rules' in start_dict[chat_id].keys():
				from telegram import InlineKeyboardMarkup, InlineKeyboardButton

				reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Rules", url = f't.me/toilet_evergarden_bot?start=rules_{chat_id}')]])

		if chat_id in start_dict.keys():
			if 'welcome' in start_dict[chat_id].keys():
				text = start_dict[chat_id]['welcome']
				sent_message = bot.send_message(chat_id = msg.chat_id, 
						 text = text, 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown', reply_markup = reply_markup)
			else:
				sent_message = bot.send_message(chat_id = msg.chat_id, 
						 text = f"@{user_name} Okairi motherfucker", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown', reply_markup = reply_markup)
		else:
			sent_message = bot.send_message(chat_id = msg.chat_id, 
						 text = f"@{user_name} Okairi motherfucker", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown', reply_markup = reply_markup)

def set_rule(bot, update):
	from chats_data import chats_data
	msg = update.message
	chat_id = update.message.chat_id

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('rules', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /setrules plugin is disabled. You can enable it using `/enable rules` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	from main import start_dict

	setter = bot.get_chat_member(chat_id, msg.from_user.id)['status']

	if setter in ["administrator","creator"]:
		text = msg.text.split("\n", 1)
		if len(text)>1:
			text = text[1]
			if chat_id not in start_dict.keys():
				start_dict[chat_id] = {}
				start_dict[chat_id]['rules'] = text
			else:
				start_dict[chat_id]['rules'] = text
			bot.send_message(chat_id = msg.chat_id, 
						 text = "Rules added!", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		else:
			bot.send_message(chat_id = msg.chat_id, 
						 text = "*Format:*\n/setrules\n_rule 1\nrule 2_", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
	else:
		bot.send_message(chat_id = msg.chat_id, 
						 text = "Fuck off, you aren't admin.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')

def set_welcome(bot, update):
	from main import start_dict
	from chats_data import chats_data

	msg = update.message
	chat_id = update.message.chat_id

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('welcome', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /setwelcome plugin is disabled. You can enable it using `/enable rules` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	setter = bot.get_chat_member(chat_id, msg.from_user.id)['status']

	if setter in ["administrator","creator"]:
		text = msg.text.split(" ", 1)
		if len(text)>1:
			text = text[1]
			if chat_id not in start_dict.keys():
				start_dict[chat_id] = {}
				start_dict[chat_id]['welcome'] = text
			else:
				start_dict[chat_id]['welcome'] = text
			bot.send_message(chat_id = msg.chat_id, 
						 text = "Welcome message added added!", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		else:
			bot.send_message(chat_id = msg.chat_id, 
						 text = "*Format:*\n/setwelcome _welcome message_", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
	else:
		bot.send_message(chat_id = msg.chat_id, 
						 text = "Fuck off, you aren't admin.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')


