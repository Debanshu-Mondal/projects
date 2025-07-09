sum=input("Enter the amount in words: ").lower().split()
total=0 
cur=0
dict1={
    "zero":0,"one":1,"two":2,"three":3,"four":4,
    "five":5,"six":6,"seven":7,"eight":8,"nine":9,
    "ten":10,"eleven":11,"twelve":12,"thirteen":13,
    "forteen":14,"fifteen":15,"sixteen":16,"seventeen":17,
    "eighteen":18,"nineteen":19,"twenty":20,"thirty":30,
    "forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,
    "ninety":90
}
dict2={
    "hundred":100,
    "thousand":1000,
    "million":1000000,
    "billion":1000000000
}
for word in sum:
    if word in dict1:
        cur+=dict1[word]
    elif word in dict2:
        cur*=dict2[word]
        if word!= "hundred": 
            total+=cur
            cur=0
    else:
        print("{}=Undefined character!".format(word))
total+=cur
cur=0
print("Numeric Value: {}".format(total))