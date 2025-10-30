---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/cloud-proxy-faq.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Cloud Proxy FAQ
---

# Cloud Proxy FAQ

This topic covers some frequently asked questions about VCF Operations cloud proxy.

## Configuration

1. What are the prerequisites for setting up a cloud proxy account?

   Prerequisites are given in the topic, [Configuring Cloud Proxies in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/configuring-cloud-proxies-in-vrealize-operations-cloud.html#GUID-bd1eed2a-5668-4640-8ae3-79ce18f3d081-en).
2. What does one-way connection mean?

   Outbound connections are initiated from cloud proxy to VCF Operations, over https/443. Cloud proxy can also facilitate vCenter actions.
3. Which ports should be opened?

   The most up-to-date technical information about ports can be found on [Ports and Protocol](https://ports.broadcom.com/).
4. Which ports should be allowed for incoming traffic to cloud proxy?

   Allow port 443 https protocol for push model adapters like application monitoring or Suite-API on cloud proxy. Allow ports 4505, 4506, and 8443 via TCP protocol for application monitoring. Allow the VRRP protocol for intercommunication between cloud proxies in a application monitoring high availability activated collector group.
5. How do I edit environment settings for cloud proxy?

   You can edit vApp options. For more information, see [Edit OVF Details for a Virtual Machine](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_028&appid=vsphere-9-0&language=&format=rendered).
6. How are certificates managed?

   Certificates are managed by cloud proxies. But for any additional proxy servers with SSL communication, you need to provide certificate(s).
7. What credential is used to login to cloud proxy?

   You can login as the “root” user. You are expected to set a new password on the first login to cloud proxy VM.

   SSH access is disabled by default, so the first login must be done via the vCenter console. You can run the following command to start SSH service:

   ```
   systemctl start sshd
   systemctl enable sshd
   ```

   To reset password, see the VMware KB Article, [2001476](https://kb.vmware.com/s/article/2001476).
8. Will I be notified if the connection between cloud proxy and VCF Operations breaks down?

   You can configure alerts/notifications on the VCF Operations cloud proxy object. For more information, see [Monitoring the Health of Cloud Proxies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies.html#GUID-6887a5cc-2bce-41e9-b965-603887775adb-en).

   VCF Operations automatically generates notifications for the following scenarios:
   - Cloud proxy is not reachable.
   - Cloud proxy is nearing sizing limits.
9. How do I change account for cloud proxy?

   You can edit vApp options. For more information, see [Edit OVF Details for a Virtual Machine](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_028&appid=vsphere-9-0&language=&format=rendered).
10. How can I check the status of cloud proxy?

    For more information, see [Monitoring the Health of Cloud Proxies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/monitoring-the-health-of-cloud-proxies.html#GUID-6887a5cc-2bce-41e9-b965-603887775adb-en).
11. Should I use Remote Collector or cloud proxy for monitoring?

    VMware recommends that you use cloud proxy to take advantage of the latest enhancements. Also, application monitoring, HA of collector groups, and data persistence are only supported through cloud proxy.

## Sizing

1. How should I size the cloud proxy?

   For information on sizing, see the VMware KB article [85832](https://kb.vmware.com/s/article/85832).

## Upgrade

1. How do I upgrade cloud proxy?

   Cloud proxy is upgraded automatically. In case the upgrade fails, see the VMware KB article [80590](https://kb.vmware.com/s/article/80590).

## High Availability

1. Is high availability supported?

   Cloud proxy supports high availability. You can add multiple cloud proxies to a collector group. If the collecting cloud proxy fails or gets disconnected, collection can be picked up by another proxy in the group.

   Since the failover is initiated after a period of 10 minutes, few collection cycles are lost.

To troubleshoot cloud proxy issues, see [Cloud Proxy Troubleshooting](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/cloud-proxy-troubleshooting.html#GUID-dc2ae994-1896-4bc6-8310-2790be403ec9-en_GUID-CB136C86-10BD-4253-A71E-37B2D7263A57).