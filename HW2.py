
def _code_verify(_code):
    lenght = 0
    _key_index = 1
    while lenght < len(_code):
        for i in _code:
            _key = int(input(f"enter key number {_key_index} out of {len(_code)} keys: "))
            if _key == _code[lenght]:
                lenght += 1
                _key_index += 1
            else:
                lenght = 0
                _key_index = 1
                break
    return "correct password"



secret_code = [77, 12, 43, 100, 51]

_pass = _code_verify(secret_code)
print(_pass)


# sorted ver
    '''def _code_verify(_code):
        length = 0
        while length < len(_code):
            key = int(input(f"enter key number {length + 1} out of {len(_code)} keys: "))
            if key == _code[length]:
                length += 1
            else:
                length = 0
        return "correct password"
    
    secret_code = [77, 12, 43, 100, 51]
    print(_code_verify(secret_code))
    '''