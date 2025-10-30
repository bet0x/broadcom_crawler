---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitor-the-vsan-cluster/about-reserved-capacity-in-vsan-cluster/configure-reserved-capacity-for-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configure Reserved Capacity for vSAN Cluster
---

# Configure Reserved Capacity for vSAN Cluster

You can configure reserved capacity for a vSAN cluster to reserve capacity for internal operations.

You can also configure reserve capacity to reserve capacity for data repair following a single ESX host failure. Ensure that you have the following required privileges: Host.Inventory.EditCluster and Host.Config.Storage.

Verify that the vSAN cluster:

- Is not configured as a vSAN stretched cluster or two-node cluster.
- Has no fault domains and nested fault domains created.
- Has a minimum of four ESX hosts.

1. In the vSphere Client, navigate to the cluster.
2. Click the Configure tab.
3. Under vSAN, select Services.
4. Click to edit the Reservations and Alerts.
5. Click to activate or deactivate the operations reserve. On enabling the operations reserve, vSAN ensures that the cluster has enough space to complete the internal operations such as rebalancing, host rebuild, and so on.
6. Click to enable or deactivate the ESX host rebuild reserve. On enabling the host rebuild reserve, vSAN provides the reservation of space to repair data back to compliance following a single host failure. You can enable the host rebuild reserve only after you enable the operations reserve. After enabling, if you deactivate the operations reserve, the host rebuild reserve gets automatically deactivated.
7. Select Customize alerts. You can set a customized threshold to receive warning and error alerts. The threshold percentage is calculated based on the available capacity, which is the difference between the total capacity and the reserved capacity. If you do not set a customized value, vSAN uses the default thresholds to generate alerts.
8. Click Apply.