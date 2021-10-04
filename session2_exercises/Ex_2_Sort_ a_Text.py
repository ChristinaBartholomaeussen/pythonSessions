def return_name(name):

    consonants  = [] #Erklære vocals til at være en list

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} 

    for ch in name:             # Løber gennem alle char i name
        if ch in vowels:        # Hvis char findes i listen med med vokaler skal den erstattes
            name = name.replace(ch, '')
    
    consonants[:0] = name       # Indsæetter hver char i consonants fra index 0
    consonants.sort()

    return consonants

myname = return_name('Ella')
print(myname)
    

