from ceasarus_engine import CeasarusEngine


class VigenereEngine(CeasarusEngine):
    def __init__(self, cipher_word, language):
        super().__init__(0, language)
        self.cipher_word = cipher_word
        self.reset_key()

    def report_key(self):
        return (('Используем ключ: {}').format(self.cipher_word))
      
    def reset_key(self):
        self.current_index = 0
        self.key = self.to_key(self.cipher_word[self.current_index])

    def set_next_key (self):
        self.current_index += 1
        if self.current_index > len (self.cipher_word) - 1:
            self.current_index = 0
        self.key = self.to_key(self.cipher_word[self.current_index])
        
    def to_key (self, letter):
        return self.languages[self.language].index (letter.lower())
    
    def cipher (self, message):
        result = super().cipher(message)
        self.reset_key()
        return result
    
    def decipher (self, message):
        result = super().decipher(message)
        self.reset_key()
        return result

    def transform_ceasarus (self, key , letter):
        result = super().transform_ceasarus (key, letter)
        self.set_next_key()
        return result