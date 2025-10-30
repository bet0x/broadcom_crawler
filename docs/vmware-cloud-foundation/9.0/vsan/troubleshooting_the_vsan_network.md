---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-network-design/troubleshooting-the-vsan-network.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Troubleshooting the vSAN Network
---

# Troubleshooting the vSAN Network

vSAN allows you to examine and troubleshoot the different types of issues that arise from a misconfigured vSAN network.

vSAN operations depend on the network configuration, reliability, and performance. Many support requests stem from an incorrect network configuration, or the network not performing as expected.

Use the vSAN health service to resolve network issues. Network health checks can direct you to an appropriate knowledge base article, depending on the results of the health check. The knowledge base article provides instructions to solve the network problem.

## Network Health Checks

The health service includes a category for networking health checks.

Each health check has an Ask Broadcom link. If a health check fails, click Ask Broadcom and read the associated Broadcom knowledge base article for further details, and guidance on how to address the issue at hand.

The following networking health checks provide useful information about your vSAN environment.

- vSAN: Basic (unicast) connectivity check. This check verifies that IP connectivity exists among all ESX hosts in the vSAN cluster, by pinging each ESX host on the vSAN network from each other ESX host.
- vMotion: Basic (unicast) connectivity check. This check verifies that IP connectivity exists among all ESX hosts in the vSAN cluster that have vMotion configured. Each ESX host on the vMotion network pings all other ESX hosts.
- All hosts have a vSAN vmknic configured. This check ensures each ESX host in the vSAN cluster has a VMkernel NIC configured for vSAN traffic.
- All hosts have matching subnets. This check tests that all ESX hosts in a vSAN cluster have been configured so that all vSAN VMkernel NICs are on the same IP subnet.
- Hosts disconnected from VC. This check verifies that the vCenter has an active connection to all ESX hosts in the vSAN cluster.
- Hosts with connectivity issues. This check refers to situations where vCenter lists the host as connected, but API calls from vCenter to the host are failing. It can highlight connectivity issues between a host and the vCenter.
- Network latency. This check performs a network latency check of vSAN hosts. If the threshold exceeds 5 ms, a warning is displayed.
- vMotion: MTU checks (ping with large packet size). This check complements the basic vMotion ping connectivity check. Maximum Transmission Unit size is increased to improve network performance. Incorrectly configured MTUs might not appear as a network configuration issue, but can cause performance issues.
- vSAN cluster partition. This health check examines the cluster to see how many partitions exist. It displays an error if there is more than a single partition in the vSAN cluster.

## Commands to Check the Network

When the vSAN network has been configured, use these commands to check its state. You can check which VMkernel Adapter (vmknic) is used for vSAN, and what attributes it contains.

Use ESXCLI to verify that the network is fully functional, and to troubleshoot any network issues with vSAN.

You can verify that the vmknic used for the vSAN network is uniformly configured correctly across all hosts, and verify that hosts participating in the vSAN cluster can successfully communicate with one another.

## esxcli vsan network list

This command enables you to identify the VMkernel interface used by the vSAN network.

The output below shows that the vSAN network is using vmk1. This command continues to work even if vSAN has been turned off and the hosts no longer participate in vSAN.

```
[root@esxi-dell-m:~] esxcli vsan network list
Interface
   VmkNic Name: vmk1
   IP Protocol: IP
   Interface UUID: 32efc758-9ca0-57b9-c7e3-246e962c24d0
   Agent Group Multicast Address: 224.2.3.4
   Agent Group IPv6 Multicast Address: ff19::2:3:4
   Agent Group Multicast Port: 23451
   Master Group Multicast Address: 224.1.2.3
   Master Group IPv6 Multicast Address: ff19::1:2:3
   Master Group Multicast Port: 12345
   Host Unicast Channel Bound Port: 12321
   Multicast TTL: 5
   Traffic Type: vsan
```

This provides useful information, such as which VMkernel interface is being used for vSAN traffic. In this case, it is vmk1. Port 23451 is used for the heartbeat, sent every second by the primary, and is visible on every other host in the cluster. Port 12345 is used for the CMMDS updates between the primary and backup. vSAN no longer supports multicast for any network communication.

## esxcli network ip interface list

This command enables you to verify items such as vSwitch or distributed switch.

Use this command to check which vSwitch or distributed switch that it is attached to, and the MTU size, which can be useful if jumbo frames have been configured in the environment. In this case, MTU is at the default of 1500.

```
[root@esxi-dell-m:~] esxcli network ip interface list
vmk0
   Name: vmk0
   <<truncated>>
vmk1
   Name: vmk1
   MAC Address: 00:50:56:69:96:f0
   Enabled: true
   Portset: DvsPortset-0
   Portgroup: N/A
   Netstack Instance: defaultTcpipStack
   VDS Name: vDS
   VDS UUID: 50 1e 5b ad e3 b4 af 25-18 f3 1c 4c fa 98 3d bb
   VDS Port: 16
   VDS Connection: 1123658315
   Opaque Network ID: N/A
   Opaque Network Type: N/A
   External ID: N/A
   MTU: 9000
   TSO MSS: 65535
   Port ID: 50331814
```

The Maximum Transmission Unit size is shown as 9000, so this VMkernel port is configured for jumbo frames, which require an MTU of about 9,000. VMware does not make any recommendation around the use of jumbo frames. However, jumbo frames are supported for use with vSAN.

## esxcli network ip interface ipv4 get –i vmk1

This command displays information such as IP address and netmask of the vSAN VMkernel interface.

With this information, an administrator can now begin to use other commands available at the command line to check that the vSAN network is working correctly.

```
[root@esxi-dell-m:~] esxcli network ip interface ipv4 get -i vmk1
Name  IPv4 Address  IPv4 Netmask   IPv4 Broadcast  Address Type  Gateway  DHCP DNS
----  ------------  -------------  --------------  ------------  -------  --------
vmk1  172.40.0.9   255.255.255.0   172.40.0.255   STATIC         0.0.0.0 false
```

## vmkping

The vmkping command verifies whether all the other ESX hosts on the network are responding to your ping requests.

```
~ # vmkping -I vmk2 172.32.0.3 -s 1472 -d
 PING 172.32.0.3 (172.32.0.3): 56 data bytes
 64 bytes from 172.32.0.3: icmp_seq=0 ttl=64 time=0.186 ms
 64 bytes from 172.32.0.3: icmp_seq=1 ttl=64 time=2.690 ms
 64 bytes from 172.32.0.3: icmp_seq=2 ttl=64 time=0.139 ms
 
 --- 172.32.0.3 ping statistics ---
 3 packets transmitted, 3 packets received, 0% packet loss
 round-trip min/avg/max = 0.139/1.005/2.690 ms
```

While it does not verify multicast functionality, it can help identify a rogue ESX host that has network issues. You can also examine the response times to see if there is any abnormal latency on the vSAN network.

If jumbo frames are configured, this command does not report any issues if the jumbo frame MTU size is incorrect. By default, this command uses an MTU size of 1500. If there is a need to verify if jumbo frames are successfully working end-to-end, use vmkping with a larger packet size (-s) option as follows:

```
 ~ # vmkping -I vmk2 172.32.0.3 -s 8972 -d
 PING 172.32.0.3 (172.32.0.3): 8972 data bytes
 9008 bytes from 172.32.0.3: icmp_seq=0 ttl=64 time=0.554 ms
 9008 bytes from 172.32.0.3: icmp_seq=1 ttl=64 time=0.638 ms
 9008 bytes from 172.32.0.3: icmp_seq=2 ttl=64 time=0.533 ms
 
 --- 172.32.0.3 ping statistics ---
 3 packets transmitted, 3 packets received, 0% packet loss
 round-trip min/avg/max = 0.533/0.575/0.638 ms
 ~ #
```

Consider adding -d to the vmkping command to test if packets can be sent without fragmentation.

## esxcli network ip neighbor list

This command helps to verify if all vSAN hosts are on the same network segment.

In this configuration, we have a four-host cluster, and this command returns the ARP (Address Resolution Protocol) entries of the other three hosts, including their IP addresses and their vmknic (vSAN is configured to use vmk1 on all hosts in this cluster).

```
[root@esxi-dell-m:~] esxcli network ip neighbor list -i vmk1
Neighbor     Mac Address        Vmknic   Expiry  State  Type   
-----------  -----------------  ------  -------  -----  -------
172.40.0.12  00:50:56:61:ce:22  vmk1    164 sec         Unknown
172.40.0.10  00:50:56:67:1d:b2  vmk1    338 sec         Unknown
172.40.0.11  00:50:56:6c:fe:c5  vmk1    162 sec         Unknown
[root@esxi-dell-m:~]
```

## esxcli network diag ping

This command checks for duplicates on the network, and round-trip times.

To get even more detail regarding the vSAN network connectivity between the various hosts, ESXCLI provides a powerful network diagnostic command. Here is an example of one such output, where the VMkernel interface is on vmk1 and the remote vSAN network IP of another host on the network is 172.40.0.10

```
[root@esxi-dell-m:~] esxcli network diag ping -I vmk1 -H 172.40.0.10
   Trace: 
         Received Bytes: 64
         Host: 172.40.0.10
         ICMP Seq: 0
         TTL: 64
         Round-trip Time: 1864 us
         Dup: false
         Detail: 
      
         Received Bytes: 64
         Host: 172.40.0.10
         ICMP Seq: 1
         TTL: 64
         Round-trip Time: 1834 us
         Dup: false
         Detail: 
      
         Received Bytes: 64
         Host: 172.40.0.10
         ICMP Seq: 2
         TTL: 64
         Round-trip Time: 1824 us
         Dup: false
         Detail: 
   Summary: 
         Host Addr: 172.40.0.10
         Transmitted: 3
         Recieved: 3
         Duplicated: 0
         Packet Lost: 0
         Round-trip Min: 1824 us
         Round-trip Avg: 1840 us
         Round-trip Max: 1864 us
[root@esxi-dell-m:~]
```

## Checking vSAN Network Performance

Make that there is sufficient bandwidth between your ESX hosts. This tool can assist you in testing whether your vSAN network is performing optimally.

To check the performance of the vSAN network, you can use iperf tool to measure maximum TCP bandwidth and latency. It is located in /usr/lib/vmware/vsan/bin/iperf.copy. Run it with -–help to see the various options. Use this tool to check network bandwidth and latency between ESX hosts participating in a vSAN cluster.

Broadcom knowledge base article [2001003](https://knowledge.broadcom.com/external/article?legacyId=2001003) can assist with setup and testing.

This is most useful when a vSAN cluster is being commissioned. Running iperf tests on the vSAN network when the cluster is already in production can impact the performance of the VMs running on the cluster.

## Checking vSAN Network Limits

The vsan.check.limits command verifies that none of the vSAN thresholds are being breached.

```
> ls
0 /
1 vcsa-04.rainpole.com/
> cd 1
/vcsa-04.rainpole.com> ls
0 Datacenter (datacenter)
/vcsa-04.rainpole.com> cd 0
/vcsa-04.rainpole.com/Datacenter> ls
0 storage/
1 computers [host]/
2 networks [network]/
3 datastores [datastore]/
4 vms [vm]/
/vcsa-04.rainpole.com/Datacenter> cd 1
/vcsa-04.rainpole.com/Datacenter/computers> ls
0 Cluster (cluster): cpu 155 GHz, memory 400 GbE
1 esxi-dell-e.rainpole.com (standalone): cpu 38 GHz, memory 123 GbE
2 esxi-dell-f.rainpole.com (standalone): cpu 38 GHz, memory 123 GbE
3 esxi-dell-g.rainpole.com (standalone): cpu 38 GHz, memory 123 GbE
4 esxi-dell-h.rainpole.com (standalone): cpu 38 GHz, memory 123 GbE
/vcsa-04.rainpole.com/Datacenter/computers> vsan.check_limits 0
2017-03-14 16:09:32 +0000: Querying limit stats from all hosts ...
2017-03-14 16:09:34 +0000: Fetching vSAN disk info from esxi-dell-m.rainpole.com (may take a moment) ...
2017-03-14 16:09:34 +0000: Fetching vSAN disk info from esxi-dell-n.rainpole.com (may take a moment) ...
2017-03-14 16:09:34 +0000: Fetching vSAN disk info from esxi-dell-o.rainpole.com (may take a moment) ...
2017-03-14 16:09:34 +0000: Fetching vSAN disk info from esxi-dell-p.rainpole.com (may take a moment) ...
2017-03-14 16:09:39 +0000: Done fetching vSAN disk infos
+--------------------------+--------------------+-----------------------------------------------------------------+
| Host                     | RDT                | Disks                                                           |
+--------------------------+--------------------+-----------------------------------------------------------------+
| esxi-dell-m.rainpole.com | Assocs: 1309/45000 | Components: 485/9000                                            |
|                          | Sockets: 89/10000  | naa.500a075113019b33: 0% Components: 0/0                        |
|                          | Clients: 136       | naa.500a075113019b37: 40% Components: 81/47661                  |
|                          | Owners: 138        | t10.ATA_____Micron_P420m2DMTFDGAR1T4MAX_____ 0% Components: 0/0 |
|                          |                    | naa.500a075113019b41: 37% Components: 80/47661                  |
|                          |                    | naa.500a07511301a1eb: 38% Components: 81/47661                  |
|                          |                    | naa.500a075113019b39: 39% Components: 79/47661                  |
|                          |                    | naa.500a07511301a1ec: 41% Components: 79/47661                  |
<<truncated>>
```

From a network perspective, it is the RDT associations (Assocs) and sockets count that are important. There are 45,000 associations per host in vSAN 6.0 and later. An RDT association is used to track peer-to-peer network state within vSAN. vSAN is sized so that it never runs out of RDT associations. vSAN also limits how many TCP sockets it is allowed to use, and vSAN is sized so that it never runs out of its allocation of TCP sockets. There is a limit of 10,000 sockets per host.

A vSAN client represents object's access in the vSAN cluster. The client typically represents a virtual machine running on a host. The client and the object might not be on the same host. There is no hard defined limit, but this metric is shown to help understand how clients balance across hosts.

There is only one vSAN owner for a given vSAN object, typically co-located with the vSAN client accessing this object. vSAN owners coordinate all access to the vSAN object and implement functionality, such as mirroring and striping. There is no hard defined limit, but this metric is once again shown to help understand how owners balance across hosts.