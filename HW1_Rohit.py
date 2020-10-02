def first_question():
    with open('text_in.txt',mode='r') as input_file:
        contents = input_file.readlines()
        b=[]
        out_string=''
        for line in contents:
            i=list(line.split(' '))
            i.remove('\n')
            a=i[-1::-1]
            output=' '.join(a)
            out_string+=output+'\n'    

    with open('text_out1.txt',mode='w') as output_file:
        output_file.write(out_string)

def second_question():
    with open('text_in.txt',mode='r') as input_file:
        contents = input_file.readlines()
        a=len(contents)
    my_list=[]

    for line in contents:
        i=list(line.split(' '))
        i.remove('\n')
        for words in i:
            if words[-1] in ['.', ',','?']:
                a=(len(words)-1)
            else:
                a=len(words)
            my_list.append(a)

    my_dict=dict((k,my_list.count(k)) for k in set(my_list))
    
    f = open('text_out2.txt',mode='w')
    b='Word Length    Count'+'\n'
    f.write(b)
    a=''
    for key,value in my_dict.items():
        if (key<=9):
            str_key=str(key)
            str_value=str(value)
        
            a=str_key+'              '+str_value.ljust(3)+'\n'
            f.write(a)
        else:
            str_key=str(key)
            str_value=str(value)
            a=str_key+'             '+str_value.ljust(3)+'\n'
            f.write(a)
    f.close()
    
def third_question():
    with open('text_in.txt',mode='r') as input_file:
        contents = input_file.readlines()
    b=''
    for line in contents:
        for character in line:
            if (character not in [' ','\n']):
                asci_encode=((ord(character)-33+(41%94))%94)+33
                asci_encoded_char=chr(asci_encode)
                b+=asci_encoded_char
                
            else:
                b+=character
    with open('text_out3.txt',mode='w') as output_file:
        output_file.write(b)


if __name__ == "__main__": 
    print('\n The files are being processed and the output files are being generated in the background')
    print('\n Check your folder for the desired ouput files')
    first_question()
    second_question()
    third_question()