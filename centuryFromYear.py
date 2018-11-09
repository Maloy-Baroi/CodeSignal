def centuryFromYear(year):

    century=year//100
    reminding_year=year%100
    if reminding_year==0:
        return century
    else:
        return century+1
