try:
    namefile = "test.jpg"
    with open(namefile, "rb") as r:
        byte = r.read(1)
        k = 0
        while byte:
            try:
                byte = r.read(1)
                print(byte)
                k += 1
            except:
                continue
except FileNotFoundError:
    print("File is not defined")
    raise SystemExit
else:
    print("[+] Number of  bytes", str(namefile) + ":" + str(k))
