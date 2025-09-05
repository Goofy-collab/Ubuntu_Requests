import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for one or multiple URLs separated by commas
    urls = input("Please enter the image URL(s) (separate multiple with commas): ").split(",")

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        url = url.strip()  # Remove extra spaces
        if not url:
            continue

        try:
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            # Check headers for content type
            content_type = response.headers.get("Content-Type", "")
            if "image" not in content_type:
                print(f"✗ Skipped (not an image): {url}")
                continue

            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename:  # If no filename in URL, generate one
                filename = "downloaded_image.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # Avoid duplicates
            if os.path.exists(filepath):
                print(f"✗ Duplicate skipped: {filename}")
                continue

            # Save the image
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
