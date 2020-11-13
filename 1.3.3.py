# Kapitel 1: Grundläggande python
# Delkapitel 1.3 If-satser
# Skapa ett program som avgör huruvida en sträng är en palindrom. Om
# strängen innehåller andra tecken än bokstäver, ignoreras den.

anvandare = input('Skriv ett ord som kanske är ett palindrom:  ')

anvandare = anvandare.casefold() # ignorerar versaler

omvand = reversed(anvandare) # vänder på strängen


if list(anvandare) == list(omvand): # gör om hannah till [h,a,n,n,a,h] kollar om dem är lika
    print('Det är ett palindrom')
else:
    print('Det är inte ett palindrom')
