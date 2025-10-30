---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/deploying-a-witness-appliance/configure-network-interface-for-witness-traffic.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configure Network Interface for Witness Traffic
---

# Configure Network Interface for Witness Traffic

You can separate data traffic from witness traffic in two-node vSAN clusters and vSAN stretched clusters.

- Verify that the data site to witness traffic connection has a minimum bandwidth of 2 Mbps for every 1,000 vSAN components.
- Verify the latency requirements:
  - Two-node vSAN clusters must have less than 500 ms RTT.
  - vSAN stretched clusters with less than 11 hosts per site must have less than 200 ms RTT.
  - vSAN stretched clusters with 11 or more hosts per site must have less than 100 ms RTT.
- Verify that the vSAN data connection meets the following requirements.
  - For hosts directly connected in a two-node vSAN cluster, use a 10 GbE direct connection between hosts. Hybrid clusters also can use a 1 GbE crossover connection between hosts.
  - For hosts connected to a switched infrastructure, use a 10 GbE shared connection (required for all-flash clusters), or a 1 GbE dedicated connection.
- Verify that data traffic and witness traffic use the same IP version.

vSAN data traffic requires a low-latency, high-bandwidth link. Witness traffic can use a high-latency, low-bandwidth and routable link. To separate data traffic from witness traffic, you can configure a dedicated VMkernel network adapter for vSAN witness traffic on each data host on both sites

You can add support for a direct network cross-connection to carry vSAN data traffic in a vSAN stretched cluster. You can configure a separate network connection for witness traffic. On each data host in the cluster, configure the management VMkernel network adapter to also carry witness traffic. Do not configure the witness traffic type on the witness host.

Network Address Translation (NAT) is not supported between vSAN data hosts and the witness host.

1. In the vSphere Client, navigate to the host in the cluster.
2. Click the Configure tab.
3. Under Networking, click VMkernel adapters.
4. Click ![More options](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d0a2fa31-8882-417b-baf6-6967cc170933.original.png) and click Edit.
5. Select vSAN Witness to separate vSAN witness traffic from other traffic types such as vMotion and management traffic.

The management VMkernel network interface is not selected for vSAN traffic. Do not re-enable the interface in the vSphere Client.