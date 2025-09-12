import requests
import os
from urllib.parse import urlparse

# Create flags directory if it doesn't exist
os.makedirs('flags', exist_ok=True)

# List of all country codes used in the project
country_codes = [
    # Europe
    'ad', 'at', 'be', 'bg', 'by', 'ch', 'cy', 'cz', 'de', 'dk', 'ee', 'es', 'fi', 'fr', 'gb', 'ge', 'gr', 'hr', 'hu', 'ie', 'is', 'it', 'li', 'lt', 'lu', 'lv', 'mc', 'md', 'me', 'mk', 'mt', 'nl', 'no', 'pl', 'pt', 'ro', 'rs', 'ru', 'se', 'si', 'sk', 'sm', 'ua', 'va', 'xk', 'al', 'ba',
    
    # North America
    'us', 'ca', 'mx', 'gt', 'bz', 'sv', 'hn', 'ni', 'cr', 'pa', 'cu', 'jm', 'ht', 'do', 'bs', 'bb', 'tt', 'gd', 'vc', 'lc', 'dm', 'ag', 'kn',
    
    # South America
    'br', 'ar', 'co', 've', 'gy', 'sr', 'pe', 'ec', 'bo', 'py', 'uy', 'cl',
    
    # Asia
    'cn', 'jp', 'kr', 'kp', 'mn', 'tw', 'id', 'th', 'vn', 'ph', 'my', 'sg', 'mm', 'kh', 'la', 'bn', 'tl', 'in', 'pk', 'bd', 'lk', 'np', 'bt', 'mv', 'kz', 'uz', 'tm', 'kg', 'tj', 'tr', 'ir', 'iq', 'sy', 'lb', 'jo', 'il', 'ps', 'sa', 'ae', 'kw', 'qa', 'bh', 'om', 'ye', 'af',
    
    # Oceania
    'au', 'nz', 'pg', 'fj', 'sb', 'vu', 'fm', 'mh', 'pw', 'nr', 'ki', 'ws', 'to', 'tv',
    
    # Africa
    'eg', 'ly', 'tn', 'dz', 'ma', 'sd', 'ng', 'gh', 'ci', 'sn', 'ml', 'bf', 'ne', 'gn', 'sl', 'lr', 'tg', 'bj', 'gw', 'gm', 'cv', 'cd', 'cg', 'cm', 'cf', 'td', 'ga', 'gq', 'st', 'ao', 'et', 'ke', 'tz', 'ug', 'rw', 'bi', 'so', 'dj', 'er', 'ss', 'za', 'na', 'bw', 'zw', 'zm', 'mw', 'mz', 'mg', 'mu', 'sc', 'km', 'ls', 'sz', 'mr'
]

base_url = "https://flagcdn.com/w320/"

def download_flag(country_code):
    """Download flag image for a given country code"""
    url = f"{base_url}{country_code}.png"
    filename = f"flags/{country_code}.png"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"Downloaded {country_code}.png")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {country_code}.png: {e}")
        return False

def main():
    print(f"Starting download of {len(country_codes)} flag images...")
    
    successful = 0
    failed = 0
    
    for code in country_codes:
        if download_flag(code):
            successful += 1
        else:
            failed += 1
    
    print(f"\nDownload complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {len(country_codes)}")

if __name__ == "__main__":
    main()
