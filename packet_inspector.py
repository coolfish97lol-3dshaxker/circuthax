def inspect_packet(packet):
    print("Packet inspection")
    print("------------------")
    print("Length:", len(packet), "bytes")
    print("Hex:", packet.hex(" "))

    if len(packet) == 0:
        print("Type: EMPTY")
    elif len(packet) > 1024:
        print("Type: OVERSIZED TEST PACKET")
    elif len(set(packet)) == 1:
        print("Type: REPEATED-BYTE PACKET")
    else:
        print("Type: NORMAL/RANDOM TEST PACKET")


def main():
    print("Local Packet Inspector")
    print("----------------------")

    while True:
        text = input("\nEnter hexadecimal data (or 'quit'): ")

        if text.lower() == "quit":
            break

        try:
            packet = bytes.fromhex(text)
        except ValueError:
            print("Invalid hexadecimal data.")
            continue

        inspect_packet(packet)


if __name__ == "__main__":
    main()
