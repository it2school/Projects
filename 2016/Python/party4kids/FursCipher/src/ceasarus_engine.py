from dmessage_engine import DMessageEngine
class CeasarusEngine(DMessageEngine):
    def __init__(self, key, language):
        super().__init__(key, language)
    
    def cipher_letter (self, letter):
       return self.transform_ceasarus(self.key, letter)
        
    def decipher_letter (self, letter):
       return self.transform_ceasarus(-self.key, letter)

    def transform_ceasarus(self, key, letter):
        selected_alphabet = self.languages [self.language]
        isupper = letter.isupper()
        low = letter.lower()           

        if low not in selected_alphabet:
            return super().cipher_letter(letter)
        else:
            ord_letter = selected_alphabet.index(low)
            translated = ((ord_letter + key ) % len(selected_alphabet))
            if isupper:
                return selected_alphabet[translated].upper()
            return selected_alphabet[translated]      
