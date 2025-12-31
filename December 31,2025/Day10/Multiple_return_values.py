# aking title case for the names
def format_name(f_name,l_name):
    if f_name == '' or l_name == '':
        return 'You didn\'t provide valid arguments.'
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    
    # print(f'{formatted_f_name} {formatted_l_name}') we can also use return as well
    return f'{formatted_f_name} {formatted_l_name}'
    print('hello') #this will not run
formatted_string = format_name('HimAnshU','tAnwAR')

print(formatted_string)