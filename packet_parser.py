import random


def make_packet():
    packet_types = [
        "empty",
        "oversized",
        "random",
        "repeated",
        "truncated"
    ]

    packet_type = random.choice(packet_types)

    if packet_type == "empty":
        return b""

    elif packet_type == "oversized":
        size = random.randint(256, 4096)
        return b"A" * size

    elif packet_type == "random":
        size = random.randint(1, 256)
        return bytes(random.randint(0, 255) for _ in range(size))

    elif packet_type == "repeated":
        value = random.randint(0, 255)
        size = random.randint(1, 512)
        return bytes([value]) * size

    elif packet_type == "truncated":
        return bytes.fromhex("01 02 03")


def main():
    print("Malformed Packet Generator")
    print("--------------------------")

    for number in range(10):
        packet = make_packet()

        print(
            f"Packet {number + 1}: "
            f"{len(packet)} bytes | "
            f"{packet.hex(' ')}"
        )


if __name__ == "__main__":
    main()
