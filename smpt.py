import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("vishnayaka@gmail.com", "vishnayaka*123#")
server.sendmail(
  "vishnayaka@gmail.com", 
  "vishruth.sn.nayaka@gmail.com", 
  "GOOD MORNING")
server.quit()