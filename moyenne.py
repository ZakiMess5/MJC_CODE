def moyenne (note1, note2, note3, coef1, coef2, coef3):
    resultat =(coef1*note1+coef2*note2+coef3*note3)/(coef1+coef2+coef3)
    return resultat


print(moyenne(18,20,16, 1, 2, 4))
