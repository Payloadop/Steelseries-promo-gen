# SteelSeries Account Generator and Promo Code Fetcher

## Overview
This script automates the process of generating SteelSeries accounts and fetching promo codes. It leverages the `mailtm` service for email registration and verification. The script performs the following tasks:

1. **Email Registration**: Creates a temporary email address using the `mailtm` service.
2. **Account Creation**: Registers a new user on the SteelSeries website.
3. **Email Verification**: Listens for a verification email and extracts the verification URL.
4. **Account Verification**: Uses the extracted URL to verify the newly created account.
5. **Promo Code Retrieval**: Fetches a promo code after successful account verification.

## Features
- **Automated Email Handling**: Utilizes the `mailtm` service to handle temporary email registration and verification.
- **Account Registration**: Automates the process of creating a new SteelSeries account.
- **Email Listener**: Listens for the verification email and extracts the verification URL.
- **Promo Code Fetching**: Retrieves promo codes post-verification and saves them to a text file.
- **Configurable Timeout**: Allows setting a timeout period for email verification.

## Requirements
- Python 3.x
- `requests`
- `tls_client`
- `mailtm`
- `Steelseries GG Client`

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Payloadop/steelseries-account-generator.git
   cd steelseries-account-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```
   python main.py
   ```

2. The script will automatically:
   - Create a new temporary email address.
   - Register a new SteelSeries account using the generated email.
   - Listen for the verification email.
   - Verify the account and fetch the promo code.

3. Promo codes will be saved in a file named `Promos.txt`.

## Configuration
- Modify the script as needed to adjust configurations such as the email service provider or timeout settings.

## Join Our Community
- Join our Discord community for support, updates, and more: [https://discord.gg/uzCQ2HzaKs](https://discord.gg/uzCQ2HzaKs)
- Looking For Saudi-Arabian's Create Ticket If U Are From SA
- Selling The Fully Automated Version Of This Tool Which Supports Proxy & Can Gen Upto 10k / hour For 250$/Lyf Key

## Contributing
Feel free to contribute by submitting issues or pull requests. Any improvements or bug fixes are welcome.

## License
This project is licensed under the MIT License.
