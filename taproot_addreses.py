import csv
from bitcoinutils.setup import setup
from bitcoinutils.keys import P2trAddress, PrivateKey

def main():
    # Always remember to setup the network
    setup('mainnet')

    # Generate a new private key
    priv_key = PrivateKey()

    # Instantiate from existing WIF key
    priv = PrivateKey.from_wif(priv_key.to_wif())

    # Get the public key
    pub = priv.get_public_key()

    # Get address from public key
    address = pub.get_taproot_address()

    # Return private key WIF and Taproot address
    
    return priv.to_wif(), address.to_string()

if __name__ == "__main__":
    num_addresses = int(input("Enter the number of addresses to generate: "))

    # Open a CSV file to write
    with open('taproot_addresses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['Private Key WIF', 'Native Address'])

        # Generate the specified number of Taproot addresses
        for _ in range(num_addresses):
            wif, address = main()
            print(_,"-> ",address)
            # Write the data to CSV
            writer.writerow([wif, address])
