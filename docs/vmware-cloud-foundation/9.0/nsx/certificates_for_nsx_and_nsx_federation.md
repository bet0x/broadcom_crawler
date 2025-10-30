---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/certificates-for-nsx-and-nsx-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Certificates for NSX and NSX Federation
---

# Certificates for NSX and NSX Federation

The system creates certificates required for the communication between NSX appliances and external communication, including NSX Federation appliances. Read about the various certificate information.

In a federated NSX deployment, certificates originating from other locations will appear in the Certificates pane. Those certificates display with names starting with Site; for example, Site certificate L=PA,ST=CA,C=US, Site certificate UID=369cd66c-..., or with their UUID only 637a2ebf-84d1-4548-a0ba-51d9420672ff. If those certificates are expiring, replace them on the originating site where their corresponding private key is stored. You can find that information in the Used By field on the UI or in the API. If you replace the certificates on any originating Global Manager or Local Manager, the system automatically synchronizes them across the federated deployment.

The Certificates for NSX Manager table reflects certificate details including the span of time that certificates are valid for new deployments only. New certificates are not generated during upgrades, so certificate validity dates will reflect a previous NSX version's default certificate expiration date.To replace existing self-signed certificates with CA-signed certificates, refer to details in [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html#GUID-115fa563-2c50-4279-b471-d19b3136dc13-en). To read about security compliance events, refer to the [NSX Event Catalog](https://docs.vmware.com/en/VMware-NSX-Event-Catalog/index.html).

Certificates for NSX Manager Nodes



| Certificate Naming Convention | Purpose | Replaceable using service\_type | Default Validity |
| --- | --- | --- | --- |
| APH (aka APH\_AR) | Appliance Proxy hub (APH) server public key and Asynchronous Replicator for cross communication, for Federation | Yes, use service\_type=APH. | 825 days |
| APH\_TN | Appliance Proxy hub (APH) certificate for Transport node (TN) and intra-cluster communication | Yes, use service\_type=APH\_TN. | 825 days |
| API | API server certificate for NSX Manager node | Yes, use service\_type=API. | 825 days |
| CCP | Control Configuration Plane certificate to communicate with transport nodes | Yes, use service\_type=CCP. | 10 years |
| MGMT\_CLUSTER (aka VIP) | API Server certificate used by VIP | Yes, use service\_type=MGMT\_CLUSTER. | 825 days |
| CBM\_CLUSTER\_MANAGER | Corfu client certificate | Yes, use service\_type=CBM\_CLUSTER\_MANAGER. | 100 years |
| CBM\_CORFU | Corfu server certificate | Yes, use service\_type=CBM\_CORFU. | 100 years. |

## Certificates for NSX Federation Communication

By default, the Global Manager uses self-signed certificates for communicating with internal components, registered Local Managers, and for authentication for NSX Manager UI or APIs.

You can view the external (UI/API) and inter-site certificates in NSX Manager. The internal certificates are not viewable or editable.

Do not enable Local Manager external VIP before you register the Local Manager on the Global Manager. When NSX Federation and PKS need to be used on the same Local Manager, complete the PKS tasks to create an external VIP and change the Local Manager certificate before you register the Local Manager on Global Manager.

## Certificates for Global Managers and Local Managers

After you add a Local Manager into the Global Manager, a trust gets established by exchanging certificates between Local Manager and Global Manager. These certificates also get copied into each of the sites registered with the Global Manager. The certificate used to establish trust with the Global Manager gets generated only when the Local Manager registers with the Global Manager. That same certificate gets deleted if the Local Manager moves out of the NSX Federation environment.

See the Certificates for Global Managers and Local Managers table for a list of all the NSX Federation specific certificates created for each appliance and the certificates these appliances exchange with each other:

Certificates for Global Managers and Local Managers



| Naming Convention in the Global Manager or Local Manager | Purpose | Replaceable? | Default Validity |
| --- | --- | --- | --- |
| The following are certificates specific to each  NSX Federation  appliance. | | | |
| APH-AR certificate | - For the Global Manager and each Local Manager. - Used for inter-site communication using the AR channel (Async-Replicator channel). | Yes, use service\_type=APH. See [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html#GUID-115fa563-2c50-4279-b471-d19b3136dc13-en). | 10 years |
| GlobalManager | - For the Global Manager. - PI certificate for the Global Manager. | Yes, use service\_type=GLOBAL\_MANAGER. Refer to [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html#GUID-115fa563-2c50-4279-b471-d19b3136dc13-en). | 825 days |
| Cluster certificate | - For the Global Manager and each Local Manager. - Used for UI/API communication with the VIP of the Global Manager or Local Manager cluster. | Yes, use service\_type=MGMT\_CLUSTER. Refer to [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html#GUID-115fa563-2c50-4279-b471-d19b3136dc13-en). | 825 days |
| API certificate | - For the Global Manager and each Local Manager. - Used for UI/API communication with individual Global Manager and Local Manager nodes for each of the locations added to the Global Manager. | Yes, use service\_type=API. See [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html#GUID-115fa563-2c50-4279-b471-d19b3136dc13-en). | 825 days |
| LocalManager | - Starting with NSX 4.1, generates only when Local Manager servers are in the NSX Federation environment. The certificate gets deleted if the Local Manager moves out of the NSX Federation environment. - PI certificate for this specific Local Manager. | Yes, use service\_type=LOCAL\_MANAGER. See [Replace NSX Certificates Using API](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-api.html#GUID-115fa563-2c50-4279-b471-d19b3136dc13-en). | 825 days |
| The LM and the GM share their Cluster, API, and APH-AR certificates between them. If a certificate is CA-signed, the CA is synchronized, but that certificate is not. | | | |

## Principal Identity (PI) Users for NSX Federation

After you add a Local Manager to the Global Manager, the following PI users with corresponding roles get created.

Principal Identity (PI) Users Created for NSX Federation



| NSX Federation Appliance | PI User Name | PI User Role |
| --- | --- | --- |
| Global Manager | LocalManagerIdentity One for each Local Manager registered with this Global Manager. | Auditor |
| Local Manager | GlobalManagerIdentity | Enterprise Admin |
| LocalManagerIdentity One for each Local Manager registered with the same Global Manager. To get a list of all the Local Manager PI users because they are not visible in the UI, enter the following API: command  ``` GET https://<local-mgr>/api/v1/trust-management/principal-identities ``` | Auditor |