def load_database():
	from pickle import load
	chats_dict = {}
	chats_db = open('chats.db', 'rb')
	try:
		chats_dict = load(chats_db)
		if chats_dict:
			global chats_data
			chats_data = chats_dict
	except:
		pass
	chats_db.close()
	return chats_data