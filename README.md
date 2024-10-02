# Shorts Maker
Shorts Maker - Python App used for making youtube shorts and having fun

## Requirements
- Python 3.10 or higher
- Pexels API key ([free]("https://www.pexels.com/api/"))
- **Dependencies**: Install the following Python libraries:
  - `pyttsx3`: For text-to-speech functionality.
  - `pexelsPy`: To interact with the Pexels API for video downloads.
  - `requests`: For making HTTP requests to download videos.
  - `shutil`: For file operations such as copying or removing directories.
  - `gpt4all`: To use the GPT-4 model for generating responses.

## Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/BAK3701/ShortsMaker
    ```
2. **Install the required dependencies**
    ```bash
    pip install pyttsx3 pexelsPy requests gpt4all
    ```
3. **Edit the pexel.py file and add your API key**
   ```bash
   PEXELS_API = 'YOUR_API_KEY_HERE'
   ```
4. **Run the application**
   ```bash
   python main.py
   ```
## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.
   

