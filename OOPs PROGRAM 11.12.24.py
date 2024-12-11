'''#PROBLEM--1

class Password:
    def __init__(self, password):  
        self.password = password

    def display(self):
        if len(self.password) < 8:  
            return "Password must contain at least 8 characters"
        elif self.password.islower():  
            return "Password must contain an uppercase letter"
        elif self.password.isupper():  
            return "Password must contain a lowercase letter"
        elif self.password.isalpha():  
            return "Password must contain numbers"
        elif self.password.isalnum() or ' ' in self.password
            return "Password must contain symbols"
        else:
            return "Password is valid"


user_password = input("Enter the password: ")
p = Password(user_password)  
print(p.display()) '''  

#PROBLEM--2
class TextProcessor:
    def __init__(self, text):
        self.text = text

    def split_into_sentences(self):
        
        punctuation = ['.', '?', '!']
        sentence = ""
        sentences = []
        for char in self.text:
            sentence += char
            if char in punctuation:
                sentences.append(sentence.strip())
                sentence = ""
        if sentence.strip(): 
            sentences.append(sentence.strip())
        return sentences

    def process_sentences(self, sentences):
        
        for sentence in sentences:
            word_count = len(sentence.split())
            print(f"o Sentence: \"{sentence}\", Word Count: {word_count}")
text = input("Enter a paragraph: ")
processor = TextProcessor(text)
sentences = processor.split_into_sentences()
print("\nSplit Sentences:")
for sentence in sentences:
    print(f"o \"{sentence}\"")
print("\nProcessed Sentence Data:")
processor.process_sentences(sentences)
