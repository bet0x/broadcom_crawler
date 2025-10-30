---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/using-the-monitoring-policy-workspace/policy-workspace/configuring-vcenter-pricing-details.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Configuring vCenter Pricing Details
---

# Configuring vCenter Pricing Details

You can add and assign new pricing cards to vCenter and Clusters in VCF Operations. The pricing card can be cost-based or rate-based, you can customize the cost-based pricing card and rate-based pricing card as per your requirement. After configuring the pricing card, you can assign it to one more vCenter or Clusters based on your pricing strategy.

If you want to copy the vCenter pricing settings from the policy currently being edited to another policy, click Copy local changes to other policy and select the policy to which you want to copy the settings. The copied pricing configuration will override any existing local pricing configuration, in the target policy.

1. From the left menu, click Infrastructure OperationsConfigurations, and then click the Policy Definition tile.
2. Select the required policy or click Add to add a new policy.
3. In the right pane, click Edit Policy.
4. In the <policy name> [Edit] workspace, click the VC Pricing card.
5. Click the Lock icon to override parent policy settings.
6. Select if you want to activate or deactivate the pricing engine.
7. Configure Basic Charges: Click the Lock icon to edit the parent policy settings. Pricing can be performed either on a cost basis or independent of it by specifying rate cards. The factor entered here is multiplied by the cost calculated as a derivative of cost drivers.

   1. Based on Cost/Based on Rate: Select if you want to pricing card to be cost-based or rate-based.

      The following options appear if you select the Based on Cost option:
      - CPU Cost: Enter a valid CPU cost factor.
      - Memory Cost: Enter a valid memory cost factor.
      - Storage Cost: Enter a valid storage cost factor.
      - Additional Cost: Enter a valid additional cost factor.

      The following options appear if you select the Based on Rate option:
      - CPU Rate: Enter the CPU Rate per vCPU, the charging period, and how to charge for the resources.
      - Memory Rate: Enter the memory rate per GB, the charging period, and how to charge for the resources.
      - Storage Rate: Enter the storage rate per GB, the charging period, and how to charge for the resources.
8. Configure Guest OS Rate: Click Guest OS Rate in the left pane and then click the Lock icon to edit the parent policy settings. These are additional charges that have to be included based on the operating system running on the virtual machine. The name of the operating system should match exactly as discovered by VMware Tools.

   1. Click Create Guest OS Rate and enter the following details:
      - Guest OS Name: Enter a guest OS name.
      - Charge Period: The Charge Period indicates the frequency of charging.
      - Base Rate: Enter a base rate.

      The guest OS rates that you add appear in the table below. To edit or delete the entries, click the vertical ellipses and select the desired option.
9. Tags: Click Tags in the left pane and then click the Lock icon to edit the parent policy settings. Tag-based charges can be used to charge for value-added services such as antivirus database disaster recovery and other applications. These applications are to be represented as vCenter tags on the VMs for these charges to work.

   1. Recurring Charges: Recurring charges represent repeating charges such as monthly license fees for antivirus software. Click Add Recurring Tag and enter the following details:
      - Tag Category: Enter a tag key.
      - Tag Value: Enter a tag value.
      - Base Rate: Enter a base rate.
      - Charge Period: The Charge Period indicates the frequency of charging.
      - Charge Based on Power State: This decides whether the charge should be applied based on the power state of the VM.

      The tags that you add appear in the table below. To edit or delete the entries, click the vertical ellipses and select the desired option.
   2. One Time Tag: Tag-based one-time charges can be used to represent incidental charges such as charges for addressing a support ticket or charges for applying an operating systems patch. Click Add One Time Tag and enter the following details:
      - Tag Category: Enter a tag key.
      - Tag Value: Enter a tag value.
      - Base Rate: Enter a base rate.

      The tags that you add appear in the table below. To edit or delete the entries, click the vertical ellipses and select the desired option.
   3. Rate Factor Tag: Rate factors are multiplication factors applied to already calculated charges. For example, to add a 50% premium on storage, set a rate factor of 1.5 to storage charge. Click Rate Factor Tag and enter the following details:
      - Tag Category: Enter a tag key.
      - Tag Value: Enter a tag value.
      - Charge Applies To: Select what the charge applies to.
      - Rate Factor: Enter a valid number. For example, if you want to increase the price of CPU which has a tag 'Tag1-Value1' by 20% then select CPU Charge from the Charge Applies To drop-down list and enter 1.2 in Rate Factor.

      The tags that you add appear in the table below. To edit or delete the entries, click the vertical ellipses and select the desired option.
10. Configure Overall Charges: Click Overall Charges in the left pane and then click the Lock icon to edit the parent policy settings. Overall Charges are flat charges that are applied to VMs that match this policy.

    1. VM Setup Charges: Enter a valid setup fee. This is to charge for the setup of the VMs.
    2. Recurring Charges: Enter a valid number.
    3. Charge Period: The Charge Period indicates the frequency of charging.

You can assign policies to the required Organization/Organization VDC under Infrastructure Operations Configurations, and then click the Policy Assignment tile. For details, see [Assigning Policies](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/configuring-policies/assigning-policies.html).