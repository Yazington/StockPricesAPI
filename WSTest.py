import wealthsimple


def my_two_factor_function():
    MFACode = ""
    while not MFACode:
        # Obtain user input and ensure it is not empty
        MFACode = input("Enter 2FA code: ")
    return MFACode


if __name__ == "__main__":
    ws = wealthsimple.WSTrade(
        "binaryaz@gmail.com",
        "Gam3r4321!",
        two_factor_callback=my_two_factor_function,
    )
    # ws.
    print(ws.get_activities())
