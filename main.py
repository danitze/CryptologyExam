import des
import sha1

if __name__ == '__main__':
    k = 0x0e329232ea6d0d73  # 64 bit
    k2 = 0x133457799BBCDFF1
    m = 0x8787878787888787
    m2 = 0x0123457789ABCDEF
    print("DES ex. 1")
    des.prove(k, m)
    print("DES ex. 2")
    des.prove(k2, m2)

    print()
    print("SHA-1")
    plainText = "This is sample message that should be hashed"
    sha1Hash = sha1.sha1Function(plainText)
    print(sha1Hash)



