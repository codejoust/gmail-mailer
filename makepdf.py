#!/usr/bin/env python

from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


import StringIO

styles = getSampleStyleSheet()

def createPdf(subject, to, address, message):
    #buff = StringIO.StringIO()

    doc = SimpleDocTemplate('tmp.pdf', pagesize=letter)

    message = message.split("\n\n")

    Catalog = []
    #header = Paragraph("", styles['Heading1'])
    #Catalog.append(header)
    style = styles['Normal']
    print address
    for line in address.split("\n"):
      p = Paragraph("%s" % line, style)
      Catalog.append(p)
    Catalog.append(Spacer(1, 0.3*inch))
    for para in message:
      p = Paragraph("%s" % para, style)
      Catalog.append(p)
      s = Spacer(1, 0.25*inch)
      Catalog.append(s)
    doc.build(Catalog)
    #return buff
    return('tmp.pdf')

