# MayekMapping
Utility Functions for managing Meitei Mayek Characters and mapping to E-pao Fonts.   

### Installation
`$ python3 -m pip install meiteimayek-mapping`

### Usage
```python
from mayek import Mayek

mayek = Mayek()

# This will print out all the Mapum Mayek
print(mayek.MAPUM)

# This will print out all the Lonsum Mayek
print(mayek.LONSUM)

# This will print out all the Cheitap Mayek
print(mayek.CHEITAP)

# This will print out all the Cheising Mayek
print(mayek.CHEISING)

# This will print out all the KHUDMA Mayek
print(mayek.KHUDAM)

# This will convert the character code of E-pao font to Unicode
print(mayek.to_unicode('mitE myeQ'))

# THis will convert from Unicode to E-pao font's character code
print(mayek.from_unicode('ꯃꯤꯇꯩ ꯃꯌꯦꯛ'))
```
