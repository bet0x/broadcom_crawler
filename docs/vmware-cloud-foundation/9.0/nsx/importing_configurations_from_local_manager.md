---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/getting-started-with-federation/configuring-global-and-local-managers/add-a-location/importing-lm-configs.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Importing Configurations from Local Manager
---

# Importing Configurations from Local Manager

After you successfully add a Local Manager location to the Global Manager, you can import all network and security Local Manager configurations to the Global Manager.

- The Local Manager appliance must register with the Global Manager.
- The Local Manager appliance must have a backup that you can restore in case the importing procedure fails.
- You must remove configurations for unsupported features from your Local Manager appliance. You are provided guidance in the NSX UI on how to resolve any importing conflicts.
- The Global Manager and the Local Manager must be on same version.

You can only import the entire Local Manager configuration into the Global Manager. There is no support for partial configuration import. You can only import the configurations once.

Local Manager Configurations Supported for Importing into Global Manager

- Context Profiles
- DHCP
- DNS
- Firewall Security Policies
- Gateway Profiles
- Groups
- NAT
- Security Profiles
- Services
- T0 Gateway
- T1 Gateway
- Time-based firewall (import/onboard now supported)

Local Manager Configurations Not Supported for Importing into Global Manager

The following features are not supported with NSX Federation. Import of configurations into the Global Manager is blocked if you have any of these configurations in your Local Manager. You must remove unsupported configurations to proceed with importing. After your supported Local Manager configurations are successfully imported into Global Manager, you can add the configurations for any of the unsupported features back into your Local Manager.

- DHCP dynamic binding
- Distributed IDS
- Distributed security for vCenter VDS Port Group only (Global Manager does not see the vCenter VDS port groups to assign them in security groups. However, Global Manager can use dynamic membership in groups based on vCenter VDS port groups tags added by Local Managers.)
- Endpoint protection
- Forwarding policies
- Guest introspection
- Identity firewall
- IDS/IPS
- L2 Bridge
- Load balancer
- Malware prevention
- Metadata proxy
- Multicast
- Network detection and response
- Network introspection
- Routing protocols (OSPF)
- Routing VPN and EVPN
- Service insertion
- T0 VRF
- TLS inspection
- URL filtering

If you use a load balancer in the Local Manager, you cannot import the load balancer, but you can still import other configurations if you meet certain conditions as described in the section "Importing Configurations if you have a Load Balancer service on the Local Manager".

Importing Configurations if you have a Load Balancer service on the Local Manager

If your Local Manager has a load balancer service, you can import configurations except the load balancer, if you meet the following conditions:

- The load balancer service must be in one-arm mode on a standalone tier-1 gateway.
- The standalone tier-1 gateway that the one-arm load balancer is attached to:
  - must have only the load balancer service and no other services
  - must not have any downlink segments
  - must not share Gateway Firewall rules with any other tier-0 or tier-1 gateways.
- Groups used in load balancer service must not be used in any firewall rules. If you have groups common to both load balancer and firewall rules, you must either remove the group from the firewall rule or create an identical group to use with the load balancer.

Configurations Created by a Principal Identity User in Local Manager

If you have configurations in the Local Manager that are created by the Principal Identity user and the same Principal Identity user is not present in the Global Manager, import is blocked.

You have the following options for importing these entities:

- The system displays a list of Principal Identity usernames that are being used on the Local Managerr to create configurations. Create each of these Principal Identity users in the Global Manager before proceeding to import.
- If you do not want to create Principal Identity usernames in Global Manager, remove all configurations in the Local Manager that are created using the Principal Identity username. You can then proceed with importing other configurations from the Local Manager.

1. Log in to the Global Manager and navigate to SystemLocation Manager.
2. A system message appears for each location that has been successfully added into the Global Manager and has objects that can be imported.
3. Click Import Now from the system message. You can also import objects by clicking Actions Import from the location tile.
4. You see a list of objects that can be imported into the Global Manager.
   1. If there are naming conflicts, you can provide a prefix or suffix for configurations. The total length of the object including the prefix and suffix must not exceed 256 characters. 

      The prefix or suffix gets applied to the following objects being imported:
      - Tier-0 gateway
      - Tier-1 gateway
      - Segments
      - DNS zones
      - DHCP profiles
      - Switching profiles: IPv6, VNI Pool, Gateway QoS, BFD, IPFIX
      - Security profiles: IPFIX, Flood-Protection, DNS Security, Session Timer, Context Profiles
      - L4-L7 services (all services listed under Inventory Services).The prefix or suffix does not get applied to the inventory and the firewall objects, that is: groups, firewall policies and firewall rules, and to system-created profiles and services.
   2. For other conflicts, follow the guidance provided in the UI.

Global Manager owns any Local Manager objects imported into the Global Manager. These objects appear in the Local Manager with this icon: ![GM icon](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/64e801a2-d78d-4da4-aa73-5cd6de1ea34e.original.png). You can only modify these objects from the Global Manager now.