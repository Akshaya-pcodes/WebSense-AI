import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import ipaddress
import socket


def is_valid_public_url(url):

    try:
        parsed_url = urlparse(url)

        if parsed_url.scheme not in ["http", "https"]:
            return False

        hostname = parsed_url.hostname

        if not hostname:
            return False

        if hostname.lower() == "localhost":
            return False

        ip_addresses = socket.getaddrinfo(
            hostname,
            None,
            type=socket.SOCK_STREAM
        )

        for address in ip_addresses:

            ip = ipaddress.ip_address(
                address[4][0]
            )

            if (
                ip.is_private
                or ip.is_loopback
                or ip.is_link_local
                or ip.is_reserved
                or ip.is_unspecified
                or not ip.is_global
            ):
                return False

        return True

    except Exception as error:
        print("URL Validation Error:", error)
        return False


def extract_website_content(url):

    try:
        url = url.strip()

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        # Validate URL
        if not is_valid_public_url(url):
            return {
                "error": "Invalid or restricted website URL."
            }

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
            )
        }

        # Request website
        response = requests.get(
            url,
            headers=headers,
            timeout=(5, 15),
            allow_redirects=False
        )

        response.raise_for_status()

        # Check content type
        content_type = response.headers.get(
            "Content-Type", ""
        ).lower()

        if "text/html" not in content_type:
            return {
                "error": "This URL does not contain an HTML webpage."
            }

        # Extract HTML
        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Remove unnecessary elements
        for element in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "noscript",
            "iframe"
        ]):
            element.decompose()

        # Extract title
        title = "Untitled Website"

        if soup.title and soup.title.string:
            title = soup.title.string.strip()

        # Extract description
        description_tag = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        description = ""

        if description_tag:
            description = description_tag.get(
                "content", ""
            )

        # Extract readable content
        content = soup.get_text(
            separator=" ",
            strip=True
        )

        content = " ".join(content.split())

        # Check extracted content
        if not content:
            return {
                "error": "No readable content found on this website."
            }

        # Limit content length
        content = content[:12000]

        return {
            "title": title,
            "description": description,
            "content": content
        }

    except requests.exceptions.Timeout:
        return {
            "error": "Website connection timed out. Please try again."
        }

    except requests.exceptions.ConnectionError:
        return {
            "error": "Unable to connect to this website. Check the URL or internet connection."
        }

    except requests.exceptions.HTTPError as error:
        return {
            "error": f"Website returned an HTTP error: {error}"
        }

    except requests.exceptions.RequestException as error:
        return {
            "error": f"Website request failed: {error}"
        }

    except Exception as error:
        print("Extractor Error:", error)

        return {
            "error": "Something went wrong while extracting website content."
        }