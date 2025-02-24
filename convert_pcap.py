import pyshark
import json
import sys
import requests

def download_pcap(url, filename="downloaded.pcap"):
    """Download PCAP file from a given URL."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded PCAP file: {filename}")
        return filename
    except Exception as e:
        print(f"Error downloading PCAP: {e}")
        sys.exit(1)

def convert_pcap_to_json(pcap_file, output_file):
    """Convert a PCAP file to JSON format."""
    try:
        cap = pyshark.FileCapture(pcap_file)
        packets_list = [packet._json for packet in cap]

        with open(output_file, "w") as f:
            json.dump(packets_list, f, indent=4)

        print(f"Conversion complete. JSON saved as {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_pcap.py <pcap_url> <output.json>")
        sys.exit(1)

    pcap_url = sys.argv[1]
    output_json = sys.argv[2]

    pcap_file = download_pcap(pcap_url)
    convert_pcap_to_json(pcap_file, output_json)
