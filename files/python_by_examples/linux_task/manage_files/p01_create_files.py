# we use the open class to create/managed a file's content. 
# for mroe info see:
# help(open)
# https://www.guru99.com/reading-and-writing-files-in-python.html
write_testfile_handler_object = open('/tmp/testfile.txt', mode='wt', encoding='utf-8')
# the mode 'wt' means write-text

write_testfile_handler_object.write('this is the first line\n')
write_testfile_handler_object.write('this is the second line\n')
write_testfile_handler_object.write('this is the third line\n')
write_testfile_handler_object.write('this is the fourth line\n')


write_testfile_handler_object.close()

read_testfile_handler_object = open('/tmp/testfile.txt', mode='rt', encoding='utf-8')
print(read_testfile_handler_object.read())

# return to begining on file. 
read_testfile_handler_object.seek(0)
# then read line by line. 

print(read_testfile_handler_object.readline())
print(read_testfile_handler_object.readline())




read_testfile_handler_object.close()


