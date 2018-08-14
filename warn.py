def set_warn(bot, update):
	from main import warn_limit_dict,warn_dict

	msg = update.message
	chat_id = msg.chat_id
	user_id = msg.from_user.id
	setter = bot.get_chat_member(chat_id, user_id)['status']
	
	try:
		warn_limit = int(msg.text.split(' ',1)[1].strip())
	except:
		bot.send_message(chat_id = msg.chat_id, 
						 text = "*Format:*\n_/set_\__warn <number>_", 
						 reply_to_message_id=msg.message_id,
						 parse_mode='MARKDOWN')
		
	if setter in ['administrator', 'creator']:
		warn_limit_dict[chat_id] = warn_limit
		bot.send_message(chat_id = msg.chat_id, 
						 text = f"Warns have been set to {warn_limit}", 
						 reply_to_message_id = msg.message_id)

		if chat_id in warn_dict.keys():
			warn_dict[chat_id]={}
	else:
		bot.send_message(chat_id = chat_id,
						 text = "Fuck off.",
						 reply_to_message_id = msg.message_id)

def clear_warns(bot, update):
	from main import warn_limit_dict,warn_dict

	msg = update.message
	chat_id = msg.chat_id
	user_id = msg.from_user.id
	clearer = bot.get_chat_member(chat_id, user_id)['status']

	warned = msg.reply_to_message.from_user.id
	if clearer != 'member':
		if chat_id in warn_dict.keys():

			if warned in warn_dict[chat_id].keys():
				warn_dict[chat_id][warned] = 0
				bot.send_message(chat_id = msg.chat_id, 
								 text = f"Warns cleared for @{msg.reply_to_message.from_user.username}", 
								 reply_to_message_id = msg.message_id)
			else:
				bot.send_message(chat_id=msg.chat_id, 
								 text = "The number of warns of this person is already 0.", 
								 reply_to_message_id = msg.message_id)

def check_warn(bot, update, warned_id):
	from main import warn_dict, warn_limit_dict
	chat_id = update.message.chat_id
	if chat_id not in warn_limit_dict.keys():
			warn_limit_dict[chat_id] = 3

	if chat_id not in warn_dict.keys():
		warn_dict[chat_id] = {}

	if warned_id not in warn_dict[chat_id].keys():
		warn_dict[chat_id][warned_id] = 1
	else:
		warn_dict[chat_id][warned_id] += 1

	if warn_dict[chat_id][warned_id] >= warn_limit_dict[chat_id]:
		warn_limit = warn_limit_dict[chat_id]
		try:
			bot.kick_chat_member(chat_id, warned_id)
			text = f"Max warns {warn_limit}/{warn_limit} reached, user banned."
			del warn_dict[chat_id][warned_id]
			return text

		except:
			warn_dict[chat_id][warned_id] -= 1
			text="Couldn't kick, either I'm not an admin or the other user is."
			return text

	else:
		text = f"Warns : {warn_dict[chat_id][warned_id]}/{warn_limit_dict[chat_id]} reached."
		return text

def warn(bot, update):
	from chats_data import chats_data
	msg = update.message
	chat_id = msg.chat_id
	
	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('warn', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /warn plugin is disabled. You can enable it using `/enable warn` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	from main import warn_dict, warn_limit_dict

	warned_id = msg.reply_to_message and msg.reply_to_message.from_user.id

	warner = bot.get_chat_member(chat_id, msg.from_user.id)['status']
	warned = warned_id and bot.get_chat_member(chat_id, warned_id)['status']

	# print(f'{warner} is warning {warned}')

	if warner in ['administrator', 'creator']:
		if not warned:
			bot.send_message(chat_id = msg.chat_id, 
							 text = "Reply to the user that you want to warn.", 
							 reply_to_message_id = msg.message_id)

		if warned_id == msg.from_user.id:
			bot.send_message(chat_id = msg.chat_id, 
							 text = "You cannot warn yourself.", 
							 reply_to_message_id = msg.message_id)

		elif warned in ['administrator', 'creator']:
			bot.send_message(chat_id = msg.chat_id, 
							 text = "I wish I could warn admins...",
							 reply_to_message_id = msg.message_id)

		elif warned == 'left':
			bot.send_message(chat_id = chat_id,
							 text = "Can't warn user, they already left.",
							 reply_to_message_id = msg.message_id)

		elif warned == 'kicked':
			bot.send_message(chat_id = chat_id,
							 text = "Can't warn user, I already kicked them.",
							 reply_to_message_id = msg.message_id)

		elif warned == 'member':
			text = msg.text.strip().split(" ",1)
			if len(text) > 1:
				warn_text = check_warn(bot, update, warned_id)
				bot.send_message(chat_id = chat_id, text = f"{warn_text}\n_Reason:_ _{text[1]}_", parse_mode="Markdown", reply_to_message_id = msg.reply_to_message.message_id)
			else:
				text = check_warn(bot, update, warned_id)
				bot.send_message(chat_id = chat_id, text = text, reply_to_message_id = msg.reply_to_message.message_id)

	elif warner not in ['creator', 'administrator']:
		bot.send_message(chat_id = chat_id,
						 text = "Fuck off.",
						 reply_to_message_id = msg.message_id)
