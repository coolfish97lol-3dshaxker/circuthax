import random


def test_parser(data):
    """
    A deliberately simple parser that we control.
    This is NOT a real Switch parser.
    """

    if len(data) < 2:
        raise ValueError("Packet too short")

    packet_type = data[0]
    packet_length = data[1]

    if packet_length > len(data) - 2:
        raise ValueError("Declared length is too large")

    return packet_type, packet_length


def make_test_packet():
    size = random.randint(0, 100)

    return bytes(
        random.randint(0, 255)
        for _ in range(size)
    )


def main():
    crashes = 0

    for number in range(1000):
        packet = make_test_packet()

        try:
            test_parser(packet)

        except Exception as error:
            crashes += 1

            print(
                f"[!] Test {number}: "
                f"{type(error).__name__}: {error}"
            )

            print("    Data:", packet.hex(" "))

    print()
    print("Testing finished.")
    print("Errors detected:", crashes)


if __name__ == "__main__":
    main()
