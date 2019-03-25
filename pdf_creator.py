from flask import make_response
import pdfkit

pdf = pdfkit.from_string(rendered, False)
response = make_response(pdf)
response.headers['Content-Type'] = 'application/pdf'
response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
