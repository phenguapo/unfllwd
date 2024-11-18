# unfllwd
### unfllwd is a web application designed to help users identify Instagram™ accounts that they follow but do not follow back. The application processes HTML files downloaded from Instagram™ to generate a list of such accounts.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Important Information](#important-information)
- [How to Download Your Instagram™ Data](#how-to-download-your-instagram-data)
  
## Features 
- Upload HTML files of Instagram™ followers and followings
- Identify users who do not follow you back
- Copy the results to clipboard
- Download the results as a text file

## Requirements
- Python 3.x
- Flask
- BeautifulSoup4
- Werkzeug

## Installation
1. Clone the repository:
```bash
git clone https://github.com/phenguapo/unfllwd.git
cd unfllwd
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Usage
Run the Flask application:
```bash
python app.py
```

5. Open your web browser and navigate to http://127.0.0.1:5000/.

6. Upload your Instagram™ data files:
  - Followers HTML file (followers_1.html)
  - Following HTML file (following.html)

7. View the results:
The application will display the users you are following but who are not following you back.
You can copy the results to the clipboard or download them as a text file.

## Contributing
1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin feature-branch)
5. Create a new Pull Request

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Important Information:
This application does not store any personal information.
The data you upload contains only your follower and following lists.
We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with Instagram™ or Meta™.
For any issues or questions, please contact the repository owner at [gdamigos@proton.me].

### How to Download Your Instagram™ Data
- Open Instagram™ and go to Settings.
- Navigate to "Accounts Center".
- Select "Your Information and Permissions".
- Click on "Download Your Information".
- Choose "Download or Transfer Information".
- Select your account and press "Next".
- Choose "Some of Your Information", then select "Followers and Following".
- Choose "Download to Device", then "Next".
- Set the Date Range to "All Time" and click "Create Files".
- Wait 3-5 minutes for the process to complete.
- Download the .zip file.
- Extract the "connections" folder.
- Navigate to the "followers and following" folder.
- Upload "followers_1.html" and "following.html" files to unfllwd.

**Created by phenguapo in 2024.**
