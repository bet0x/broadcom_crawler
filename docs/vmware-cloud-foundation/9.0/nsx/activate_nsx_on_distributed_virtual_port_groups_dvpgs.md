---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/quick-start-wizard-to-prepare-clusters-for-networking-and-security/activate-distributed-security-for-vds.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Activate NSX on Distributed Virtual Port Groups (DVPGs)
---

# Activate NSX on Distributed Virtual Port Groups (DVPGs)

NSX allows distributed security across all ports within the DVPGs found in a host cluster. As the host switch is of the type VDS, you can enable DFW capabilities on workload VMs.

The following are the requirements for installing Distributed Security for VDS:

- The vSphere cluster must have at least one VDS configured and ESX cluster hosts must be members of a VDS with uplinks configured.
- A compute manager must be registered in NSX. See [Add a Compute Manager](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1.html#GUID-75c7ad86-09a2-4935-acec-17e9c9332251-en).
- Before you deploy and configure Distributed Security on hosts, ensure that NSX is not deployed on such hosts.

DFW supports both DVPGs created in vSphere and segments created in NSX within the same cluster.

Distributed Security provides security-related functionality to your VDS such as:

- Distributed Firewall (DFW)
- Distributed IDS/IPS
- Identity Firewall
- L7 App ID
- Fully Qualified Domain Name (FQDN) Filtering
- Security Intelligence
- NSX Malware Prevention
- NSX Guest Introspection

After you activate security on DVPGs, DVPG ports and DVPG segments are discovered by NSX.

1. From your browser, log in with admin privileges to an NSX Manager at [https://<nsx-manager-ip-address](_about_blank)>.
2. Navigate to System > Quick Start > Host Cluster Preparation.
3. On the Prepare Clusters for Networking and Security card, click Get Started.
4. Select the clusters where you want to activate distributed security.
5. Click Install NSX and under Networking, choose either VLAN or Overlay.

   Choosing VLAN enables only NSX VLAN Networking.
6. In the dialog box, click Install.
7. Navigate to the System > Fabric > Hosts page to activate security on DVPG within a cluster.
8. On the Hosts > Cluster page, select the cluster on which you want to activate security on the DVPGs within the cluster.

   Ensure you select all clusters where the VDS spans. If you leave out a cluster that VDS spans, security will not be activated on DVPGs of that cluster.
9. On the Hosts page, click Actions > Activate NSX on DVPGs.

   Before you activate NSX on DVPGs, protect all the management appliances by adding them to the distributed firewall exclusion list. Sometimes, if "Actions > Activate NSX on DVPGs" is performed immediately after "Actions > Deactivate NSX on DVPGs" hosts may be in a partial success state. To work around this issue, create a dummy DVPG under the Hosts located DVS in the VC. Hosts will retrigger the sync process, and be fully successful.
10. On the Activate NSX on DVPGs card, click Yes to activate the DVPGs.

    NSX discovers the port groups associated to the VDS switch. To learn more about how to find the discovered ports in NSX, see [Distributed Port Groups](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/segments/distributed-port-groups.html).
11. To deactivate security on DVPGs within a cluster:
    1. On the Hosts > Cluster page, select the cluster on which you want to deactivate security on the DVPGs within the cluster.
    2. On the Hosts page, click Actions > Deactivate NSX on DVPGs.

After successfully activating security on a cluster, on the Hosts page, the NSX on DVPGs column status is updated to Yes. Distributed Security is installed and you can begin using security capabilities such as creating DFW policies and rules for the VDS.

The system creates distributed port group segments under the default security transport zones described in [Create Transport Zones](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/create-transport-zones.html).