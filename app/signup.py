import csv
import os

def signUp(username,password):

    cwd = os.getcwd()

    def sign(user):
        file1 = open(f'{cwd}/app/creds.csv','a',newline='')
        wr1 = csv.writer(file1)
        wr1.writerow([username,password])
        file = open(f'{cwd}/app/files/{user}.csv','w',newline='')
        wr = csv.writer(file)
        wr.writerow(['taskname','schedule','completed'])
        file.close()

    file2 = open(f'{cwd}/app/creds.csv','r')
    rd = csv.reader(file2)

    found = False

    for i in rd:
        if username == i[0]:
            found = False
            break
        else:
            found = True
                
    if found:
        sign(username)
        return True
    else:
        return False

# signUp('pavan','pavan12345')