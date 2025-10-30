---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/verify-failover-of-nsx-edge-vteps.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Verify Failover of NSX Edge VTEP Active Standby Nodes
---

# Verify Failover of NSX Edge VTEP Active Standby Nodes

In NSX Federation environment when we use stretched overlay segment for each Segment we have one Active and one Standby SR running on the NSX Edge Node.

When an active NSX Edge Node fails, the NSX Control Plane ensures the traffic failover to the standby NSX Edge node and respectively all transport nodes forward traffic to the new active NSX Edge node.

Review a topology where you have created L2 stretched overlay segments across multiple sites in your NSX Federation environment, each segment relies on two NSX Edge nodes that are in an Active/Standby configuration for cross site traffic. For example, as shown in image 1, NSX Edge 1 is Active and NSX Edge 2 is Standby node. Respectively VTEP of the Active NSX Edge will act as active L2 forwarder for all cross site traffic from all ESX Transport Node.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2fa18fd3-4d1a-4279-b866-be1c7282a3d7.original.png)

To ensure HA functionality for NSX Edge nodes, each NSX Edge node communicates the HA state to the central control plane so it knows who is the Active NSX Edge. In turn, the Control Plane communicates, VTEP group membership and HA State information received from NSX Edge node to all transport nodes that host these stretched segments.

![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/19414d2f-8f70-47da-9627-201ffeb6f7a9.original.png)

The output displays the HA state of both NSX Edge nodes. And the stale record is False, which indicates that the HA state is accurate.

To view the HA state of the Active Edge VTEP after a failover follow the procedure:

This procedure is applicable to all NSX stretched Segments used in Federation.

1. Copy the UUID of the stretched segment that is attached to a Tier-1 or Tier-0 gateway.
2. Define which is the Active Edge for that specific T1 Gateway where the segment is connected.
3. You can also use the following API to get the Active/Standby Edge for the specific Segment.

   /infra/segments/<segment-id>/inter-site-forwarder/site-span-info
4. Connect to the Edge with user: admin password.
5. Run get vtep-group to know the VTEP groups present on the NSX Edge node.
6. Verify whether the output of the get vtep-group command has the stretched segment UUID.
7. Copy the VTEP-Group ID corresponding to the segment.
8. In the NSX Manager node CLI terminal, run get vtep-group <vtep-group-ID> vteps-staleness-status.

   ```
   VNI       IP                   MAC            LABEL       Segment      TransportNode-Id                      TN-Connection   HA-STATE  STALE-RECORD

   26625     172.20.1.151     00:0c:29:9e:64:5e      0x18001    172.20.1.0   32330174-32bc-11ee-8063-000c299e6454        true         ACTIVE     False
   26625     172.20.1.152     00:0c:29:ea:8e:aa      0xFC01     172.20.1.0   914d0362-32bc-11ee-ba27-000c29ea8ea0        true        STANDBY     False
   ```
10. Run get vtep-group to know the VTEP groups present on the NSX Edge node.
11. Verify whether the output of the get vtep-group command has the stretched segment UUID.
12. Copy the VTEP-Group ID corresponding to the segment.
13. In the NSX Manager node CLI terminal, run get vtep-group <vtep-group-ID> vteps-staleness-status.

    ```
    VNI           IP                   MAC            LABEL       Segment      TransportNode-Id                      TN-Connection   HA-STATE  STALE-RECORD
    26625     172.20.1.151     00:0c:29:9e:64:5e      0x18001    172.20.1.0   32330174-32bc-11ee-8063-000c299e6454        true         ACTIVE     False
    26625     172.20.1.152     00:0c:29:ea:8e:aa      0xFC01     172.20.1.0   914d0362-32bc-11ee-ba27-000c29ea8ea0        true        STANDBY     False
    ```

    The output displays the HA state of both NSX Edge nodes. And the stale record is False, which indicates that the HA state is accurate.
14. Verify that one of the NSX Edge nodes is active and the other one is in Standby mode.
15. If the active NSX Edge goes down, the HA state mode changes. The Standby node becomes the Active node.
16. Run get vtep-group <vtep-group-ID> vteps-staleness-status.

    ```
     VNI        IP                  MAC              LABEL       Segment        TransportNode-Id                     TN-Connection   HA-STATE  STALE-RECORD
     26625   172.20.1.151    00:0c:29:9e:64:5e       0x18001    172.20.1.0    32330174-32bc-11ee-8063-000c299e6454        true         ACTIVE      True
     26625   172.20.1.152    00:0c:29:ea:8e:aa       0xFC01     172.20.1.0    914d0362-32bc-11ee-ba27-000c29ea8ea0        true         ACTIVE     False
    ```

    In the output, NSX Edge with 172.20.1.151 address has gone down and hence the Stale-Record is True.

The NSX Control Plane ensures that stale entries of failed NSX Edge nodes are correctly recorded in the output of the VTEP groups.