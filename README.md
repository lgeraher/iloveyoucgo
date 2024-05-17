```
 ___          ___       ________  ___      ___ _______            ___    ___ ________  ___  ___          ________  ________  ________     
|\  \        |\  \     |\   __  \|\  \    /  /|\  ___ \          |\  \  /  /|\   __  \|\  \|\  \        |\   ____\|\   ____\|\   __  \    
\ \  \       \ \  \    \ \  \|\  \ \  \  /  / | \   __/|         \ \  \/  / | \  \|\  \ \  \\\  \       \ \  \___|\ \  \___|\ \  \|\  \   
 \ \  \       \ \  \    \ \  \\\  \ \  \/  / / \ \  \_|/__        \ \    / / \ \  \\\  \ \  \\\  \       \ \  \    \ \  \  __\ \  \\\  \  
  \ \  \       \ \  \____\ \  \\\  \ \    / /   \ \  \_|\ \        \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \____\ \  \|\  \ \  \\\  \ 
   \ \__\       \ \_______\ \_______\ \__/ /     \ \_______\     __/  / /      \ \_______\ \_______\       \ \_______\ \_______\ \_______\
    \|__|        \|_______|\|_______|\|__|/       \|_______|    |\___/ /        \|_______|\|_______|        \|_______|\|_______|\|_______|
                                                                \|___|/                                                                   
                                                                                                                                          
```

# AWS Lambda. Layers, Triggers and Deployment (with real examples)

## Overview

This project contains an AWS Lambda function named `I_Love_You_CGO.py`. The function is designed to read XML files from an S3 bucket, convert the XML content to JSON, and then insert the JSON data into a MongoDB collection.

## Features

- **Read from S3**: Automatically triggered by S3 events when a new XML file is uploaded.
- **XML to JSON Conversion**: Uses `xmltodict` to convert XML data to JSON.
- **MongoDB Insertion**: Inserts the converted JSON data into a specified MongoDB collection.

## Agenda

- Create the S3 bucket
- Create the function with custom IAM role
- Add trigger
- Configure source code
- Configure handler
- Configure environment variables
- Test the function to see it fail
- Create the layers
  - `pip install xmltodict --upgrade --no-cache-dir -t .`
  - `pip install pymongo --upgrade --no-cache-dir -t .`
- Add the layers
- Test the function to see it fail
- Adjust the timeout
- Test the function to see it work
- Q&A

## Setup

### Prerequisites

- AWS account with access to Lambda, S3, and IAM.
- MongoDB instance (either MongoDB Atlas or a self-hosted instance).
- Python environment with the required dependencies.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/lgeraher/ILoveYouCGO ILoveYouCGO
   cd ILoveYouCGO
   ```

### Configuration

1. **AWS Configuration**:
   - Set up an IAM role with the necessary permissions for Lambda, S3, and MongoDB access.
   - Ensure your Lambda function has environment variables set for `MONGO_URI`.

2. **Environment Variables**:
   - `MONGO_URI`: MongoDB connection string.

## Usage

Once deployed, the Lambda function will be triggered automatically whenever an XML file is uploaded to the specified S3 bucket. The function will process the file, convert the XML content to JSON, and store it in MongoDB.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [Luis Gerardo Hernandez](mailto:gerardo.hernandez@improving.com).

## Special Thanks

I want to express my deepest gratitude and special thanks to my wife Cecilia for her unwavering support, love, and encouragement in every aspect of my life. None of this would have been possible without her constant belief in me and her incredible patience. She is not just my biggest inspiration but also the most important source of strength and resilience, which has been truly mighty in every sense. Thank you, Cecilia, for being my rock and for always being there for me.
