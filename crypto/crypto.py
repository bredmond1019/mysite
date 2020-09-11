def b64_encode(input_bytes):
    b64_index_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    encoded_output = ''

    bit_list = list(''.join([bin(byte)[2:].zfill(8) for byte in input_bytes]))

    groups_of_6 = [bit_list[i:i+6] for i in range(0, len(bit_list), 6)]

    for group in groups_of_6:
        group = ''.join(group)

        if len(group) == 2: 
            if '1' in group:
                group += '0000'
                encoded_output += b64_index_table[int(group, 2)] + '=='
            else:
                encoded_output += '=='
        
        elif len(group) == 4:
            if '1' in group:
                group += '00'
                encoded_output += b64_index_table[int(group, 2)] + '='
            else:
                encoded_output += '='
        
        elif len(group) == 6:
            encoded_output += b64_index_table[int(group, 2)]
    
    return encoded_output



def xor_byte_string(input_hex_1, input_hex_2):

    bytes_1 = bytes.fromhex(input_hex_1)
    bytes_2 = bytes.fromhex(input_hex_2)
    
    return bytes([b1 ^ b2 for b1, b2 in zip(bytes_1, bytes_2)]).hex()

