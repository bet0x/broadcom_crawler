---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/vsan-file-service/edit-vsan-file-service.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Edit vSAN File Service
---

# Edit vSAN File Service

You can edit and reconfigure the settings of a vSAN file service.

- If there are active shares, changing the Active Directory domain is not permitted as this action can disrupt the user permissions on the active shares.
- If your Active Directory password has been changed, then you can edit the Active Directory configuration settings and provide the new password.

  This action might cause minor disruption to the inflight I/Os on the file shares.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, click Services.
4. On the File Service row, click Edit > Edit domain.

   The File Service Domain wizard opens.
5. In the File Service Domain page, edit the file service domain name and click Next.
6. In the Networking page, make the appropriate configuration changes and click Next. You can edit the primary IP addresses, static IP addresses, and DNS names. You can add or remove the primary IP addresses or static IP addresses. You cannot change the DNS name without changing the IP.

   Changing domain information is a disruptive action. It might require all clients to use new URLs to reconnect to the file shares.
7. In the Directory service page, make appropriate directory related changes if required, and click Next.

   You cannot change the AD domain, organizational unit, and username after initially configuring vSAN file services.
8. In the Review page, click Finish after making necessary changes.

The changes are applied to the vSAN file service configuration.