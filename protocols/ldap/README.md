## ldap ports 389, 636, 3268, 3269

LDAP (Lightweight Directory Access Protocol) locates organizations, individuals, and other resources such as files and devices in a network.  
Often used in combination of Kerberos and AC (Active Directory)

## enumeration

using nmap:

```bash
nmap -n -sV --script "ldap* and not brute" 10.10.11.241
```

using ldapsearch:

```bash
$ ldapsearch -x -H ldap://<IP> -s base namingcontexts

# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingcontexts 
#

#
dn:
namingcontexts: DC=hospital,DC=htb
namingcontexts: CN=Configuration,DC=hospital,DC=htb
namingcontexts: CN=Schema,CN=Configuration,DC=hospital,DC=htb
namingcontexts: DC=DomainDnsZones,DC=hospital,DC=htb
namingcontexts: DC=ForestDnsZones,DC=hospital,DC=htb

# search result
search: 2
result: 0 Success
```

Next, we can check for a null-bind on the LDAP:

```bash
$ ldapsearch -x -H ldap://<IP> -b DC=hospital,DC=ht
```

