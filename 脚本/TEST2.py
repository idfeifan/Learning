import re
a =''
result = a[::-1]
strinfo = re.compile(r"\)'MMYYYY',\)\(pmatsemit_xinu\(emitxinu_morf")

b = strinfo.sub('99',result,1)
result = b[::-1]
print(result)