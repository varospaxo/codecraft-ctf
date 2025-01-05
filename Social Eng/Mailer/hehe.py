import imaplib
import email
import smtplib
import re
import time
import requests
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmailMonitor:
    def __init__(self, imap_server, smtp_server, email_address, password, target_domain):
        self.imap_server = imap_server
        self.smtp_server = smtp_server
        self.email_address = email_address
        self.password = password
        self.target_domain = target_domain
        self.executor = ThreadPoolExecutor(max_workers=5)
        self.running = True
        
    def connect_imap(self):
        self.imap = imaplib.IMAP4_SSL(self.imap_server)
        self.imap.login(self.email_address, self.password)
        
    def connect_smtp(self):
        self.smtp = smtplib.SMTP_SSL(self.smtp_server)
        self.smtp.login(self.email_address, self.password)
        
    def extract_email_addresses(self, text):
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(email_pattern, text)
    
    def send_reply(self, to_address):
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = to_address
        msg['Subject'] = "Automated Reply"
        body = "CKCTF{1_4m_ph15h3d}"
        msg.attach(MIMEText(body, 'plain'))
        self.smtp.send_message(msg)
        
    def process_email(self, email_message):
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode()
        return email_message.get_payload(decode=True).decode()
    
    def process_single_email(self, num, msg_data):
        try:
            email_body = msg_data[0][1]
            email_message = email.message_from_bytes(email_body)
            body_text = self.process_email(email_message)
            found_emails = self.extract_email_addresses(body_text)
            
            for addr in found_emails:
                try:
                    self.send_reply(addr)
                    logger.info(f"Sent reply to: {addr}")
                except Exception as e:
                    logger.error(f"Error sending to {addr}: {str(e)}")
            
            self.imap.store(num, '+FLAGS', '\\Seen')
        except Exception as e:
            logger.error(f"Error processing email {num}: {str(e)}")
    
    def monitor_inbox(self):
        try:
            self.connect_imap()
            self.connect_smtp()
            
            while self.running:
                try:
                    self.imap.select('INBOX')
                    search_criteria = f'(UNSEEN FROM "*@{self.target_domain}")'
                    _, message_numbers = self.imap.search(None, search_criteria)
                    
                    if message_numbers[0]:
                        futures = []
                        for num in message_numbers[0].split():
                            _, msg_data = self.imap.fetch(num, '(RFC822)')
                            futures.append(
                                self.executor.submit(self.process_single_email, num, msg_data)
                            )
                        
                        for future in futures:
                            future.result()
                    
                    time.sleep(5)
                except Exception as e:
                    logger.error(f"Error in monitoring loop: {str(e)}")
                    # Attempt to reconnect
                    try:
                        self.connect_imap()
                        self.connect_smtp()
                    except:
                        time.sleep(5)  # Wait before retry
                        
        finally:
            self.cleanup()
    
    def cleanup(self):
        try:
            self.executor.shutdown(wait=True)
            self.imap.logout()
            self.smtp.quit()
        except:
            pass
    
    def stop(self):
        self.running = False

class Scheduler:
    def __init__(self):
        self.running = True
        self.username = 'digiitplus'
        self.token = '3f2be63762bd2b065987850a7e5dd807d1bb8065'
        self.host = 'www.pythonanywhere.com'
        self.id = 831960
    
    def update_schedule(self):
        while self.running:
            try:
                t = time.localtime()
                current_hour = time.strftime("%H", t)
                current_minute = time.strftime("%M", t)

                t = datetime.time(int(current_hour), int(current_minute))
                result = datetime.datetime.combine(datetime.date.today(), t) + datetime.timedelta(minutes=2)
                only_t = result.time()
                timelast = datetime.datetime.strptime(str(only_t), '%H:%M:%S')
                hour = timelast.hour
                minute = timelast.minute

                response = requests.patch(
                    f'https://{self.host}/api/v0/user/{self.username}/schedule/{self.id}/',
                    headers={'Authorization': f'Token {self.token}'},
                    json={
                        'hour': str(hour),
                        'minute': str(minute),
                        'description': str(only_t)
                    },
                    timeout=10
                )

                if response.status_code == 200:
                    logger.info(f"Schedule updated: {response.content}")
                else:
                    logger.error(f'Schedule update failed with status {response.status_code}: {response.content}')

            except Exception as e:
                logger.error(f"Error in scheduler: {str(e)}")

            time.sleep(150)
    
    def stop(self):
        self.running = False

def main():
    # Email monitor configuration
    IMAP_SERVER = "imap.gmail.com"
    SMTP_SERVER = "smtp.gmail.com"
    EMAIL_ADDRESS = "crudespace@gmail.com"
    PASSWORD = "zabuetdjgghllpvs"
    TARGET_DOMAIN = "gmail.com"
    
    try:
        # Create instances
        monitor = EmailMonitor(IMAP_SERVER, SMTP_SERVER, EMAIL_ADDRESS, PASSWORD, TARGET_DOMAIN)
        scheduler = Scheduler()
        
        # Create threads
        monitor_thread = Thread(target=monitor.monitor_inbox, name="MonitorThread", daemon=True)
        scheduler_thread = Thread(target=scheduler.update_schedule, name="SchedulerThread", daemon=True)
        
        # Start threads
        monitor_thread.start()
        scheduler_thread.start()
        
        # Keep main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        logger.info("Shutting down...")
        monitor.stop()
        scheduler.stop()
        
if __name__ == "__main__":
    main()