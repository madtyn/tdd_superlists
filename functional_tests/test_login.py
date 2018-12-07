import os
import poplib
import imaplib
import re
import time
from django.core import mail
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

SUBJECT = 'Your login link for Superlists'


class LoginTest(FunctionalTest):
    def wait_for_email(self, test_email, subject):
        if not self.staging_server:
            email = mail.outbox[0]
            self.assertIn(test_email, email.to)
            self.assertEqual(email.subject, subject)
            return email.body

        email_id = None
        start = time.time()
        inbox = imaplib.IMAP4_SSL('imap.gmail.com')
        
        try:
            inbox.login(test_email, os.environ['GMAIL_PASSWORD'])
            inbox.select('inbox')
            type_, data = inbox.search(None, 'ALL')
            id_list = data[0].split()
            last = int(id_list[-1])
            while time.time() - start < 60:
                # get 10 newest messages
                

                for i in range(last, last-10, -1):
                    print('getting msg', i)
                    typ, data = inbox.fetch(str(last), '(RFC822)')
                    lines = [line.strip() for line in data[0][1].decode('utf8').split('\n')]
                    print(lines)
                    if f'Subject: {subject}' in lines:
                        email_id = i
                        body = '\n'.join(lines)
                        return body
                time.sleep(5)
        finally:
            if email_id:
                inbox.store(str(email_id), '+FLAGS', '\\Deleted')
                inbox.expunge()
            inbox.logout()


    def test_can_get_email_link_to_log_in(self):
        # Edith goes to the awesome superlists site
        # and notices a "Log in" section in the navbar for the first time
        # It's telling her to enter her email address, so she does
        if self.staging_server:
            test_email = 'madtyn@gmail.com'
        else:
            test_email = 'edith@example.com'

        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(test_email)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # A message appears telling her an email has been sent
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))

        # She checks her email and finds a message
        body = self.wait_for_email(test_email, SUBJECT)

        # It has a url link in it
        self.assertIn('Use this link to log in', body)
        url_search = re.search(r'http://.+/.+$', body)
        if not url_search:
            self.fail(f'Could not find url in email body:\n{body}')
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # she clicks it
        self.browser.get(url)

        # she is logged in!
        self.wait_to_be_logged_in(email=test_email)

        # Now she logs out
        self.browser.find_element_by_link_text('Log out').click()

        # She is logged out
        self.wait_to_be_logged_out(email=test_email)
        
