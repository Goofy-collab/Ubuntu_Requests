### 🌍 Ubuntu-Inspired Image Fetcher

This project is a simple Python script that fetches images from the web, saves them locally, and organizes them in a folder called **`Fetched_Images`**.

It is inspired by the Ubuntu principle of community, sharing, and respect — connecting to the wider web community while handling errors gracefully.

---

## ✨ Features

* Fetch images from a provided URL
* Create a `Fetched_Images` directory if it doesn’t exist
* Save images with the correct filename (or generate one if missing)
* Handle errors gracefully (connection errors, invalid URLs, etc.)
* Prevent duplicate downloads
* Check HTTP headers to confirm the file is an image

---

## 🛠️ Requirements

* Python **3.7+** (tested on Python 3.13.5)
* `requests` library

Install dependencies with:

```bash
python -m pip install requests
```

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/Ubuntu_Requests.git
   cd Ubuntu_Requests
   ```

2. Run the script:

   ```bash
   python ubuntu_fetcher.py
   ```

3. Enter one or multiple image URLs when prompted (separated by commas).

4. Images will be saved inside the **Fetched\_Images** directory.

---

## 📖 Example Output

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.
```

---

## 🧠 Challenge Extensions

* Support multiple URLs at once 
* Add precautions when downloading from unknown sources 
* Prevent duplicate downloads 
* Check HTTP headers before saving

---
