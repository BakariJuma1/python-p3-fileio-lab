def write_file(file_name, file_content):
    file_name=(f"{file_name}.txt")
    with open(file_name,'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    file_name=(f"{file_name}.txt")
    with open(file_name,'a')as f:
        f.write(append_content)


def read_file(file_name):
    file_name=(f"{file_name}.txt")
    with open(file_name,'r')as f:
        return f.read()

write_file(file_name='logfile',file_content='Log1: Bananas are added')
append_file(file_name='logfile',append_content='Log2:3 Bananas subtracted')
read_file(file_name='logfile')
content=read_file('logfile')
print(content)