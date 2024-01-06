students={
    101:{'name':'heel','number':376,'email id':'heel@gmail.com'},
    102:{'name':'patel','number':377,'email id':'patel@gmail.com'},
    103:{'name':'purv','number':378,'email id':'purv@gmail.com'}
}

for key,values in students.items():
    print('Studemnt is: ',key)

    for i,j in values.items():
        print(f'{i} is {j}')
    print('-'*20)

    # =====================
    #========OR==============
    #======================
    students={
    101:{'name':'heel','number':376,'email id':'heel@gmail.com'},
    102:{'name':'patel','number':377,'email id':'patel@gmail.com'},
    103:{'name':'purv','number':378,'email id':'purv@gmail.com'}
}

for key,values in students.items():
    # print(f'key is {key}')
    print('Studemnt is: ',key)

    for i in values:
        print(f'{i} is {values[i]}')
    print('-'*20)