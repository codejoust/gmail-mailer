
import re
import lob

import usaddress

import makepdf

lob.api_key = 'test_44186cc51327700d3c1ae89fca1a060a759'

def deal_with_email_data(subject, frm, lines):
	firstBreakAt = lines.index("\n\n")
	addresspart = lines[:firstBreakAt]
	messagepart = lines[firstBreakAt:]
	address = createAddress(addresspart)
	object_message = createObject(makepdf.createPdf(subject, 'iain', addresspart, messagepart))
	obj = createObject(object_message)
	address_from = lob.Address.list(count=2).data

	return lob.Job.create(
	    name='Thankyou first!',
	    to_address=address,
	    from_address='adr_5b0a9530c75c5bd7',
	    objects = obj
	)

def createAddress(address):
	addr = usaddress.parse(address)
	data = {}
	for part, addrtype in addr:
		if addrtype not in data:
			data[addrtype] = []
		data[addrtype].append(part)
	for element in data: 
		data[element] = " ".join(data[element])

	return lob.Address.create(
	    name=data.get('Recipient', 'Lucky Winner!')[40:],
	    address_line1=data['AddressNumber'] + ' ' + data['StreetName'],
	    address_city=data.get('PlaceName', None),
	    address_state=data['StateName'],
	    address_country='US',
	    address_zip=data.get('ZipCode', '30003')
	)

def createObject(fn):
	print 'filename'
	print fn 
	#Create an Object using a file-like object.
	
	return lob.Object.create(
	    name='Mainfile',
	    file=open('tmp.pdf', 'rb'),
	    setting=100,
	    quantity=1,
	    double_sided=0
	)

