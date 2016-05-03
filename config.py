import sys
sys.dont_write_bytecode = True

imap_server = 'imap.gmail.com'
mail_user = 'xxxxx@gmail.com'
mail_pass = 'xxxxx'

imap_folder = '"[Gmail]/All Mail"'  # common: "INBOX", "[Gmail]", "[Gmail]/All Mail",
                                    # "[Gmail]/Drafts", "[Gmail]/Important", "[Gmail]/Sent Mail",
                                    # "[Gmail]/Spam", "[Gmail]/Starred", "[Gmail]/Trash"
subject_contains = "Google"         # one or more words in mail subject

path_to_save = './'                 # current dir
file_name = ''                      # overrides original file name if set
