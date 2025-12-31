def calculate_love_score(name1,name2):
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of each letter in "TRUE" and "LOVE"
    count_t = 0
    count_r = 0
    count_u = 0
    count_e = 0
    count_l = 0
    count_o = 0
    count_v = 0
    count_e2 = 0

    for letter in combined_names:
        if letter == 't':
            count_t += 1
        elif letter == 'r':
            count_r += 1
        elif letter == 'u':
            count_u += 1
        elif letter == 'e':
            count_e += 1

    for letter in combined_names:
        if letter == 'l':
            count_l += 1
        elif letter == 'o':
            count_o += 1
        elif letter == 'v':
            count_v += 1
        elif letter == 'e':
            count_e2 += 1
    # Calculate the love score
    love_score = int(str(count_t + count_r + count_u + count_e) + str(count_l + count_o + count_v + count_e2))
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")
