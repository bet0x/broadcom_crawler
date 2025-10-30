---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/git/integrating-with-git.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configuring Source Control in VCF Operations
---

# Configuring Source Control in VCF Operations

You can configure source control settings in VCF Operations to synchronize configuration templates to and from a repository.

- Verify that your VCF Operations fleet management can establish a connection to the appropriate the source control solution.
- Ensure bi-directional HTTPS connectivity between the VCF Operations management appliance and the Git repository.
- Verify that you are using a supported source control solution.
- Generate access tokens to authenticate and authorize a secure connection to the repositories.

  - **GitLab**: Generate an access token for your repository following the [documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) from GitLab.

    The access token must have the Maintainer or Owner role. Ensure the access token has an expiration date and the following scopes:

    - Read access to the repository. (i.e. read\_repository in GitLab)
    - Write access to the repository. (i.e. write\_repository in GitLab)
    - Read access to the project. (i.e. read\_api in GitLab)
    - Read and write access to the project. (i.e. api in Gitlab)
  - **GitHub**: Generate an access token for your repository following the [documentation](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) from GitHub.

1. To integrate source control in VCF Operations, from the left menu, click AdministrationControl Panel and then click Source Control.
2. For Source Control Type, select a source control solution.
3. Enter the Source Control Server address where the configuration templates will be stored.
4. Enter the access token from your source control type in the Access Key.
5. Specify the Branch for storing or reading content.
6. Provide the Repository path for storing or retrieving contents.
7. By default, Code Review is enabled by default. The code review process creates a merge request for any operation on a configuration template. The content syncs to the repository after the merge request is approved.

   To disable the code review process, uncheck the Code Review checkbox.
8. Click Test Connection to verify if the integration is successful. If the Connection Result is successful, click Save to complete the integration.

After the setup is complete, you can manage the configuration templates from your source control solution.

**Template Organization and Repository Structure**: Configuration templates are automatically created and organized in a defined folder structure: Operations-ConfigTemplate/config-templates/vCenter. Each template must be stored in a unique folder in the source control repository.

**Template Name and Storage**: Each configuration template must have a unique name to avoid duplication.

**Template Content and File Structure**: For each configuration template, three files are automatically created in the repository:

1. <templatename>-desiredState.json: Contains the desired state of the template.
2. <templatename>-metaData.json: Contains metadata information like template name, version, and selected configuration.
3. <templatename>-manifest.json: Used to manage and maintain the template's structure and metadata.