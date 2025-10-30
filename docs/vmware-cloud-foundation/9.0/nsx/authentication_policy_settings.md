---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/authentication-policy-settings.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Authentication Policy Settings
---

# Authentication Policy Settings

You can view or customize your authentication policy settings through the API and CLI.

Some details are important to understand about viewing or changing policy settings.

- This feature allows one password policy only.
- Changes to the password configuration affects new users immediately. After administrators update existing user password configurations current users must follow updated password configuration changes.
- API configuration changes take about 20 seconds to take effect.
- For NSX Edge, changed passwords are not synchronized across the cluster. Both CLI and API changes appear in one node.
- Appliance transport node support includes BCG, autonomous Edge, or Unified Appliances (UA). There is no support for transport node password configuration changes for the local administrator or the auditor user in ESX.
- Privileged Access Management (PAM) supports setting minimum or maximum password length, but not both settings.
- Use of negative numbers for password entries sets the minimum range while positive numbers set the maximum range. To keep the existing default, leave the response empty.
- If modified pre-upgrade, the password policy configuration remains the same post upgrade for existing users. NSX Manager does not enforce the default password policy in this case.
- Authentication policies

  ```
  [API] /api/v1/node/aaa/auth-policy
  ```

  ```
  [API] /api/v1/cluster/<Node-UUID>/node/aaa/auth-policy
  ```

  ```
  [API] /api/v1/transport-nodes/<transport-node-id>/node/aaa/auth-policy
  ```

NSX Manager includes the following CLI and API password complexity and authentication command support. These password policy options now sync across the management cluster nodes. Viewing password details does not require any permissions. Modifying existing password defaults requires admin permissions.

For more information on defaults ranges and other details, see the NSX Command-Line Interface Reference and the NSX API Guide.

CLI Password Policy Customizable Options



| Password Option | CLI Command |
| --- | --- |
| View or configure password complexity configuration | ``` get password-complexity ```  ``` Wed Jun 08 2022 UTC 12:57:45.325 - minimum 12 characters in length - maximum 128 characters in length - minimum 1 lowercase characters - minimum 1 uppercase characters - minimum 1 numeric characters - minimum 1 special characters - default password complexity rules as enforced by the Linux PAM module ```  ``` set password-complexity ```   You can change specific parameters using these arguments:   ``` Minimum password length (leave empty to not change): Maximum password length (leave empty to not change): Lower characters (leave empty to not change): Upper characters (leave empty to not change): Numeric characters (leave empty to not change): Special characters (leave empty to not change): Minimum unique characters (leave empty to not change): Allowed similar consecutives (leave empty to not change): Allowed monotonic sequence (leave empty to not change): Hash algorithm (leave empty to not change): Password remembrance (leave empty to not change): ``` |
| View authentication policy | ``` get auth-policy cli ```  ``` lockout-period   Lockout period max-auth-failures Maximum authentication failures before lockout ``` |
| Configure authentication policy | ``` set auth-policy cli ```  ``` lockout-period   Lockout period max-auth-failures Maximum authentication failures before lockout ``` |

API Password Policy Customizable Options



| Password Option | API Commands |
| --- | --- |
| View password complexity and authorization policy | ``` get /api/v1/node/aaa/auth-policy ```  ``` { "_retry_prompt": 3, "_schema": "AuthenticationPolicyProperties", "_self": {    "href": "/node/aaa/auth-policy",    "rel": "self" }, "api_failed_auth_lockout_period": 5, "api_failed_auth_reset_period": 900, "api_max_auth_failures": 900, "cli_failed_auth_lockout_period": 900, "cli_max_auth_failures": 5, "digits": -1, "hash_algorithm": "sha512", "lower_chars": -1, "max_repeats": 0, "max_sequence": 0, "maximum_password_length": 128, "minimum_password_length": 12, "minimum_unique_chars": 0, "password_remembrance": 0, "special_chars": -1, "upper_chars": -1 } ``` |
| View Workspace ONE Access(VIDM) authorization policy | ``` get auth-policy vidm ```  ``` Wed Jun 08 2022 UTC 12:58:28.357 LB Enabled: False Enabled: False Hostname: Thumbprint: Client Id: Node Hostname: ``` |
| Configure VIDM authorization policy | ``` set auth-policy vidm ```  ``` enabled  Enabled property hostname  System’s network name lb-extern External Load Balancer Flag For vIDM Wiring ``` |
| Configure password complexity and authorization policy  - API failed authorization attempts lockout period (in seconds) | ``` put /api/v1/node/aaa/auth-policy ```  ``` lockout_period <lockout-period-arg> ``` |
| - Authentication failure lockout reset period | ``` lockout_reset_period ``` |
| - Number of failures allowed before API lockout | ``` max_auth_failures ``` |
| - Number of numeric characters | ``` digits ``` |
| - Hash algorithm | ``` hash_algorithm ``` |
| - Number of lowercase characters | ``` lower_chars ``` |
| - Sequence of same characters | ``` max_repeats ``` |
| - Maximum monotonic character sequence (1234 or DCBA) | ``` max_sequence ``` |
| - Maximum password length | ``` maximum_password_length ``` |
| - Minimum password length | ``` minimum_password_length ``` |
| - Minimum unique characters | ``` minimum_unique_chars ``` |
| - Minimum number of password reuse | ``` password_remembrance ```   - If 0, the check for previous passwords is disabled and users can reuse any previous password. Default. - If you enter a number, the user cannot reuse that number of previous passwords. For example, if set to 2, the user cannot reuse the last two passwords. |
| - Number of special characters | ``` special_chars ``` |
| - Number of uppercase characters | ``` upper_chars ``` |
| Reset password complexity, authentication policy, or both | For node, transport-nodes, and clusters:  ``` reset-password-complexity ```  ``` reset-auth-policies ```  ``` reset-all ``` |