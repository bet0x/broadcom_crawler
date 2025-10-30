---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/add-a-kms-to-vcenter-server.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Add a KMS to vCenter
---

# Add a KMS to vCenter

You add a Key Management Server (KMS) to your vCenter system from the vSphere Client.

- Verify that the key server is in the vSphere Compatibility Matrices and is KMIP 1.1 compliant.
  - Verify that you have the required privileges: Cryptographer.ManageKeyServers
- Connecting to a KMS by using only an IPv6 address is not supported.
- Connecting to a KMS through a proxy server that requires user name or password is not supported.

vCenter creates a KMS cluster when you add the first KMS instance. If you configure the KMS cluster on two or more vCenters, make sure you use the same KMS cluster name.

Do not deploy your KMS servers on the vSAN cluster you plan to encrypt. If a failure occurs, hosts in the vSAN cluster must communicate with the KMS.

- When you add the KMS, you are prompted to set this cluster as a default. You can later change the default cluster explicitly.
- After vCenter creates the first cluster, you can add KMS instances from the same vendor to the cluster.
- You can set up the cluster with only one KMS instance.
- If your environment supports KMS solutions from different vendors, you can add multiple KMS clusters.

1. Navigate to vCenter.
2. Click Configure tab.
3. Browse the inventory list and select the vCenter instance.
4. Under Security, click Key Providers.
5. Click Add KMS, specify the KMS information in the wizard, and click OK. 

   Option | Value || KMS cluster | Select Create new cluster for a new cluster. If a cluster exists, you can select that cluster. |
   | Cluster name | Name for the KMS cluster. You can use this name to connect to the KMS if your vCenter instance becomes unavailable. |
   | Server alias | Alias for the KMS. You can use this alias to connect to the KMS if your vCenter instance becomes unavailable. |
   | Server address | IP address or FQDN of the KMS. |
   | Server port | Port on which vCenter connects to the KMS. |
   | Proxy address | Optional proxy address for connecting to the KMS. |
   | Proxy port | Optional proxy port for connecting to the KMS. |
   | User name | Some KMS vendors allow users to isolate encryption keys that are used by different users or groups by specifying a user name and password. Specify a user name only if your KMS supports this functionality, and if you intend to use it. |
   | Password | Some KMS vendors allow users to isolate encryption keys that are used by different users or groups by specifying a user name and password. Specify a password only if your KMS supports this functionality, and if you intend to use it. |