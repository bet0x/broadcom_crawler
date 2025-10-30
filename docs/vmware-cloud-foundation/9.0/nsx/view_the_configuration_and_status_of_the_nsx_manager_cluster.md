---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/managing-the-nsx-manager-cluster/view-the-configuration-and-status-of-the-nsx-manager-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > View the Configuration and Status of the NSX Manager Cluster
---

# View the Configuration and Status of the NSX Manager Cluster

You can view the
configuration and status of the
NSX Manager
cluster from the
NSX Manager UI.
You can get additional information using the CLI.

1. From your browser, log
   in with admin privileges to an
   NSX Manager at
   https://nsx-manager-ip-address.
2. Select
   SystemOverview

   The status
   of the
   NSX Manager
   cluster is displayed.
3. To see additional
   information about the configuration, run the following CLI command:

   ```
   manager1> get cluster config
   Cluster Id: 18807edd-56d1-4107-b7b7-508d766a08e3
   Cluster Configuration Version: 3
   Number of nodes in the cluster: 3

   Node UUID: 43cd0642-275c-af1d-fe46-1f5200f9e5f9
   Node Status: JOINED
       ENTITY                               UUID                                       IP ADDRESS      PORT     FQDN
       HTTPS                                5c8d01f1-f3ee-4f94-b517-a093d8fbfad3       10.160.71.225   443      ychin-nsxmanager-ob-12065118-1-F5
       CONTROLLER                           06fd0574-69c0-432e-a8af-53d140dbef8f       10.160.71.225   -        ychin-nsxmanager-ob-12065118-1-F5
       CLUSTER_BOOT_MANAGER                 da8d535e-7a0c-4dd8-8919-d88bdde006b8       10.160.71.225   -        ychin-nsxmanager-ob-12065118-1-F5
       DATASTORE                            3c9c4ec1-afef-47bd-aadb-1ed6a5536bc4       10.160.71.225   9000     ychin-nsxmanager-ob-12065118-1-F5
       MANAGER                              eb5e8922-23bd-4c3a-ae22-d13d9195a6bc       10.160.71.225   -        ychin-nsxmanager-ob-12065118-1-F5
       POLICY                               f9da1039-08ad-4a20-bacc-5b91c5d67730       10.160.71.225   -        ychin-nsxmanager-ob-12065118-1-F5

   Node UUID: 8ebb0642-201e-6a5f-dd47-a1e38542e672
   Node Status: JOINED
       ENTITY                               UUID                                       IP ADDRESS      PORT     FQDN
       HTTPS                                3757f155-8a5d-4b53-828f-d67041d5a210       10.160.93.240   443      ychin-nsxmanager-ob-12065118-2-F5
       CONTROLLER                           7b1c9952-8738-4900-b68b-ca862aa4f6a9       10.160.93.240   -        ychin-nsxmanager-ob-12065118-2-F5
       CLUSTER_BOOT_MANAGER                 b5e12db1-5e0d-4e33-a571-6ba258dceb2e       10.160.93.240   -        ychin-nsxmanager-ob-12065118-2-F5
       DATASTORE                            bee1f629-4e23-4ab8-8083-9e0f0bb83178       10.160.93.240   9000     ychin-nsxmanager-ob-12065118-2-F5
       MANAGER                              45ccd6e3-1497-4334-944c-e6bbcd5c723e       10.160.93.240   -        ychin-nsxmanager-ob-12065118-2-F5
       POLICY                               d5ba5803-b059-4fbc-897c-3aace8cf1219       10.160.93.240   -        ychin-nsxmanager-ob-12065118-2-F5

   Node UUID: 2e7e0642-df4a-b2ec-b9e8-633d1469f1ea
   Node Status: JOINED
       ENTITY                               UUID                                       IP ADDRESS      PORT     FQDN
       HTTPS                                bce3cc4c-7d60-45e2-aa7b-cdc75e445a14       10.160.76.33    443      ychin-nsxmanager-ob-12065118-3-F5
       CONTROLLER                           ced46f5c-9e52-4b31-a1cb-b3dead991c71       10.160.76.33    -        ychin-nsxmanager-ob-12065118-3-F5
       CLUSTER_BOOT_MANAGER                 88b70d31-3428-4ccc-ab57-55859f45030c       10.160.76.33    -        ychin-nsxmanager-ob-12065118-3-F5
       DATASTORE                            fb4aec3c-cae3-4386-b5b9-c0b99b7d9048       10.160.76.33    9000     ychin-nsxmanager-ob-12065118-3-F5
       MANAGER                              82b07440-3ff6-4f67-a1c9-e9327d1686ad       10.160.76.33    -        ychin-nsxmanager-ob-12065118-3-F5
       POLICY                               61f21a78-a56c-4af1-867b-3f24132d53c7       10.160.76.33    -        ychin-nsxmanager-ob-12065118-3-F5
   ```
4. To see additional
   information about the status, run the following CLI command:

   ```
   manager1> get cluster status
   Cluster Id: 18807edd-56d1-4107-b7b7-508d766a08e3
   Group Type: DATASTORE
   Group Status: STABLE

   Members:
       UUID                                       FQDN                                       IP               STATUS
       43cd0642-275c-af1d-fe46-1f5200f9e5f9       ychin-nsxmanager-ob-12065118-1-F5          10.160.71.225    UP
       8ebb0642-201e-6a5f-dd47-a1e38542e672       ychin-nsxmanager-ob-12065118-2-F5          10.160.93.240    UP
       2e7e0642-df4a-b2ec-b9e8-633d1469f1ea       ychin-nsxmanager-ob-12065118-3-F5          10.160.76.33     UP

   Group Type: CLUSTER_BOOT_MANAGER
   Group Status: STABLE

   Members:
       UUID                                       FQDN                                       IP               STATUS
       43cd0642-275c-af1d-fe46-1f5200f9e5f9       ychin-nsxmanager-ob-12065118-1-F5          10.160.71.225    UP
       8ebb0642-201e-6a5f-dd47-a1e38542e672       ychin-nsxmanager-ob-12065118-2-F5          10.160.93.240    UP
       2e7e0642-df4a-b2ec-b9e8-633d1469f1ea       ychin-nsxmanager-ob-12065118-3-F5          10.160.76.33     UP

   Group Type: CONTROLLER
   Group Status: STABLE

   Members:
       UUID                                       FQDN                                       IP               STATUS
       7b1c9952-8738-4900-b68b-ca862aa4f6a9       ychin-nsxmanager-ob-12065118-2-F5          10.160.93.240    UP
       ced46f5c-9e52-4b31-a1cb-b3dead991c71       ychin-nsxmanager-ob-12065118-3-F5          10.160.76.33     UP
       06fd0574-69c0-432e-a8af-53d140dbef8f       ychin-nsxmanager-ob-12065118-1-F5          10.160.71.225    UP

   Group Type: MANAGER
   Group Status: STABLE

   Members:
       UUID                                       FQDN                                       IP               STATUS
       43cd0642-275c-af1d-fe46-1f5200f9e5f9       ychin-nsxmanager-ob-12065118-1-F5          10.160.71.225    UP
       8ebb0642-201e-6a5f-dd47-a1e38542e672       ychin-nsxmanager-ob-12065118-2-F5          10.160.93.240    UP
       2e7e0642-df4a-b2ec-b9e8-633d1469f1ea       ychin-nsxmanager-ob-12065118-3-F5          10.160.76.33     UP

   Group Type: POLICY
   Group Status: STABLE

   Members:
       UUID                                       FQDN                                       IP               STATUS
       43cd0642-275c-af1d-fe46-1f5200f9e5f9       ychin-nsxmanager-ob-12065118-1-F5          10.160.71.225    UP
       8ebb0642-201e-6a5f-dd47-a1e38542e672       ychin-nsxmanager-ob-12065118-2-F5          10.160.93.240    UP
       2e7e0642-df4a-b2ec-b9e8-633d1469f1ea       ychin-nsxmanager-ob-12065118-3-F5          10.160.76.33     UP

   Group Type: HTTPS
   Group Status: STABLE

   Members:
       UUID                                       FQDN                                       IP               STATUS
       43cd0642-275c-af1d-fe46-1f5200f9e5f9       ychin-nsxmanager-ob-12065118-1-F5          10.160.71.225    UP
       8ebb0642-201e-6a5f-dd47-a1e38542e672       ychin-nsxmanager-ob-12065118-2-F5          10.160.93.240    UP
       2e7e0642-df4a-b2ec-b9e8-633d1469f1ea       ychin-nsxmanager-ob-12065118-3-F5          10.160.76.33     UP
   ```