words=input("Enter : ").split()
rev_words=[]
def rev(a):
    global rev_words
    if len(a)!=0:
        rev_words.append(a[-1])
        return rev(a[:len(a)-1])
    else:
        return True
rev(words)
final=' '.join(rev_words)
print(final)