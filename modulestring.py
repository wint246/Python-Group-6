def demnguyenam(st):
    dem=0
    a="ueoai"
    for i in st:
        if i in a:
            dem+=1
    return dem

def chuanhoaspace(st):
    return (" ".join(st.strip().split()))