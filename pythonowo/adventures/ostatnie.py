import os, glob
'''
print(sys.version) #printuje wersje pythona

os.system('ls') dziala jak ls
'''
'''
file_list = os.popen('ls').read().split('\n')
os.system('mkdir dupa_test')
for file_name in file_list:
    os.system(f'cp {file_name} dupa_test/{file_name}')


new_list = glob.glob('./**/*.py', recursive=True)
os.system('mkdir nowa_dupa_test')

for file_name in new_list:
    os.system(f'cp {file_name} nowa_dupa_test/{file_name.replace("./", "")}')
'''
### dziala ale sypie errorami ###############################

