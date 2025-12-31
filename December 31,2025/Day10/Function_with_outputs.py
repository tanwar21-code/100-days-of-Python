# aking title case for the names
def format_name(f_name,l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    
    # print(f'{formatted_f_name} {formatted_l_name}') we can also use return as well
    return f'{formatted_f_name} {formatted_l_name}'
formatted_string = format_name('HimAnshU','tAnwAR')

print(formatted_string)