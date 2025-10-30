---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/understanding-vsan-networking/network-requirements-for-vsan/network-firewall-requirements.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Network Firewall Requirements
---

# Network Firewall Requirements

When you configure the network firewall, consider which version of vSAN you are deploying.

When you enable vSAN on a cluster, all required ports are added to ESXfirewall rules and configured automatically. You do not need to open any firewall ports or enable any firewall services manually. You can view open ports for incoming and outgoing connections in the ESX host security profile (Configure > Security Profile).

vsanEncryption Firewall Rule

If your cluster uses vSAN encryption, consider the communication between hosts and the KMS server.

vSAN encryption requires a Key Management Server (KMS). vSAN can use a vCenter Native Key Provider or an external KMS. vCenter obtains the key IDs from the KMS, and distributes them to the ESX hosts. KMS servers and ESX hosts communicate directly with each other. KMS servers might use different port numbers, so the vsanEncryption firewall rule enables you to simplify communication between each vSAN host and the KMS server. This allows a vSAN host to communicate directly to any port on a KMS server (TCP port 0 through 65535).

When a host establishes communication to a KMS server, the following operations occur.

- The KMS server IP is added to the vsanEncryption rule and the firewall rule is enabled.
- Communication between vSAN node and KMS server is established during the exchange.
- After communication between the vSAN node and the KMS server ends, the IP address is removed from vsanEncryption rule, and the firewall rule is deactivatedagain.

vSAN hosts can communicate with multiple KMS hosts using the same rule.