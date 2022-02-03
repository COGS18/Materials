def atbash_encrypt(input_string):
    
    """Use atbash encryption to take an input string and 
    return the capitalized, reverse alphabetical position string.
    
    Parameters
    ----------
    input_string : str
        input string to be encrypted
        
    Returns
    -------
    atbash_string : str
        atbash encrypted string
    """
    
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    atbash_string = ''

    for char in input_string:
        char = char.upper()
        if char in alpha:
            position = alpha.find(char)
            atbash_string += reverse_alpha[position]
        else:
            atbash_string = None
            break
        
    return atbash_string


def atbash_decrypt(atbash_string):    
    ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    REVERSEALPHA='ZYXWVUTSRQPONMLKJIHGFEDCBA'
    atbash_string=atbash_string.upper()
    decrypted_string=''
    for l in atbash_string:
        if l in REVERSEALPHA:
            letterindex=REVERSEALPHA.find(l)
            decrypted_string=decrypted_string+ALPHA [letterindex]
        else: decrypted_string=decrypted_string+l
    return decrypted_string

def atbash_wrapper(input_string, method='encrypt'):
    if method == 'encrypt':
        output_string = atbash_encrypt(input_string)
    elif method == 'decrypt':
        output_string = atbash_encrypt(input_string)
    else:
        output_string = "method should be either 'decrypt' or 'encrypt'"
    
    return output_string