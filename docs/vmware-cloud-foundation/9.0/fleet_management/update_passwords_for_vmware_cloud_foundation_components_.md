---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/manage-passwords/update-passwords.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Update Passwords for VMware Cloud Foundation Components 
---

# Update Passwords for VMware Cloud Foundation Components

For security reasons, you can change passwords for the accounts that are used by VMware Cloud Foundation components. Changing these passwords periodically or when certain events occur, such as an administrator leaving your organization, reduces the likelihood of security vulnerabilities.

- Verify that there are no failed workflows. To check for failed workflows, click Fleet ManagementTasks in the VCF Operations console.
- Verify that no active workflows are running or are scheduled to run during the password update.
- The user's role must include the following permissions:
  - Fleet Management: Passwords:Manage.
  - Fleet Management: Passwords:View.

You can update only one password at a time.

Although individual components support different password requirements, it is recommended that you set passwords following a common set of requirements across all accounts:

- Minimum length: 15
- Maximum length: 20
- At least one lowercase letter, one uppercase letter, a number, and one of the following special characters: ! @ # $ ^ \*
- Must NOT include:
  - A dictionary word
  - A palindrome
  - More than four monotonic character sequences
  - Three of the same consecutive characters

1. In the VCF Operations console, click Fleet ManagementPasswords .
2. Click VCF Management or click VCF Instances and click a VCF Instance or VCF domain name.
3. Select a component and click Update Password.
4. Enter and confirm the new password.
5. Click Update Password. 

   A message appears at the top of the page showing the progress of the operation.