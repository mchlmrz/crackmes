def GetNextName( OldName ):
	if (len(OldName) == OldName.count("~")):
		return '!'*(len(OldName)+1)
	elif (OldName.rfind("~") > 1):
		i = OldName.rfind("~")

		if (ord(OldName[i-1]) == 91):
			newC = 93
		else:
			newC = ord(OldName[i-1])+1
		
		return OldName[0:i-1] + chr(newC) + '!'*(len(OldName)-i)
	elif (OldName.find("~") == 1):
		i = 1		
		if (ord(OldName[i-1]) == 91):
			newC = 93
		else:
			newC = ord(OldName[i-1])+1

		return chr(newC) + '!'*(len(OldName)-i)
	else:
		if (ord(OldName[-1]) == 91):
			v = 93
		else:
			v = ord(OldName[-1]) + 1
		
		return OldName[:(len(OldName)-1)] + chr(v)

def HashIt( Name ):
	edx = 0x0000ffff

	for ch in Name:
		ch = ord(ch)  & 0xFFFFFFFF
		eax = ch
		edi = edx

		edx = edx >> 1

		esi = edx

		esi = (esi ^ 0x8408)  & 0xFFFFFFFF
		if (((edi ^ ch) & 1) == 0):
			esi = edx

		edi = ch
		edi = edi >> 1
		edi = (edi ^ esi)  & 0xFFFFFFFF
		esi = esi >> 1

		edx = esi

		edx = (edx ^ 0x8408)  & 0xFFFFFFFF
		if ((edi & 1) == 0):
			edx = esi

		edi = edi & 1

		for x in range(2,7):
			esi = ch
			edi = edx
			edi = edi >> 1
			esi = esi >> x

			esi = (esi ^ edx)  & 0xFFFFFFFF
			edx = edi
			edx = (edx ^ 0x8408)  & 0xFFFFFFFF

			if ((esi & 1) == 0):
				edx = edi

			esi = esi & 1
		
		esi = edx
		esi = esi >> 1
		eax = eax >> 7
		eax = (eax ^ edx)  & 0xFFFFFFFF
		edx = esi
		edx = (edx ^ 0x8408)  & 0xFFFFFFFF
		
		al = eax & 0xFF
		if ((al & 1) == 0):
			edx = esi	


	edx = (~edx) & 0xFFFFFFFF

	code = (edx >> 8) & 0x000000FF
	code = code << 8
	code = code | edx

	code = code & 0x0000FFFF

	return ( ((code << 8) | (code >> 8) ) & 0x0000FFFF)

Namex = "Michele!!!!!!!!"
tofind = 10
while (True):
	if (HashIt(Namex) == 0xe425):
		print("Found a name: ")
		print(Namex)
		print("\n")

		tofind = tofind - 1

		if (tofind == 0):
			break
	
	Namex = GetNextName(Namex)
