db = list()
with open('list.txt', 'r') as filehandle:
	for line in filehandle:
		dbline = line[:-1]
		db.append(dbline)

print('Welcome to my Databaser')
while True:
	y = input('would you like to read, write, delete or exit? ')

	if y == 'read':
		with open('list.txt', 'r') as filehandle:
			db = []
			for line in filehandle:
				dbline = line[:-1]
				db.append(dbline)
		try:
			z = int(input('please pick an entry number: '))
			try:
				print(db[z - 1])
			except:
				print('entry number not found!')
		except:
			print('Thats not a number!')

	elif y == 'write':
		z = input('state an entry: ')+"\n"
		db.append(z)
		with open('list.txt', 'a') as filehandle:
			filehandle.write('%s\n' % z)

	elif y == 'delete':
	  try:
	   try:
	    db[-1] = ''
	    with open('list.txt', 'w+') as filehandle:
	     for index,line in enumerate(filehandle):
	      if index != -1:
	       filehandle.write(line)
	    print('Delete successful')
	    list_of_lines = ''
	   except:
	     print('entry not found!')
	  except:
	   print('Thats not a number!')

	elif y == 'exit':
		break

	else:
		print('This is not a valid answer, please try again.')
