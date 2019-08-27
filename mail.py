from flask import Flask, request, render_template
from flask_mail import Mail, Message
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



app = Flask(__name__,template_folder='template')
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sadithyakumaran@gmail.com'
app.config['MAIL_PASSWORD'] = 'vanpersiesux'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST'])

def getvalue():
    hr = request.form['mid']
    name = request.form['name']
    num = request.form['cn']
    
    gen = request.form['gender']
    if gen == 'male':
        
        p1 = 'Respected Sir,\n\n'
        p2 = 'Greetings from Sri Venkateswara College of Engineering.\n'
        p3 = 'With respect to our telephonic conversation, I am sending you the details and a formal invitation extended to you and your colleagues for the Mock Placements-2019 to be conducted on February 17th (Sunday) at Sri Venkateswara College of Engineering, Sriperumbudur.\n\n'
        p4 = 'The event is expected to start at 9:30. You can contact me at the phone number mentioned in the mail for clarification on any details regarding logistics.\n\n'
        p5 = 'We would be absolutely honoured and delighted to have you on board for this event. Looking forward to your participation .\n'
        p6 = 'Please refer to the file attached below for further details about the event.\n\n'
        p7 = 'Thank you.\n\n'
        p8 = 'Regards,\n'
        p9 = '{}\n'.format(name)
        p10 = '{}\n'.format(num)
        p11 = 'The Forum for Economic Studies by Engineers\n Placement cell'
        body = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11
        
    
    if gen == 'female':
        p1 = "Respected Ma'am,\n\n"
        p2 = 'Greetings from Sri Venkateswara College of Engineering.\n'
        p3 = 'With respect to our telephonic conversation, I am sending you the details and a formal invitation extended to you and your colleagues for the Mock Placements-2019 to be conducted on February 17th (Sunday) at Sri Venkateswara College of Engineering, Sriperumbudur.\n\n'
        p4 = 'The event is expected to start at 9:30. You can contact me at the phone number mentioned in the mail for clarification on any details regarding logistics.\n\n'
        p5 = 'We would be absolutely honoured and delighted to have you on board for this event. Looking forward to your participation .\n'
        p6 = 'Please refer to the file attached below for further details about the event.\n\n'
        p7 = 'Thank you.\n\n'
        p8 = 'Regards,\n'
        p9 = '{}\n'.format(name)
        p10 = '{}\n'.format(num)
        p11 = 'The Forum for Economic Studies by Engineers\n Placement cell'
        body = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11
        

    print(hr)
    print(name)
    print(num)
    print(gen)
    
    

    
    fromaddr = "sadithyakumaran@gmail.com"
    toaddr = hr
   
# instance of MIMEMultipart 
    msg = MIMEMultipart() 
  
# storing the senders email address   
    msg['From'] = fromaddr 
  
# storing the receivers email address  
    msg['To'] = toaddr 
  
# storing the subject  
    msg['Subject'] = "Mock Placements 2019"
  
# string to store the body of the mail 
    
        
       
     
    
        
        
    
    
  
# attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 





    

     

    


    filename='invite.pdf'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("sadithyakumaran@gmail.com","vanpersiesux")
    text = msg.as_string()

    server.sendmail("sadithyakumaran@gmail.com",toaddr,text)
    server.quit()

    
    
    return "Sent"


    
if __name__ == '__main__':
    app.run(debug=True)









    

    
    
        
   
