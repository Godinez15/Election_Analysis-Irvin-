with open('./output.txt', 'a') as output_file:
    #
    output_file.write('output')
    print('by the time this line executes; the file is *open*, and can write to it*')
    

    print('by the time this executes; python closed the file safely')

