DEFAULT_BLOCK_SIZE  =  128
BYTE_SIZE  =  256
def  main（）：
    filename =  ' encrypted_file.txt '
    response =  input（' Encrypte \ Decrypt [e \ d]：'）

    如果 response.lower（）。startswith（' e '）：
        mode =  ' encrypt '
    elif response.lower（）。startswith（' d '）：
        mode =  ' decrypt '

    如果 mode ==  ' encrypt '：
        如果 不是 os.path.exists（' rsa_pubkey.txt '）：
            rkg.makeKeyFiles（' rsa '，1024）
            
        message =  input（' \ n输入消息：'）
        pubKeyFilename =  ' rsa_pubkey.txt '
        打印（'加密和写入％s ... ' ％（文件名））
        encryptedText = encryptAndWriteToFile（filename，pubKeyFilename，message）

        打印（' \ n加密文本：'）
        打印（encryptedText）

    elif模式==  ' decrypt '：
        privKeyFilename =  ' rsa_privkey.txt '
        print（'从％s读取并解密... ' ％（filename））
        decryptedText = readFromFileAndDecrypt（文件名，privKeyFilename）
        打印（'将解密到rsa_decryption.txt ... '）
        与 开放（' rsa_decryption.txt '，' w ^ '）为 12月：
            dec.write（decryptedText）

        print（' \ n Decryption：'）
        打印（解密文本）


def  getBlocksFromText（message，blockSize = DEFAULT_BLOCK_SIZE）：
    messageBytes = message.encode（' ascii '）

    blockInts = []
    for blockStart in  range（0，len（messageBytes），blockSize）：
        blockInt =  0
        对于我在 范围内（blockStart，min（blockStart + blockSize，len（messageBytes）））：
            blockInt + = messageBytes [i] *（BYTE_SIZE  **（i ％ blockSize））
        blockInts.append（blockInt）
    返回 blockInts


def  getTextFromBlocks（blockInts，messageLength，blockSize = DEFAULT_BLOCK_SIZE）：
    message = []
    for blockInt in blockInts：
        blockMessage = []
        对于我在 范围（BLOCKSIZE -  1，- 1，- 1）：
            如果 len（message）+ i < messageLength：
                asciiNumber = blockInt //（BYTE_SIZE  ** i）
                blockInt = blockInt ％（BYTE_SIZE  ** i）
                blockMessage.insert（0，chr（asciiNumber））
        message.extend（blockMessage）
    return  ' '. join（message）


def  encryptMessage（message，key，blockSize = DEFAULT_BLOCK_SIZE）：
    encryptedBlocks = []
    n，e =键

    for block in getBlocksFromText（message，blockSize）：
        encryptedBlocks.append（pow（block，e，n））
    返回 encryptedBlocks


def  decryptMessage（encryptedBlocks，messageLength，key，blockSize = DEFAULT_BLOCK_SIZE）：
    decryptptedBlocks = []
    n，d =键
    加密块中的块：
        decryptptedBlocks.append（pow（block，d，n））
    return getTextFromBlocks（decryptptedBlocks，messageLength，blockSize）


def  readKeyFile（keyFilename）：
    fo =  open（keyFilename）
    content = fo.read（）
    fo.close（）
    keySize，n，EorD = content.split（'，'）
    return（int（keySize），int（n），int（EorD））


def  encryptAndWriteToFile（messageFilename，keyFilename，message，blockSize = DEFAULT_BLOCK_SIZE）：
    keySize，n，e = readKeyFile（keyFilename）
    如果 keySize < blockSize *  8：
        sys.exit（“ ERROR：块大小为％s的比特和密钥大小是％S比特RSA密码需要的块尺寸为比密钥大小等于或大于要么减小块大小或使用不同的密钥。” ％（blockSize *  8，keySize））

    encryptedBlocks = encryptMessage（message，（n，e），blockSize）

    对于我的 范围（len（encryptedBlocks））：
        encryptedBlocks [i] =  str（encryptedBlocks [i]）
    encryptedContent =  '，'. join（encryptedBlocks）
    encryptedContent =  ' ％s _ ％s _ ％s ' ％（len（message），blockSize，encryptedContent）
    fo =  open（messageFilename，' w '）
    fo.write（encryptedContent）
    fo.close（）
    返回 encryptedContent


def  readFromFileAndDecrypt（messageFilename，keyFilename）：
    keySize，n，d = readKeyFile（keyFilename）
    fo =  open（messageFilename）
    content = fo.read（）
    messageLength，blockSize，encryptedMessage = content.split（' _ '）
    messageLength =  int（messageLength）
    blockSize =  int（blockSize）

    如果 keySize < blockSize *  8：
        sys.exit（' ERROR：块大小为％s位，密钥大小为％s位，RSA密码要求块大小等于或大于密钥大小，是否指定了正确的密钥文件和加密文件？' ％（blockSize *  8，keySize））

    encryptedBlocks = []
    对块中 encryptedMessage.split（' '）：
        encryptedBlocks.append（int（block））

    返回 decryptMessage（encryptedBlocks，messageLength，（n，d），blockSize）

如果 __name__  ==  ' __main__ '：
    主要（）