## Introduction

This repository contains Python code that uses the `requests` library to interact with the TikTok API for the purpose of following users. The program sends an HTTP request to the TikTok server to follow a specific user.

## Requirements

To ensure this code runs correctly, make sure you have the following packages installed:

- requests  
- Gorgon 
- Argus
- Ladon 


## Usage Instructions

1. **Configure Variables**:
   - Set up the following variables with your TikTok data:
     - `iid`: Unique device identifier.
     - `did`: Device ID.
     - `uid`: User ID.
     - `secuid`: User security ID.

2. **Modify Settings**:
   - Ensure you have modified the headers to meet the requirements of the TikTok API.
   - You can change `item_id` and `channel_id`, among other parameters in the `base_params()` function as needed.

3. **Run the Code**:
   - After setting the variables and headers, you can run the code. It may take some time depending on internet speed and server response.

## How the Code Works

### Main Functions

- **sign(params, payload, sec_device_id, cookie, aid, license_id, sdk_version_str, sdk_version, platform, unix)**:
  - This function signs the input data using cryptographic techniques and the utilized libraries (`Gorgon`, `Argus`, `Ladon`).

- **base_params()**:
  - This function returns the essential parameters required for the HTTP request.

- **algo()**:
  - This function calls the signing function and returns the signature values used in the requests.

### Sending the Request

- The request is sent to the API using `requests`, including the required parameters and headers.

### Handling the Response

- The response from the server is printed in JSON format, allowing you to view the returned data.

## Contributing

If you would like to contribute to improving the code or adding new features, feel free to open an issue or submit a Pull Request.

## License

This code is available for personal use, and the author takes no responsibility for any illegal or unauthorized use.

## Telegram Channel

For updates and discussions, you can join the Telegram channel: [SizaGodCh](https://t.me/SizaGodCh)
