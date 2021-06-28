msg = ["H", "e", "l", "l", "o", "S", "t", "u", "d", "e", "n", "t"]
str1 = []; str2 = []
cnt1 = 0; cnt2 = 0
print ("Rail Fence - Encryption\n\n")
print ("Plain Text: HelloStudent\n\n")
for i in range(len(msg)) :
    print(str1, str2, cnt1, cnt2)
    if (i % 2 == 0) :
        str1.append(msg[i])
        cnt1 += 1
    else :
        str2.append(msg[i])
        cnt2 += 1
print ("Cipher Text:", str1, str2)