#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import email
import imaplib

from config import imap_server, imap_folder, subject_contains, path_to_save, file_name
from config import mail_user, mail_pass
from string import maketrans

mail = imaplib.IMAP4_SSL(imap_server, 993)

try:
    mail.login(mail_user, mail_pass)
    # print mail.list() # to see mailbox folder structure
    mail.select(imap_folder)
    res_code, msg_ids = mail.search(None, 'SUBJECT', '"{!s}"'.format(subject_contains))
    # print res_code, msg_ids  # DEBUG

    if res_code:
        for msg_id in msg_ids[0].split():
            resp, data = mail.fetch(msg_id, '(RFC822)')
            msg_body = data[0][1]
            m_data = email.message_from_string(msg_body)
            if m_data.get_content_maintype() != 'multipart':
                continue
            for part in m_data.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                if not file_name:
                    file_name = part.get_filename()
                if file_name is not None:
                    intab = "\r\n, "
                    outtab = "____"
                    trantab = maketrans(intab, outtab)
                    file_name = file_name.translate(trantab)
                    sv_path = os.path.join(path_to_save, file_name)
                    if not os.path.isfile(sv_path):
                        print sv_path
                        with open(sv_path, 'wb') as fp:
                            fp.write(part.get_payload(decode=True))
finally:
    try:
        mail.close()
    finally:
        mail.logout()
