import pyshark
import json
import sys

def convert_pcap_to_json(pcap_file, output_file):
    try:
        cap = pyshark.FileCapture(pcap_file)
        packets_list = [packet._json for packet in cap]

        with open(output_file, "w") as f:
            json.dump(packets_list, f, indent=4)

        print(f"Conversion complete. JSON saved as {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_pcap.py input.pcap output.json")
        sys.exit(1)

    input_pcap = sys.argv[1]
    output_json = sys.argv[2]

    convert_pcap_to_json(input_pcap, output_json)
