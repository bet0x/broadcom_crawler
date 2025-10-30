---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-a-standalone-or-clustered-vrealize-orchestrator-8-0-1-deployment-with-iso-image.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Upgrading Standalone or Clustered VCF Operations Orchestrator Deployments
---

# Upgrading Standalone or Clustered VCF Operations Orchestrator Deployments

You can upgrade your VMware Aria Automation Orchestrator deployment to VCF Operations orchestrator by using a mounted ISO image.

Verify that you are upgrading a VMware Aria Automation Orchestrator 8.18.1 deployment to VCF Operations orchestrator 9. Upgrades from earlier product versions are not supported.

1. Download and mount the ISO image.
   1. Download the ISO image from the official Broadcom download site.
   2. Connect the CD-ROM drive of the Automation Orchestrator Appliance virtual machine in vSphere. See the vSphere Virtual Machine Administration documentation.

      After connecting the CD-ROM drive, navigate to your Automation Appliance VM settings page and verify that Connect At Power On is enabled.
   3. Mount the ISO image to the CD-ROM drive of the Automation Orchestrator Appliance virtual machine in vSphere. See the vSphere Virtual Machine Administration documentation.
2. Log in to the Automation Orchestrator Appliance command line as root.
3. Run the blkid command, and note the device name for the Automation Orchestrator Appliance CD-ROM drive.
4. Mount the CD-ROM drive.

   ```
               mount /dev/xxx /mnt/cdrom
   ```

   For clustered Automation Orchestrator deployments, you must perform steps 2 and 3 on all nodes in the cluster.
5. Back up your Automation Orchestrator deployment by taking a virtual machine snapshot. See [Take a Snapshot of a Virtual Machine](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-virtual-machine-administration-guide-8-0/managing-virtual-machinesvsphere-vm-admin/using-snapshots-to-manage-virtual-machinesvsphere-vm-admin/managing-existing-snapshotsvsphere-vm-admin/take-snapshots-of-a-virtual-machinevsphere-vm-admin.html).

   Automation Orchestrator 8.x does not currently support memory snapshots. Before taking the snapshot of your deployment, verify that the Snapshot the virtual machine’s memory option is deactivated.
6. To initiate the upgrade, run the vracli upgrade exec -y --repo cdrom:// command on one of the nodes in your deployment.

   For Automation Orchestrator deployments authenticated with vSphere, you must provide the credentials of the user who registered your deployment with the vCenter Single Sign-On (SSO) service. You can verify the identity of this user either in the /data/vco/usr/lib/vco/app-server/conf/sso.properties path in the virtual appliance, or in the output of the vracli vro authentication command. You can either enter the password manually or export the your password as a environmental variable. This can be useful for scenarios where you are using an automated script to upgrade multiple Automation Orchestrator deployments. To export the SSO password, run the export VRO\_SSO\_PASSWORD=your\_sso\_password command.

   During the upgrade, you are automatically logged out of your terminal, because the Automation Orchestrator Appliance reboots.
7. Log in to the Automation Orchestrator Appliance command line as root and follow the upgrade progress by running the vracli upgrade status --follow command.

   The vracli upgrade status --follow command can occasionally display a false error message that indicates that the upgrade has failed. To troubleshoot this problem, see step 8.
8. If you receive an error message while running the vracli upgrade status --follow  command, follow these steps:
   1. Verify that you receive the following error message:

      ```
      Running health check after upgrade for nodes and pods.
      Health check after upgrade for nodes and pods failed.
      ... Upgrade terminated due to critical error. Follow the upgrade guide to recover the system. ...
      ```
   2. Navigate to the /var/log/vmware/prelude/upgrade-report-latest and confirm that you receive the following error:

      ```
      Pod: vco-app-xxxx is not in Ready or Completed state. All pods must be in either of these states
      ```
   3. Run the kubectl get pods -n prelude -w | grep -E 'vco|orchestration-ui' command and verify that the status of all 3 vco-app pods and the orchestration-up-app pod is RUNNING.

      It can take up to 5-10 minutes after receiving the error message for all pods to enter the RUNNING state.

      ```
      orchestration-ui-app-xxxx    1/1     Running   0          5h42m
      vco-app-xxxx              3/3     Running   0          5h47m
      ```
   4. Run the curl -k https://<your\_orchestrator\_FQDN>/vco/api/healthstatus command and verify that the health check is returning a RUNNING status.

      ```
      {"state":"RUNNING","health-status":{"state":"OK","time":1615296823325},"instance-id":"your_orchestrator_FQDN"}
      ```

      The preceding command must run in an environment different from the Automation Orchestrator command line. You can run the command from the command line of a different virtual machine. You can also view the health status information in a browser by navigating directly to https://<your\_orchestrator\_FQDN>/vco/api/healthstatus.

You have upgraded your Automation Orchestrator 8.18.1 deployment to VCF Operations orchestrator 9. If you encounter a notification stating that the upgrade has failed, see [False Upgrade Failure Notification](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/upgrade-a-standalone-or-clustered-vrealize-orchestrator-8-0-1-deployment-with-iso-image/the-vrealize-orchestrator-upgrade-fails-but-the-appliance-containers-are-up-and-running.html).

Validate that the Automation Orchestrator upgrade was successful by running the vracli version command in the command line of the appliance. By running this command, you can validate the product version and build number of VCF Operations orchestrator.