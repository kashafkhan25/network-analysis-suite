from scapy.all import sniff, IP, TCP, UDP, ICMP, wrpcap

print("-" * 50)
print("Starting Packet Sniffer... Capturing 50 packets.")
print("Live traffic will print below, and save to a file.")
print("-" * 50)

# This list will temporarily hold the captured packets in memory so we can save them
captured_packets = []

def process_packet(packet):
    # Keep track of every packet captured
    captured_packets.append(packet)
    
    # Check if the packet has an IP layer (Layer 3)
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Determine the protocol name
        proto_name = "OTHER"
        if packet.haslayer(TCP):
            proto_name = "TCP"
        elif packet.haslayer(UDP):
            proto_name = "UDP"
        elif packet.haslayer(ICMP):
            proto_name = "ICMP"
            
        print(f"[+] {proto_name} Packet: {src_ip} -> {dst_ip}")

# Start sniffing. 'count=50' stops the script automatically after 50 packets.
sniff(prn=process_packet, count=50)

print("\n" + "-" * 50)
print("Sniffing complete. Saving packets...")

# Save the packets to a standard PCAP file format
wrpcap("captured_traffic.pcap", captured_packets)

print("SUCCESS: Packets saved to 'captured_traffic.pcap'.")
print("-" * 50)
