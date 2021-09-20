import regex
from calibre import replace_entities
from calibre import prepare_string_for_xml

def replace(match, number, file_name, metadata, dictionaries, data, functions, *args, **kwargs):

    def replace_word(wmatch):
        # Check if the current word exits in the dictionary
        CheckThisSpelling = wmatch.group(1)
        if dictionaries.recognized(CheckThisSpelling) == True:   
            return wmatch.group()
        else:
        #	else try to correct it - remove American spelling
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("or", "our") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)         
            NewSpelling = CheckThisSpelling + '~'
            NewSpelling = NewSpelling.replace("or~", "our") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2) 
            NewSpelling = CheckThisSpelling + '~'
            NewSpelling = NewSpelling.replace("ors~", "our") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)    
        #	else try to correct it - remove American spelling
            NewSpelling = CheckThisSpelling + '~'
            NewSpelling = NewSpelling.replace("er~", "re") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("er", "re") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
            else:
              NewSpelling = NewSpelling.replace("ree", "re") 
              if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)                                    
            NewSpelling = CheckThisSpelling + '~'
            NewSpelling = NewSpelling.replace("ers~", "res") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
            NewSpelling = CheckThisSpelling + '~'
            NewSpelling = NewSpelling.replace("nse~", "nce") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
        #	else try to correct it - remove American spelling
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("l", "ll") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("l", "ll",1) 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("l", "~",2) 
            NewSpelling = NewSpelling.replace("~", "l",1)
            NewSpelling = NewSpelling.replace("~", "ll",1)                       
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)                                                 
        #	else try to correct it - remove American spelling
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("ll", "l") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("ll", "l",1) 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("ll", "~",2) 
            NewSpelling = NewSpelling.replace("~", "ll",1)
            NewSpelling = NewSpelling.replace("~", "l",1)                       
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)               
         #
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("U", "li") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("U", "ll") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)            
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("h", "li") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2) 
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("H", "li") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2) 
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("h", "li",1) 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2) 
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("H", "li",1) 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)  
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("h", "~",2) 
            NewSpelling = NewSpelling.replace("~", "h",1)
            NewSpelling = NewSpelling.replace("~", "li",1)              
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2) 
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("H", "~",2) 
            NewSpelling = NewSpelling.replace("~", "H",1)
            NewSpelling = NewSpelling.replace("~", "li",1)   
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)                         
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("im", "un") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("l", "ll") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
         #
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("imi", "um") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)              
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("m", "rn") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2) 
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("m", "in") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2) 
         #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("m", "hi") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)  
          #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("mn", "um") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)           
          #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("nm", "run") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
          #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("nmi", "rum") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)                                                                                                           
          #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("bn", "lm") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)                                                                                                            
          #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("ii", "h") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)                                                                                                            
          #	else try to correct it 
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("ii", "u") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)                                                                                                            
         #	
         #	else try to correct it 
            if CheckThisSpelling == 'Fd':
                return " I'd" +  wmatch.group(2)  
            if CheckThisSpelling == 'Fve':
                return " I've" +  wmatch.group(2)
            if CheckThisSpelling == 'Fm':
                return " I'm" +  wmatch.group(2)
            if CheckThisSpelling == 'Fll':
                return " I'll" +  wmatch.group(2) 
            if CheckThisSpelling == 'youVe':
                return " you've" +  wmatch.group(2)
            if CheckThisSpelling == 'YouVe':
                return " You've" +  wmatch.group(2)                   
         #	
         #	else try to correct it 
            if CheckThisSpelling == 'wren\'t':
                return " weren't" +  wmatch.group(2)              

         #	
         #	else try to correct it 
            if CheckThisSpelling == '&':
                return ' ' + chr(38) +  wmatch.group(2)  
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace(">", "y") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("j&", "fi") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)
            NewSpelling = CheckThisSpelling
            NewSpelling = NewSpelling.replace("i&", "fi") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)  
            NewSpelling = NewSpelling.replace("l&", "fi") 
            if dictionaries.recognized(NewSpelling) == True:   
                return NewSpelling +  wmatch.group(2)                                      
                                                                              
        return wmatch.group()
        #return wmatch.group() + '1' + wmatch.group(1) + '2' + wmatch.group(2) + '3' + NewSpelling
    # Search for words 
    text = replace_entities(match.group()[1:-1])  # Handle HTML entities like &amp;
    corrected = regex.sub(r'\s*([\w\>\&[[a-z]\'[a-z]]]*)([\s*\.\?\,\"\;])', replace_word, text, flags=regex.VERSION1 | regex.UNICODE)
    return '>%s<' % prepare_string_for_xml(corrected)  # Put back required entities
