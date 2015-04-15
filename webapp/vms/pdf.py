from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Spacer, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from django.http import HttpResponse
from pytz import timezone
from datetime import datetime, timedelta
from .models import TheftReport, StudentVehicle, EmployeeVehicle
# from vms import views
import os,re,pytz
# reportlab.platypus.Paragraph



def pdf_gen(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Confirmation.pdf"'

    # Here actual pdf generation work starts
    image="vms/static/vms/images/logo-iitg.gif"
    banner="vms/static/vms/images/hindi-banner.gif"
    fimg=open(str(image),'r+')
    #fimg.write(response.read())
    #fimg.close()
    # utc = pytz.utc
    # currzone = timezone(str(utc.zone))
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    # loc_dt = currzone.localize(now)

    styles = getSampleStyleSheet()
    styleN = styles['Normal']

    p = canvas.Canvas(response, bottomup=1)
    # p.saveState()
    p.translate(5,840)      ## origin ha shifted to this co-ordinates
    # p.scale(1,-1)
    # p.rotate(90)
    #image = canvas.ImageReader(StringIO.StringIO(image))
    p.drawImage(str(image), 0, -120 , width=100,height=100)
    p.drawImage(str(banner), 120, -60 , width=400,height=40)
    p.saveState()
    p.setFont("Times-Roman", 26)
    p.drawString(120,-80, "Indian Institute of Technology Guwahati")
    p.restoreState()

    p.saveState()
    p.setFont("Times-Roman", 12)
    p.drawString(120,-100, "Guwahati - 781039, INDIA")
    p.restoreState()
    
    p.saveState()
    p.setFont("Times-Roman", 20)
    p.drawString(150,-200,"Receipt for Theft Report")
    p.restoreState()

    p.line(150,-209,350,-209)

    p.saveState()
    p.setFont("Times-Roman", 17)
    p.drawString(10,-170,"Date :")
    p.restoreState()
    p.drawString(51, -170, str(now.strftime("%d-%m-%Y")))
    # p.drawString(60, -170, str(now))

    p.saveState()
    p.setFont("Times-Roman", 17)
    p.drawString(460,-170,"Time :")
    p.restoreState()
    p.drawString(505, -170,now.strftime("%H:%M:%S"))

    p.saveState()
    p.setFont("Times-Roman", 17)
    p.drawString(150,-250,"Reporter name :")
    p.restoreState()
    # print "here"
    p.drawString(262,-250, str(request.reporter.first_name + " " + request.reporter.last_name))
    # print "here2"
    p.saveState()
    p.setFont("Times-Roman", 17)
    p.drawString(150,-290,"Vehicle Pass Number :")
    p.restoreState()

    p.drawString(309,-290,request.vehicle_pass_no)
    
    # p.saveState()
    # p.setFont("Times-Roman", 17)
    # p.drawString(150,-330,"Vehicle Type :")
    # p.restoreState()

    # p.drawString(254,-330,request.POST['vehicle_type'])

    # # p.saveState()
    # p.setFont("Times-Roman", 17)
    # p.drawString(150,-370,"Vehicle Model :")
    # p.restoreState()

    # p.drawString(264,-370,request.POST['vehicle_model'])

    p.saveState()
    p.setFont("Times-Roman", 17)
    p.drawString(150,-330,"Theft Date and Time :")
    p.restoreState()

    p.drawString(310,-330,str(request.theft_time.strftime("%d-%m-%Y %H:%M:%S")))

    p.saveState()
    p.setFont("Times-Roman", 17)
    p.drawString(150,-370,"Theft Place :")
    p.restoreState()

    p.drawString(241,-370,str(request.theft_place))

    p.saveState()
    p.setFont("Times-Roman", 17)
    p.drawString(150,-410,"Your Status : ")
    p.restoreState()

    p.drawString(247,-410,request.status)

    p.drawString(40, -450, "NB: System Generated Receipt. Does Not Require Signature.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

