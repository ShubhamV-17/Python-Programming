st = input("enter message: ")
coding = input("1 for coding and 0 for decoding ")  
coding==True if (coding == "1") else False
nwords = []
words = st.split(" ")

if coding:
    for word in words:
        if len(word) >= 3:
            r1 = "aht"
            r2 = "gie"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])  # new way to reverse the string
    print(" ".join(nwords))
else:
    for word in words:
        if len(word) >= 3 and word.startswith("aht") and word.endswith("gie"):
            temp = word[3:-3]
            if len(temp) > 0:
                stnew = temp[-1] + temp[:-1]
                nwords.append(stnew)
            else:
                nwords.append(word)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))