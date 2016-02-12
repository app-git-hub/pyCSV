masterPBdict = dict()

def writeDict(dictName, fileHandle):
	for key, value in dictName.items():
		final = ""
		try:
			value.sort()
		except AttributeError:
			final+= "%(value)s:    %(key)s" % locals()
		else:
			# print only the longest name, cz it is most descriptive
		# final+= "\n"
		fileHandle.write(final)
		del final
	return

def clean(aLine):
	global masterPBdict, longestName
	name, sep, num = aLine.partition("\t")
	longestName = max(len(name), longestName)
	try:
		masterPBdict[num]					# wait if number exists in DB
	except KeyError:
		masterPBdict[num] = name			# if number is uniques, create key: value pair
	else:
		try:
			masterPBdict[num].append(name)	# num is duplicae, so appended name to old name list
		except AttributeError:
			old = masterPBdict.pop(num)		# replace str by list and 
			masterPBdict[num] = [old]
			masterPBdict[num].append(name)
	return

with open("all.tsv", mode="rt", encoding="UTF-8") as h:
	for _ in range(950):
		x = h.readline()
		if len(x) > 0:
			clean(x)

with open("clean.txt", mode="wt", encoding="UTF-8") as o:
	writeDict(masterPBdict, o)











"""
masterPBdict = dict()

def writeDict(dictName, fileHandle):
	for key, value in dictName.items():
		final = ""
		try:
			value.sort()
		except AttributeError:
			final+= "%(value)s:    %(key)s" % locals()
		else:
			for index, aName in enumerate(    list(set(value))    ):
				if len(value)//2-1 == index:
					final+= "%(aName)s:    %(key)s" % locals()
				else:
					final+= "%(aName)s" % locals()
		# final+= "\n"
		fileHandle.write(final)
		del final
	return

def clean(aLine):
	global masterPBdict
	name, sep, num = aLine.partition("\t")
	try:
		masterPBdict[num]					# wait if number exists in DB
	except KeyError:
		masterPBdict[num] = name			# if number is uniques, create key: value pair
	else:
		try:
			masterPBdict[num].append(name)	# num is duplicae, so appended name to old name list
		except AttributeError:
			old = masterPBdict.pop(num)		# replace str by list and 
			masterPBdict[num] = [old]
			masterPBdict[num].append(name)
	return

with open("all.tsv", mode="rt", encoding="UTF-8") as h:
	for _ in range(950):
		x = h.readline()
		if len(x) > 0:
			clean(x)

with open("clean.txt", mode="wt", encoding="UTF-8") as o:
	writeDict(masterPBdict, o)
"""
"""
masterPBdict = dict()
longestName = 0

def pretty(num, names, mode='s'):
	midpt = len(names)//2-1
	for index, aName in enumerate(names):
		if mode is 's':
			if midpt == index:
				s+= "%(aName)s:    %(num)s" % locals()
			else:
				s+= "%(aName)s" % locals()
		else:
			global longestName
			longestName+= 5
			if midpt == index:
				s = "%(aName)s: " + "-"*longestName-len(aName) + " %(num)s"
				print(s % locals())
			elif index > midpt:
				lower()
			else:
				upper()
		print(s)
	return

def writeDict(d):
	for key, value in d.items():
		try:
			value.sort()
		except AttributeError:
			print("%(value)s:    %(key)s" % locals())
		else:
			pretty(key, value, mode="s")
	return

def clean(aLine):
	global masterPBdict, longestName
	name, sep, num = aLine.partition("\t")
	longestName = max(len(name), longestName)
	try:
		masterPBdict[num]					# wait if number exists in DB
	except KeyError:
		masterPBdict[num] = name			# if number is uniques, create key: value pair
	else:
		try:
			masterPBdict[num].append(name)	# num is duplicae, so appended name to old name list
		except AttributeError:
			old = masterPBdict.pop(num)		# replace str by list and 
			masterPBdict[num] = [old]
			masterPBdict[num].append(name)
	return

with open("all.tsv", mode="rt", encoding="UTF-8") as h:
	for _ in range(950):
		x = h.readline()
		if len(x) > 0:
			clean(x)

writeDict(masterPBdict)
"""