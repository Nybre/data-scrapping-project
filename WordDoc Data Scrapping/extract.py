import docxpy
file = 'Peterson.docx'
# extract hyperlinks from a word doc
doc = docxpy.DOCReader(file)
doc.process()  # process file
hyperlinks = doc.data['links']
 
