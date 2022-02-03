from atbash import atbash_encrypt, atbash_decrypt, atbash_wrapper

def test_atbash_encrypt():
    assert callable(atbash_encrypt)
    assert isinstance(atbash_encrypt('hello'), str)
    assert atbash_encrypt('HELLO') == 'SVOOL'
    assert atbash_encrypt('hello') == 'SVOOL'
    
def test_atbash_decrypt():
    assert callable(atbash_decrypt)
    assert isinstance(atbash_decrypt('hello'), str)
    assert atbash_decrypt('SVOOL') == 'HELLO'
    assert atbash_decrypt('svool') == 'HELLO'

def test_atbash_wrapper():
    assert callable(atbash_wrapper)
    assert isinstance(atbash_wrapper('hello', method='encrypt'), str)
    assert atbash_wrapper('hello', method='encrypt') == 'SVOOL'
    assert atbash_wrapper('HELLO', method='encrypt') == 'SVOOL'
    assert atbash_wrapper('SVOOL', method='decrypt') == 'HELLO'
    assert atbash_wrapper('svool', method='decrypt') == 'HELLO'    
    assert atbash_wrapper('svool', method='blargh') == "method should be either 'decrypt' or 'encrypt'"