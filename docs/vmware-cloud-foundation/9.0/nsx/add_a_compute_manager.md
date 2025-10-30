---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/add-a-compute-manager-1.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Compute Manager
---

# Add a Compute Manager

A compute manager, for example, vCenter, is an application that manages resources such as hosts and VMs.

- Verify that you are using the supported vSphere version. See [Supported vSphere version](http://partnerweb.vmware.com/comp_guide/sim/interop_matrix.php).
- Verify that you have IPv4 communication with vCenter.
- Verify that you use the recommended number of compute managers. See [VMware Configuration Maximums](https://configmax.broadcom.com/home).
- Decide the hashing algorithm type you want to use for stamping NSX Manager thumbprint in compute manager extension. SHA1 and SHA256 algorithm types are supported. The default is SHA1. If you use SHA256 there might be communication issues between WCP component in VC and NSX Manager.
  - To set the hashing algorithm, run API PUT https://<nsx-mgr>/api/v1/fabric/compute-managers/thumbprint-hashing-algorithm

    ```
    {
       "hashing_algorithm_type": "SHA1"
    }
    ```

- For Day-0 operations, provide the credentials of a vCenter user.

  - These credentials will be used only on Day-0 for NSX to communicate with vCenter. NSX will not store these credentials in its database.
  - You can provide the credentials of a vCenter administrator, or create a role and a user specifically for NSX and provide this user's credentials. Go to the AdministrationGlobal Permissions tab. Add global permissions to the newly created user and role and select Propagate to Children.

    ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4f0bffe0-4e59-4ab4-b063-1477c0c820f3.original.png)
  - Create a custom role with the following vCenter privileges:

    |  |  |
    | --- | --- |
    | Global | Cancel task |
    | Extension | Register extension |
    | Extension | Unregister extension |
    | Extension | Update extension |
    | Host | Configuration.Maintenance |
    | Host | Configuration.NetworkConfiguration |
    | Host | Local Operations.Create virtual machine |
    | Host | Local Operations.Delete virtual machine |
    | Host | Local Operations.Reconfigure virtual machine |
    | Network | Assign network |
    | Permissions | Reassign role permissions |
    | Resource | Assign vApp to resource pool |
    | Resource | Assign virtual machine to resource pool |
    | Sessions | Message |
    | Sessions | Validate session |
    | Sessions | View and stop sessions |
    | Scheduled task | Select all privileges |
    | Tasks | Select all privileges |
    | vApp | Select all privileges |
    | Virtual Machine. | Configuration |
    | Virtual Machine | Guest Operations |
    | Virtual Machine | Provisioning |
    | Virtual Machine | Inventory |

NSX polls compute managers to collect cluster information from vCenter.

For more information about vCenter roles and privileges, see the vSphere Security document.

1. From your browser, log in with admin privileges to an NSX Manager at https://<nsx-manager-ip-address> or https://<nsx-manager-fqdn>.
2. Select SystemFabricCompute
   ManagersAdd Compute
   Manager.
3. Complete the compute manager details.

   Option | Description || Name | Type the name to identify the vCenter instance. |
   | FQDN or IP Address | Type the FQDN or IP address of the vCenter instance. |
   | User Name | Type the user name to log in to the vCenter instance. |
   | Password | Type the password. |
   | HTTPS Port | The default port is 443. If you use another port, verify that the port is open on all the NSX Manager appliances. |
   | VPC Access in vSphere Client | Defines representation and consumption of VPCs from default Project in the vCenter instance:  - Full Access - VPC and subnet available for configuration from vCenter. This option is enabled by default. - Read Only - VPC and subnet available in vCenter for read only access from vCenter - Disabled - None of the VPC objects in vCenter network are represented as port group under relevant VDS |
   | Description | Enter a description. |
   | Tag | Enter a tag. |
4. Click Save.
5. Click Confirm to accept the server provided thumbprint.
6. If the progress icon changes from In progress to Not registered, perform the following steps to resolve the error instead of editing Compute Manager.
   1. Select the error message and click Resolve. One possible error message is the following:Extension already registered at CM <vCenter name> with id <extension ID>
   2. (Optional) If prompted, enter the vCenter credentials.
   3. Click Resolve.

      If an existing registration exists, it will be replaced.

It takes some time for NSX to register the compute manager with vCenter and for the connection status to appear as UP.

You can click the compute manager's name to view the details, edit the compute manager, or manage tags that apply to the compute manager.

After vCenter is successfully registered, the vCenter instance's Trusted Root CA certificate can be seen on SystemCertificates tab under the miscellaneous category.

Unregistering a compute manager from NSX deletes the service account for that NSX deployment in the VC instance.

After you successfully register the vCenter instance, do not power off and delete all NSX Manager VMs without first unregistering that vCenter instance. Otherwise, you will not be able to register that vCenter instance again when you deploy a new NSX Manager node. An error message will state that the vCenter instance is already registered with another NSX Manager. To resolve this error, use the Resolve action on the Compute Managers page.

After a vCenter (VC) compute manager is successfully added, it cannot be removed if you successfully performed any of the following actions:

- Transport nodes are prepared using VDS that is dependent on the VC.
- Service VMs deployed on a host or a cluster in the VC using NSX service insertion.
- You use the NSX Manager UI to deploy Edge VMs or NSX Manager nodes on a host or a cluster in the VC.

If you try to perform any of these actions and you encounter an error (for example, installation failed), you can remove the VC if you have not successfully performed any of the actions listed above.

If you have successfully prepared any transport node using VDS that is dependent on the VC or deployed any VM, you can remove the VC after you have done the following:

- Unprepare all transport nodes. If uninstalling a transport node fails, you must force delete the transport node.
- Undeploy all service VMs, all NSX Edge VMs, and all NSX Manager nodes. The undeployment must be successful or in a failed state.
- If an NSX Manager cluster consists of nodes deployed from the VC (manual method) and nodes deployed from the NSX Manager UI, and you had to undeploy the manually deployed nodes, then you cannot remove the VC. To successfully remove the VC, ensure that you re-deploy an NSX Manager node from the VC.

This restriction applies to a fresh installation of NSX as well as an upgrade.