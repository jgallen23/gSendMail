import smtplib
from email.MIMEText import MIMEText

class GSendMail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_html(self, to, subject, body):
        msg = MIMEText(body)
        msg.set_type("text/html")
        msg["From"] = self.email
        msg["To"] = to
        msg["Subject"] = subject
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.email, self.password)
        server.sendmail(self.email, to, msg.as_string())
        server.close()


def main():
    from optparse import OptionParser
    usage = "usage: %prog -u [email] -p [passwd] -t [to] -s [subject] -b [body]"
    parser = OptionParser(usage)
    parser.add_option("-u", "--gmail", action = "store", type = "string", dest = "email")
    parser.add_option("-p", "--passwd", action = "store", type = "string", dest = "passwd")
    parser.add_option("-t", "--to", action = "store", type = "string", dest = "to")
    parser.add_option("-s", "--subject", action = "store", type = "string", dest = "subject")
    parser.add_option("-b", "--body", action = "store", type = "string", dest = "body")

    (options, args) = parser.parse_args()

    if options.email and options.passwd:
        g = GSendMail(options.email, options.passwd)
        g.send_html(options.to, options.subject, options.body)
    else:
        parser.print_help()

if __name__ == "__main__": main()
