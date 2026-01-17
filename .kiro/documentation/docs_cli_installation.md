# Installation
## macOS[](https://kiro.dev/docs/cli/installation/#macos)
You can natively install Kiro CLI for macOS at the command line.
`curl -fsSL https://cli.kiro.dev/install | bash`
Kiro will direct you to open your web browser, where you will follow the steps under [Authentication](https://kiro.dev/docs/cli/authentication).
## Linux AppImage[](https://kiro.dev/docs/cli/installation/#linux-appimage)
You can install Kiro CLI for Linux using the AppImage format, which is a portable format that works on most Linux distributions without requiring installation.
To install Kiro CLI for Linux using AppImage, complete the following procedure.
  1. Download Kiro CLI for Linux AppImage:


`https://desktop-release.q.us-east-1.amazonaws.com/latest/kiro-cli.appimage`
  1. Make the AppImage executable:
bash
```

chmod +x kiro-cli.appimage


```

  2. Run the AppImage:
bash
```

./kiro-cli.appimage


```

  3. Kiro will direct you to open your web browser, where you will follow the steps under [Authentication](https://kiro.dev/docs/cli/authentication).


## With a zip file[](https://kiro.dev/docs/cli/installation/#with-a-zip-file)
The setup for Linux integration with the Kiro CLI requires installing the appropriate file for your system, verifying the file, and installing the program.
### Install and update requirements[](https://kiro.dev/docs/cli/installation/#install-and-update-requirements)
  * You must be able to extract or "unzip" the downloaded package. If your operating system doesn't have the built-in unzip command, use an equivalent.
  * Kiro for command line requires glibc 2.34 or newer, which is included by default in most major Linux distributions released since 2021.
  * For older distributions with glibc versions earlier than 2.34, use the special musl-based version (indicated by `-musl.zip` in the filename).
  * Kiro for command line is supported on 64-bit x86_64 and ARM aarch64 versions of recent distributions of Fedora, Ubuntu, and Amazon Linux 2023.


### Checking your glibc version[](https://kiro.dev/docs/cli/installation/#checking-your-glibc-version)
To determine which version you need, check your glibc version:
```

ldd --version


```

If the version is 2.34 or newer, use the standard version. If it's older, use the musl version.
### To download the installation file[](https://kiro.dev/docs/cli/installation/#to-download-the-installation-file)
Choose the appropriate download command based on your system architecture and glibc version:
#### Standard version (glibc 2.34+)[](https://kiro.dev/docs/cli/installation/#standard-version-glibc-234)
##### Linux x86-64[](https://kiro.dev/docs/cli/installation/#linux-x86-64)
`curl --proto '=https' --tlsv1.2 -sSf 'https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-x86_64-linux.zip' -o 'kirocli.zip'`
##### Linux ARM (aarch64)[](https://kiro.dev/docs/cli/installation/#linux-arm-aarch64)
`curl --proto '=https' --tlsv1.2 -sSf 'https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-aarch64-linux.zip' -o 'kirocli.zip'`
#### Musl version (for glibc < 2.34)[](https://kiro.dev/docs/cli/installation/#musl-version-for-glibc--234)
##### Linux x86-64 with musl[](https://kiro.dev/docs/cli/installation/#linux-x86-64-with-musl)
`curl --proto '=https' --tlsv1.2 -sSf 'https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-x86_64-linux-musl.zip' -o 'kirocli.zip'`
##### Linux ARM (aarch64) with musl[](https://kiro.dev/docs/cli/installation/#linux-arm-aarch64-with-musl)
`curl --proto '=https' --tlsv1.2 -sSf 'https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-aarch64-linux-musl.zip' -o 'kirocli.zip'`
### To install Kiro CLI[](https://kiro.dev/docs/cli/installation/#to-install-kiro-cli)
  1. Unzip the installer:
```

unzip kirocli.zip


```

  2. Run the install program:
```

./kirocli/install.sh


```

By default, the files are installed to `~/.local/bin`.


## Ubuntu[](https://kiro.dev/docs/cli/installation/#ubuntu)
You can install Kiro CLI for Ubuntu using the .deb package.
To install Kiro CLI for Ubuntu, complete the following procedure.
  1. Download Kiro CLI for Ubuntu.


`wget https://desktop-release.q.us-east-1.amazonaws.com/latest/kiro-cli.deb`
  1. Install the package:
bash
```

sudo dpkg -i kiro-cli.deb
sudo apt-get install -f


```

  2. Launch Kiro CLI:
bash
```

kiro-cli


```

  3. Kiro will direct you to open your web browser, where you will follow the steps under [Authentication](https://kiro.dev/docs/cli/authentication).


## Proxy configuration[](https://kiro.dev/docs/cli/installation/#proxy-configuration)
Kiro CLI (v1.8.0 and later) supports proxy servers commonly used in enterprise environments. The CLI automatically respects standard proxy environment variables.
### Setting proxy environment variables[](https://kiro.dev/docs/cli/installation/#setting-proxy-environment-variables)
Configure proxy settings by setting these environment variables in your shell:
bash
```

# HTTP proxy for non-SSL traffic
export HTTP_PROXY=http://proxy.company.com:8080

# HTTPS proxy for SSL traffic  
export HTTPS_PROXY=http://proxy.company.com:8080

# Bypass proxy for specific domains
export NO_PROXY=localhost,127.0.0.1,.company.com


```

### Proxy with authentication[](https://kiro.dev/docs/cli/installation/#proxy-with-authentication)
For proxies requiring authentication:
bash
```

export HTTP_PROXY=http://username:password@proxy.company.com:8080
export HTTPS_PROXY=http://username:password@proxy.company.com:8080


```

### Troubleshooting proxy issues[](https://kiro.dev/docs/cli/installation/#troubleshooting-proxy-issues)
If you encounter proxy-related connection issues:
  * Verify proxy server accessibility and credentials
  * Ensure your corporate firewall allows connections to AWS endpoints
  * Contact your IT administrator if SSL certificate validation fails
  * Check that the proxy server supports the required protocols


## Uninstalling Kiro CLI[](https://kiro.dev/docs/cli/installation/#uninstalling-kiro-cli)
You can uninstall Kiro CLI if you no longer need it.
To uninstall Kiro CLI on macOS, run:
bash
```

kiro-cli uninstall


```

To uninstall Kiro CLI on Ubuntu, complete the following procedure.
  1. Use the apt package manager to remove the package:
bash
```

sudo apt-get remove kiro-cli


```

  2. Remove any remaining configuration files:
bash
```

sudo apt-get purge kiro-cli


```



## Debugging Kiro CLI[](https://kiro.dev/docs/cli/installation/#debugging-kiro-cli)
If you're having a problem with Kiro CLI, run `kiro-cli doctor` to identify and fix common issues.
### Expected output[](https://kiro.dev/docs/cli/installation/#expected-output)
bash
```

$ kiro-cli doctor

✔ Everything looks good!

Kiro CLI still not working? Run kiro-cli issue to let us know!


```

If your output doesn't look like the expected output, follow the prompts to resolve your issue. If it's still not working, use `kiro-cli issue` to report the bug.
### Common issues[](https://kiro.dev/docs/cli/installation/#common-issues)
Here are some common issues you might encounter when using Kiro CLI:
Authentication failures : If you're having trouble authenticating, try running `kiro-cli login` to re-authenticate.
Autocomplete not working : Ensure your shell integration is properly installed by running `kiro-cli doctor`.
SSH integration issues : Verify that your SSH server is properly configured to accept the required environment variables.
### Troubleshooting steps[](https://kiro.dev/docs/cli/installation/#troubleshooting-steps)
Follow these steps to troubleshoot issues with Kiro CLI:
  1. Run `kiro-cli doctor` to identify and fix common issues.
  2. Check your internet connection.
  3. Verify that you're using a supported environment. For more information, see [Supported command line environments](https://kiro.dev/docs/cli/reference/supported-environments).
  4. Try reinstalling Kiro CLI.
  5. If the issue persists, report it using `kiro-cli issue`.


Page updated: November 18, 2025
[Authentication](https://kiro.dev/docs/cli/authentication/)
On this page
  * [macOS](https://kiro.dev/docs/cli/installation/#macos)
  * [Linux AppImage](https://kiro.dev/docs/cli/installation/#linux-appimage)
  * [With a zip file](https://kiro.dev/docs/cli/installation/#with-a-zip-file)
  * [Install and update requirements](https://kiro.dev/docs/cli/installation/#install-and-update-requirements)
  * [Checking your glibc version](https://kiro.dev/docs/cli/installation/#checking-your-glibc-version)
  * [To download the installation file](https://kiro.dev/docs/cli/installation/#to-download-the-installation-file)
  * [Standard version (glibc 2.34+)](https://kiro.dev/docs/cli/installation/#standard-version-glibc-234)
  * [Musl version (for glibc < 2.34)](https://kiro.dev/docs/cli/installation/#musl-version-for-glibc--234)
  * [To install Kiro CLI](https://kiro.dev/docs/cli/installation/#to-install-kiro-cli)
  * [Ubuntu](https://kiro.dev/docs/cli/installation/#ubuntu)
  * [Proxy configuration](https://kiro.dev/docs/cli/installation/#proxy-configuration)
  * [Setting proxy environment variables](https://kiro.dev/docs/cli/installation/#setting-proxy-environment-variables)
  * [Proxy with authentication](https://kiro.dev/docs/cli/installation/#proxy-with-authentication)
  * [Troubleshooting proxy issues](https://kiro.dev/docs/cli/installation/#troubleshooting-proxy-issues)
  * [Uninstalling Kiro CLI](https://kiro.dev/docs/cli/installation/#uninstalling-kiro-cli)
  * [Debugging Kiro CLI](https://kiro.dev/docs/cli/installation/#debugging-kiro-cli)
  * [Expected output](https://kiro.dev/docs/cli/installation/#expected-output)
  * [Common issues](https://kiro.dev/docs/cli/installation/#common-issues)
  * [Troubleshooting steps](https://kiro.dev/docs/cli/installation/#troubleshooting-steps)