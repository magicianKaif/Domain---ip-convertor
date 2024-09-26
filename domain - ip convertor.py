import urllib.parse

def get_ip(address):
    try:
        url = "http://" + address
        domain = urllib.parse.urlparse(url).netloc()
        return domain.split("[")[0]
    except ValueError:
        print(f"Invalid domain: {address}")
        return None

def main():
    website = input("Enter a website URL: ")

    if website is None:
        print("Please provide a valid website URL.")
    else:
        ip_address = get_ip(website)
        if ip_address is None:
            print(f"Failed to fetch IP address for {website}.")
        else:
            print(f"Website: {website}\nIP Address: {ip_address}")

if __name__ == "__main__":
    main()