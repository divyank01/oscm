import xml.etree.ElementTree as ET

def handle_errorList(form):
	xmlString = "<root>"+str(form)+"</root>"
	print xmlString
	root=ET.fromstring(xmlString)
	for cell in root.iter('td'):
		found=False
		message=""
		for u_list in cell.iter('ul'):
			if u_list.attrib.get('class')=='errorlist':
				message = u_list[0].text
				cell.remove(u_list)
				found=True
				#remove this from here
		if found:
			for inputs in cell.iter('input'):
				temp=inputs.attrib.get('placeholder')
				inputs.set('placeholder',temp+" "+message)
	return ET.tostring(root, encoding="us-ascii", method="xml").replace("<root>","").replace("</root>","")