#coding=utf-8
import smtplib  
import email.mime.multipart  
import email.mime.text  
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from log import Log
import os
from public import function

def send_report(result_dir):
	"最新生成的测试报告"
	lists=os.listdir(result_dir)
	lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
	#print (u'最新测试生成的报告： '+lists[-1])
	#找到最新生成的文件
	file_new = os.path.join(result_dir,lists[-1])
	print(file_new)
	return file_new

def Send_mail(sender,pwd,receiver,subject,content,file):
	log=Log()
	msg=email.mime.multipart.MIMEMultipart()  
	msg['from']=sender  
	msg['to']=';'.join(receiver) 
	msg['subject']=subject
	txt=email.mime.text.MIMEText(content)  
	msg.attach(txt)
	  
	
	#发送附件，提示病毒，无法发送成功
	htmlpart = MIMEApplication(open(file, 'rb').read())
	htmlpart.add_header('Content-Disposition', 'attachment', filename='beauty.html')
	msg.attach(htmlpart)
	
	# xlsx类型的附件
	#xlsxpart = MIMEApplication(open('test.xlsx', 'rb').read())
    #xlsxpart.add_header('Content-Disposition', 'attachment', filename='test.xlsx')
    #msg.attach(xlsxpart)
	
	try:
		smtp=smtplib.SMTP()
		smtp.connect('smtp.qiye.163.com')
		smtp.login(sender,pwd)
		smtp.sendmail(sender,receiver,str(msg))  
		smtp.quit()
		log.info("邮件发送成功")
	except smtplib.SMTPException:
		log.info("Error: 无法发送邮件")
              
if __name__ == '__main__':
	filedir=function.get_filepath("/result/report")
	base_dir=base_dir.replace('\\','/')
	   
	file=send_report(filedir)
	sender = 'mengxue@senyint.com'
	pwd="Mx111111"
	receiver = ['mengxue@senyint.com']
	subject='演示间系统启动验证'
	content='<html><h1>你好/n</h1>\n</html>'
	Send_mail(sender,pwd,receiver,subject,content,file)
