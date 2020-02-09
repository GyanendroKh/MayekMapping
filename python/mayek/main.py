import json
import io
import os

class Mayek:
  """This class contains the character mapping (E-pao Font) and categories of the Meitei Mayek characters."""
  def __init__(self):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mayek.json')
    data = io.open(path).read()
    self.data = json.loads(data)

    self.MAPUM = [c['char'].strip() for c in self.data[0]['mayek']]
    self.LONSUM = [c['char'].strip() for c in self.data[1]['mayek']]
    self.CHEITAP = [c['char'].strip() for c in self.data[2]['mayek']]
    self.CHEISING = [c['char'].strip() for c in self.data[3]['mayek']]
    self.KHUDAM = [c['char'].strip() for c in self.data[4]['mayek']]

    self.MAPPING = {}
    for mayek in self.data:
      for char in mayek['mayek']:
        self.MAPPING[char['code'].strip()] = char['char'].strip()
    
    self.MAPPING_REV = {v: k for k, v in self.MAPPING.items()}

  def to_unicode(self, string: str) -> str:
    """Converts the character codes of E-pao Font to Unicode characters."""
    unicode = []
    for c in string:
      if c in self.MAPPING: 
        unicode.append(self.MAPPING[c])
      else:
        unicode.append(c)
    return ''.join(unicode)
  
  def from_unicode(self, unicode: str) -> str:
    """Converts the unicode character to E-pao Font."""
    string = []
    for c in unicode:
      if c in self.MAPPING_REV:
        string.append(self.MAPPING_REV[c])
      else:
        string.append(c)
    return ''.join(string)
  
  def __str__(self):
    return json.dumps(self.data, ensure_ascii=False)


if __name__ == "__main__":
  mayek = Mayek()

  print(mayek.MAPPING)
  print(mayek.MAPPING_REV)
  print(mayek.MAPUM)
  print(mayek.LONSUM)
  print(mayek.CHEITAP)
  print(mayek.CHEISING)
  print(mayek.KHUDAM)

  print(mayek.to_unicode('mitE myeQ'))
  print(mayek.from_unicode('ꯃꯤꯇꯩ ꯃꯌꯦꯛ'))
