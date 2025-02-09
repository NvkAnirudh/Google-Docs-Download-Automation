# Google Docs to PDF Downloader

This Python script automates the process of downloading all Google Docs from a specific Google Drive folder and saving them as PDFs locally.

## Features

- Batch Download: Downloads all Google Docs in a specified folder.

- PDF Export: Converts Google Docs to PDFs.

- OAuth 2.0 Authentication: Uses Google Drive and Docs API for access.

- Local Storage: Saves PDFs in a specified directory.

## Prerequisites

1. Google Cloud Setup

- Create a project in [Google Cloud Console](https://cloud.google.com/?hl=en).

- Enable Google Drive API and Google Docs API.

- Generate OAuth 2.0 credentials and download the credentials.json file.

2. Install Dependencies

Ensure you have Python installed, then install the required libraries:
```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client google-cloud-storage
```

## Usage

1. Set Up Credentials

Place your credentials.json file in the same directory as the script.

2. Update Folder ID

Replace YOUR_FOLDER_ID in the script with your actual Google Drive folder ID.

3. Run the Script
```
python script.py
```

The script will authenticate, fetch Google Docs from the folder, and save them as PDFs in the downloaded_pdfs directory.

## Notes

- On first run, a browser window will open for authentication.

- A token.json file will be created to store authentication tokens.

- The script only processes Google Docs (.gdoc) and does not download other file types.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests to improve the script!

<br>

Let me know if you need modifications or additional details!